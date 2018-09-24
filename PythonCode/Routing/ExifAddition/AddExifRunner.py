from AddExif import copy_png_files_and_convert_to_jpg, get_gps_coords_default, getConfig
import os

def main():
	#write argparser for user to pass in which gps coords to use
	rav_numnber = 1
	
	config = getConfig()
	gps_lats, gps_longs, gps_alts = get_gps_coords_default(rav_numnber)
	png_folder = get_RAV_image_dir(rav_number)
	jpg_folder = get_RAV_JPG_image_dir + 'Drone{}Camera{}JPG'.format(rav_number, camera_number)
	
	#copy_png_files_and_convert_to_jpg(png_folder, jpg_folder, sorting_lambda = lambda file_name: int(file_name.split('_')[1].replace('.png','')),gps_lats, gps_longs, gps_alts = []
	

if __name__ == '__main__':
	main()