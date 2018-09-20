# -*- coding: utf-8 -*-

#dependencies: 
#exiftool https://www.sno.phy.queensu.ca/~phil/exiftool/
#

import subprocess
import os
import configparser
import os
import re
from PIL import Image
from ExifUtils.core import write_exif_gps_data
from ExifUtils.helpers import verify_file_exists, verify_dir_exists, copy_file, convert_png_to_jpg
#parse config file, which contains locations of images gathered by RAV in AirSim
#and location of file where files with EXIF data attached should go


def getConfig():
	config = configparser.ConfigParser()
	config.read('AddExif.conf')
	return config
	

def verify_gps_lats_longs(gps_lats, gps_longs):
	if len(gps_lats) != len(gps_longs):
		return False
	
	
def copy_png_files_and_convert_to_jpg(png_folder, jpg_folder, sorting_lambda = lambda file_name: int(file_name.split('_')[1].replace('.png','')),gps_lats, gps_longs, gps_alts = []):
	'''Given a folder containing png files and a corresponding csv file containing lat, 
	long, alt for images, will create a new folder in specified location, copy png files to 
	jpg and write GPS details to exif. If a file in png_folder is not png it will be copied to 
	to jpg folder but not converted.'''
	
	#check that jpg_folder exists
	if not verify_dir_exists(jpg_folder):
		print('Creating folder: {}'.format(jpg_folder))
		os.makedirs(jpg_folder)
		
	else:
		if os.listdir(jpg_folder) != []:
			print('{} is not an empty directory, may accidentally overwrite images'.format(jpg_folder))
	
	
	#first copy files from png_folder to jpg_folder if they are .png format
	for png_file in os.listdir(png_folder):
		try:
			copy_file(png_file, jpg_folder)
		except Exception as e:
		#don't try and deal with exception (may change this)
			raise e
		
	#now convert files to jpg
	for unconverted_png_file in os.listdir(jpg_folder):
		try:
			convert_png_to_jpg(unconverted_png_file, )
		except Exception as e:
		#don't try and deal with exception (may change this)
			raise e
	
	#process images by adding gps exif data. Assume that gps_lats and gps_longs are valid
	counter = 0
	for jpg_file in sorted(os.listdir(jpg_folder), key = sorting_lambda):
		write_exif_gps_data(gps_lats[counter], gps_longs[counter], gps_alts[counter])
		counter += 1
	
def get_gps_coords_default(rav_number):
	'''Gets lats, longs from default location in ROCSAFE project'''
	config = getConfig()
	curdir = os.path.realpath(__file__)
	os.chdir(curdir)
	os.chdir("../..")
	base_dir = os.getcwd()
	gps_coords = open(base_dir + config['DEFAULT']['gpslocations'] + str(rav_number) + ".txt", 'r' ).readlines()
	lats = [float(coord.split(',')[0]) for coord in gps_coords.split('\n')]
	longs = [float(coord.split(',')[1]) for coord in gps_coords.split('\n')]
	alts = [float(coord.split(',')[2]) for coord in gps_coords.split('\n')]
	return lats, longs, alts
	
def get_RAV_image_dir(rav_number):
	config = getConfig()
	curdir = os.path.realpath(__file__)
	os.chdir(curdir)
	os.chdir("../..")
	base_dir = os.getcwd()
	rav_png_images_loc = base_dir + config['DEFAULT']['RAVImages_location']
	return rav_png_images_loc + 'Drone{}Camera3'.format(rav_number)
	
def get_RAV_JPG_image_dir(rav_number):
	config = getConfig()
	curdir = os.path.realpath(__file__)
	os.chdir(curdir)
	os.chdir("../..")
	base_dir = os.getcwd()
	rav_jpg_dir = base_dir + config['DEFAULT']['jpg_images_location']
	return rav_jpg_dir
	
	
	
def get_gps_locations():
	gpslocations1 = open(base_dir + config['DEFAULT']['gpslocations1'], 'r' ).readlines()
	os.chdir("../..")

	base_dir = os.getcwd()
#print("Working from directory: " + base_dir)
#files containing GPS locations
#print('reading: ', base_dir + config['DEFAULT']['gpslocations1'])
#gpslocations1 = open(base_dir + config['DEFAULT']['gpslocations1'], 'r' ).readlines()
#gpslocations2 = open(base_dir + config['DEFAULT']['gpslocations2'], 'r' ).readlines()
#gpslocations3 = open(base_dir + config['DEFAULT']['gpslocations3'], 'r' ).readlines()
#gpslocations_files = [gpslocations1]
#, gpslocations2, gpslocations3]
#print('gpslocations1: {}'.format(gpslocations1))

#the location of the folder to save images as jpg instead of png - this can actually be done from within airsim!
#images will be saved in JPGImages\Drone{}Camera{}.JPG
#JPGImages = base_dir + config['DEFAULT']['jpg_images_location']
#print('Using JPG Image directory: ', JPGImages)
#"D:\IJCAIDemoCode\PythonClientGPSMapping\GPSMappings\GPSAnnotatedImages\JPGImages"

