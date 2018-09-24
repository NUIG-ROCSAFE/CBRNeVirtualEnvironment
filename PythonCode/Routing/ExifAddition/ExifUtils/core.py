# -*- coding: utf-8 -*-
from ExifUtils.helpers import verify_file_exists, verify_dir_exists, copy_file, convert_png_to_jpg
#dependencies: 
#exiftool https://www.sno.phy.queensu.ca/~phil/exiftool/
#

import subprocess
import os
import sys
import configparser
import datetime
import re
import pathlib

def get_exiftool_commands(tags_values: dict, image_loc:str):
	if tags_values:
		commands_list = ['-' + key + '=' + str(value) if value else '-' + key for key, value in tags_values.items()]
	else:
		commands_list = []
	commands_list.append(image_loc)
	return commands_list

def run_exiftool(tags_values: dict, image_loc: str):
	'''Runs exiftool with the given tags=value pairs in the tags_value dict'''
	commands_list = get_exiftool_commands(tags_values, image_loc)
	exiftool_location = str(pathlib.Path(os.path.dirname(os.path.abspath(__file__))).joinpath("../bin/exiftool-10.88/exiftool"))
	try:	
		return subprocess.check_output([exiftool_location] + commands_list)
	except Exception as e:
		raise type(e)('Could not run exiftool with commands: {}'.format(commands_list) + str(e)).with_traceback(sys.exc_info()[2])
		
	
def write_exif_gps_data(image_loc: str, gps_lat: float, gps_long: float, gps_alt: float = 32):
	'''Writes exif data to a specified jpg image'''
	return run_exiftool({'GPSLongitude': gps_long, 'GPSLatitude': gps_lat, 
	'GPSAltitude':'"{}"'.format(gps_alt), 'GPSVersionID':'3 2 0 0','gpsaltituderef':'0',
	"-n": None, "GPSLatitudeRef": 'N', "GPSLongitudeRef": "W"}, image_loc)
	
	#subprocess.check_output(["exiftool", '-GPSLongitude={}'.format(gps_long),  '-GPSLatitude={}'.format(gps_lat), '-GPSAltitude="{}"'.format(gps_alt), #'-GPSVersionID=3 2 0 0','-gpsaltituderef=0', "-n", "-GPSLatitudeRef=N", "-GPSLongitudeRef=W",  image_loc])
	
def write_exif_comment(image_loc: str, comment = ""):
	return run_exiftool({'Comment': comment}, image_loc)
	#subprocess.check_output(["exiftool", 'Comment={}'.format(comment), image_loc])
	
def write_exif_date_original( image_loc: str,date: str):
	'''Writes the date that the image was take at. date should be in the form %Y:%m:%d %H:%M:%S'''
	return run_exiftool({'datetimeoriginal': date}, image_loc)
	#subprocess.check_output(["exiftool", '"-datetimeoriginal={}"'.format(date), image_loc])
	
def write_exif_date_modified(image_loc: str,date: str):
	'''Writes the date that the image was take at. date should be in the form %Y:%m:%d %H:%M:%S'''
	return run_exiftool({'filemodifydate': date}, image_loc)
	
def write_author(image_loc, author: str):
	'''Writes the date that the image was take at. date should be in the form %Y:%m:%d %H:%M:%S'''
	return run_exiftool({'author': author}, image_loc)
	#subprocess.check_output(["exiftool", '"-datetimeoriginal={}"'.format(date), image_loc])

def process_image(from_file_location: str, to_dir_location: str, comment: str = '', tags: "list of strings", date: str, 
	gps_lat: float = None, gps_long: float = None, gps_alt: float = 32):
	'''Given a raw png image and metadata about that image, copies it to a specified location 
	in jpg format and writes metadata to exif'''
	copy_file(from_file_location, to_dir_location)
	file_name = os.path.basename(from_file_location)
	copied_png_location = pathlib.Path(to_dir_location).joinpath(file_name)
	print("converting {} to a jpg".format(str(copied_png_location)))
	jpg_location = convert_png_to_jpg(str(copied_png_location))
	if gps_lat!=None and gps_long!=None and gps_alt!=None:
		write_exif_gps_data(str(jpg_location), gps_lat, gps_long, gps_alt)
	if comment != None:
		write_exif_comment(str(jpg_location),comment)
	if date != None:
		write_exif_date_original(str(jpg_location), str(date))
	
def get_exif_data(image_loc: str) -> bytes:
	return run_exiftool({}, image_loc)
	
def get_exif_data_json(image_loc: str):
	return {item.split(':')[0].strip():item.split(':')[1].strip() for item in filter(lambda item: item, run_exiftool({}, image_loc).decode().split('\n'))}
	
	