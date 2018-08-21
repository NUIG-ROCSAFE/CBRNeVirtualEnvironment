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

#parse config file, which contains locations of images gathered by RAV in AirSim
#and location of file where files with EXIF data attached should go

config = configparser.ConfigParser()
config.read('AddExif.conf')

os.chdir("../..")
base_dir = os.getcwd()
print("Working from directory: " + base_dir)
#files containing GPS locations
print('reading: ', base_dir + config['DEFAULT']['gpslocations1'])
gpslocations1 = open(base_dir + config['DEFAULT']['gpslocations1'], 'r' ).readlines()
#gpslocations2 = open(base_dir + config['DEFAULT']['gpslocations2'], 'r' ).readlines()
#gpslocations3 = open(base_dir + config['DEFAULT']['gpslocations3'], 'r' ).readlines()
gpslocations_files = [gpslocations1]
#, gpslocations2, gpslocations3]
print('gpslocations1: {}'.format(gpslocations1))

#the location of the folder to save images as jpg instead of png - this can actually be done from within airsim!
#images will be saved in JPGImages\Drone{}Camera{}.JPG
JPGImages = base_dir + config['DEFAULT']['jpg_images_location']
print('Using JPG Image directory: ', JPGImages)
#"D:\IJCAIDemoCode\PythonClientGPSMapping\GPSMappings\GPSAnnotatedImages\JPGImages"

#the location of the images saved by the RAVs from airsim. Must be in the format 
#image_{number}.png examples: image_20.png image_1.png
drone1Images = base_dir + config['DEFAULT']['drone1Images_location']
#drone2Images = base_dir + config['DEFAULT']['drone2Images_location']
#drone3Images = base_dir + config['DEFAULT']['drone3Images_location']



def copy_png_files_and_convert_to_jpg(drone_index, drone_images, camera_number):
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
            
			
copy_png_files_and_convert_to_jpg(1, drone1Images, 3)
#copy_png_files_and_convert_to_jpg(2, drone2Images, 3)
#copy_png_files_and_convert_to_jpg(3, drone3Images, 3)

write_exif_data(1, 3)
#write_exif_data(2, 3)
#write_exif_data(3, 3)