#the location of the images saved by the RAVs from airsim. Must be in the format 
#image_{number}.png examples: image_20.png image_1.png
#drone1Images = base_dir + config['DEFAULT']['drone1Images_location']
#drone2Images = base_dir + config['DEFAULT']['drone2Images_location']
#drone3Images = base_dir + config['DEFAULT']['drone3Images_location']



def copy_png_files_and_convert_to_jpg(drone_index, drone_images, camera_number):
    print('Copying files from directory {}'.format(drone_images))
    print("Converting {} images taken from RAV {} to jpg".format(len(os.listdir(drone_images)), drone_index))
    for image in sorted(os.listdir(drone_images), key=lambda x: int(re.findall("_[0-9]{1,4}", x)[0][1:])):
        png_im_loc = drone_images + '\\{}'.format(image)
        jpg_im_loc = JPGImages + '\Drone{}Camera{}'.format(drone_index, camera_number) + 'JPG' + '\\drone{}'.format(drone_index) + image.replace('png', 'jpg')
        print('Converting {} to jpg: {}'.format(png_im_loc, jpg_im_loc))
        im = Image.open(png_im_loc)
        rgb_im = im.convert('RGB')
        rgb_im.save(jpg_im_loc)

def write_exif_data(drone_index, camera_number):
	#remove any temp images in directory that exiftool may have created previously
	for image in os.listdir(JPGImages + '\Drone{}Camera{}JPG'.format(drone_index, camera_number)):
		if '_original' in image:
			os.remove(JPGImages + '\Drone{}Camera{}JPG'.format(drone_index, camera_number) + '\\' + image)
            
	try:
		gps_locs = gpslocations_files[drone_index-1]
		for image_loc, gpsLocation in zip(sorted(os.listdir(JPGImages + '\Drone{}Camera{}JPG'.format(drone_index, camera_number)), key = lambda x: int(re.findall("_[0-9]{1,4}", x)[0][1:])), gpslocations_files[drone_index-1]):
			#print(JPGImages + "\Drone{}Camera3JPG\{}'.format(drone_index, image_loc)")
			print(["exiftool", '-GPSLongitude={}'.format(gpsLocation.split(',')[1].replace('\n','').replace(' ','').replace(' ','').replace(' ','').replace(' ','')),  '-GPSLatitude={}'.format(gpsLocation.split(',')[0].replace('\n','').replace(' ','').replace(' ','').replace(' ','').replace(' ','')), '-GPSAltitude="32"', '-GPSVersionID=3 2 0 0','-gpsaltituderef=0', "-n", "-GPSLatitudeRef=N", "-GPSLongitudeRef=E", JPGImages + "\Drone{}Camera3JPG\{}".format(drone_index, image_loc)])
			print(subprocess.check_output(["exiftool", '-GPSLongitude={}'.format(gpsLocation.split(',')[1].replace('\n','').replace(' ','').replace(' ','').replace(' ','').replace(' ','')),  '-GPSLatitude={}'.format(gpsLocation.split(',')[0].replace('\n','').replace(' ','').replace(' ','').replace(' ','').replace(' ','')), '-GPSAltitude="32"', '-GPSVersionID=3 2 0 0','-gpsaltituderef=0', "-n", "-GPSLatitudeRef=N", "-GPSLongitudeRef=W",  JPGImages + "\Drone{}Camera{}JPG\{}".format(drone_index, camera_number, image_loc)]))
    
	except Exception as e:
		print(e)
		raise e
	#print(subprocess.check_output(["exiv2", "pr", "-p", "a",  "D:\IJCAIDemoCode\PythonClientGPSMapping\GPSMappings\Images\Images1\Camera3\image_4.png"]))    
	finally:
		#remove any temp images in directory that exiftool may have created
		for image in os.listdir(JPGImages + '\Drone{}Camera{}JPG'.format(drone_index, camera_number)):
			#os.rename('D:\IJCAIDemoCode\PythonClientGPSMapping\GPSMappings\GPSAnnotatedImages\JPGImages\Drone{}Camera3JPG'.format(drone_index) + '\\' + image, 'D:\IJCAIDemoCode\PythonClientGPSMapping\GPSMappings\GPSAnnotatedImages\JPGImages\Drone{}Camera3JPG'.format(drone_index) + '\\' + 'drone3' + image)
			if '_original' in image:
				os.remove(JPGImages + '\Drone{}Camera{}JPG'.format(drone_index, camera_number) + '\\' + image)
            
			
#copy_png_files_and_convert_to_jpg(1, drone1Images, 3)
#copy_png_files_and_convert_to_jpg(2, drone2Images, 3)
#copy_png_files_and_convert_to_jpg(3, drone3Images, 3)

write_exif_data(1, 3)
#write_exif_data(2, 3)
#write_exif_data(3, 3)


