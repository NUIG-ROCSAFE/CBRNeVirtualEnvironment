from AddExif import copy_png_files_and_convert_to_jpg, get_gps_coords_default, getConfig, get_RAV_image_dir, get_RAV_JPG_image_dir
import os

def main():
	#write argparser for user to pass in which gps coords to use
	rav_number = 1
	
	config = getConfig()
	gps_lats, gps_longs, gps_alts = get_gps_coords_default(rav_number)
	print(gps_lats,'\n', gps_longs, '\n',gps_alts)
	png_folder = get_RAV_image_dir(rav_number)
	print('png_folder: ', png_folder)
	jpg_folder = get_RAV_JPG_image_dir(rav_number)
#	+ 'Drone{}Camera{}JPG'.format(rav_number, camera_number)
	print('jpg_folder: ', jpg_folder)
	#png_folder, jpg_folder, gps_lats, gps_longs, gps_alts = [], sorting_lambda = lambda file_name: #int(file_name.split('_')[1].replace('.png',''))
	copy_png_files_and_convert_to_jpg(png_folder, jpg_folder, gps_lats, gps_longs, gps_alts)
	

if __name__ == '__main__':
	main()