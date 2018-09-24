import os
import shutil
from PIL import Image

def verify_file_exists(file_loc: str) -> bool:
	return os.path.isfile(file_loc)

def verify_dir_exists(dir_loc: str) -> bool:
	return os.path.isdir(dir_loc)
	
def copy_file(from_file_location: str, to_file_dir: str):
	'''Copies a png file from one folder to another'''
	#only tested for png files!
	if not verify_file_exists(from_file_location):
		raise Exception("File: {} does not exist".format(from_file_location))
	if not verify_dir_exists(to_file_dir):
		raise Exception("File: {} does not exist".format(to_file_dir))
	if from_file_location[-4:] != '.png':
		raise Exception("Source file extension must be .png, not {}".format(to_file_location[-3:]))
	
	shutil.copy2(from_file_location, to_file_dir)

def convert_png_to_jpg(file_location: str, delete_png = True) -> "copied jpg location":
	'''Converts a png file to a jpg file and removes the old png file'''
	if not verify_file_exists(file_location):
		raise Exception("File: {} does not exist".format(file_location))
	if file_location[-4:] != '.png':
		raise Exception("Source file extension must be .png, not {}".format(file_location[-3:]))
	#Image.open(file_location).convert('RGB').save(file_location[:-3] + 'jpg')
	Image.open(file_location).convert('RGB').save(file_location[:-3] + 'jpg',"JPEG", quality = 100)
	os.remove(file_location)
	return file_location[:-3] + 'jpg'