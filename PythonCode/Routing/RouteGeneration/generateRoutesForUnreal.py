import argparse
import sys
import os
import configparser
from generateRoutesForUnrealUtils import generate_route_text, save_python_to_file, get_txt

def get_config() -> configparser.ConfigParser:
	config = configparser.ConfigParser()
	#read the global default config
	config.read(os.getcwd().replace("\\", "/") + '/../../../../Config/config.ini')
	print("Read config file from here: {}".format(os.getcwd().replace("\\", "/") + '/../../../../Config/config.ini'))
	return config
	
def create_folders_if_dont_exist():
	'''If default folders don't exist, create them'''
	pass


def main(no_ravs, no_cameras = 1, rav_velocity = 4, rav_altitude = 35, RAV_route_execution_dir = "", RAV_recorded_GPS_waypoints="", saved_images_dir=""):
	config = get_config()
	print('config: ', config.sections())
	print("Generating routes for ", no_ravs, " ravs")
	base_dir = os.path.abspath(__file__).split('PythonCode')[0].replace('\\', '/')[:-1]
	print("Generating routes using base directory: {}".format(base_dir))
	#READ DEFAULTS
	RAVGPSRoutesDir = base_dir + config["DATA"]["PlannedAgentRoutesDir"]
	
	if saved_images_dir == "":
			#saved_images_dir = base_dir + "/PythonCode/PythonClientGPSMapping/GPSMappings/Images"
			saved_images_dir = base_dir + config["DATA"]["CollectedPNGImagesDir"]
			
	#create saved images directory if not already in existence
	if not os.path.isdir(saved_images_dir):
			#exit program and ask for valid path
			print('Directory {} does not exist, creating'.format(saved_images_dir))
			os.makedirs(saved_images_dir)
	
	
	if RAV_recorded_GPS_waypoints == "":
		RAV_recorded_GPS_waypoints = base_dir + config["DATA"]["RAVRecordedGPSWaypoints"]
		#RAV_recorded_GPS_waypoints = base_dir + "/PythonCode/PythonClientGPSMapping/GPSMappings/GPSCoords"
		
	#create route execution directory if not already in existence
	if RAV_route_execution_dir == "":
		RAV_route_execution_dir = base_dir + config['PYTHON']['PythonRAVRouteExecutionDir']
		#RAV_route_execution_dir = base_dir + "/PythonCode/PythonGridMapping/AirSimPythonClient"
		
	#create recorded waypoints directory if not already in existence
	if not os.path.isdir(RAV_recorded_GPS_waypoints):
		print('Directory {} does not exist, creating in default location'.format(saved_images_dir))
		os.makedirs(RAV_recorded_GPS_waypoints)
		
	#create images directory
	for rav_no in range(int(no_ravs)):
		if not os.path.isdir(saved_images_dir + config['DATA']['RAVImagesDirFormatStr'].format(rav_no + 1)):
			os.makedirs(saved_images_dir + config['DATA']['RAVImagesDirFormatStr'].format(rav_no + 1))
		for camera_no in range(int(no_cameras)):
			if not os.path.isdir(saved_images_dir + config['DATA']['RAVImagesDirFormatStr'].format(rav_no + 1) + config['DATA']['CameraImagesDirFormatStr'].format(camera_no+1)):
				print('Directory {} does not exist, creating in default location'.format(saved_images_dir + config['DATA']['RAVImagesDirFormatStr'].format(rav_no + 1) + config['DATA']['CameraImagesDirFormatStr'].format(camera_no+1)))
				os.makedirs(saved_images_dir + config['DATA']['RAVImagesDirFormatStr'].format(rav_no + 1) + config['DATA']['CameraImagesDirFormatStr'].format(camera_no+1))

	for rav_no in range(int(no_ravs)):
		
		#set default directories if not provided. Assume that directory layout is that specified in IJCAIDemoCode		
		#[15:] due to lat, long, alt header
		assert ''.join(open(RAVGPSRoutesDir+"/Agent{}.csv".format(rav_no+1)).readlines()[1:]) == open(RAVGPSRoutesDir+"/Agent{}.csv".format(rav_no+1)).read()[15:]
		#drone_number, gps_coords, gps_coords_file_dir, saved_images_dir, no_cameras = 1, rav_velocity = 5, rav_altitude = 35, sleep_time = 0.5, images: #bool = True, gps_locations: bool=True
		#skip the header
		python_code = generate_route_text(rav_no+1, ''.join(open(RAVGPSRoutesDir+"/Agent{}.csv".format(rav_no+1)).readlines()[1:]), RAV_recorded_GPS_waypoints,saved_images_dir, config['DATA']['RAVImagesDirFormatStr'], config['DATA']['CameraImagesDirFormatStr'],config['DATA']['ImagesFileFormatStr'],no_cameras, rav_velocity = rav_velocity, rav_altitude=rav_altitude, sleep_time=2, images=True, gps_locations=True)
		
		#python_code = generate_route_text(rav_no+1, open(RAVGPSRoutesDir+"/Agent{}.csv".format(rav_no+1)).read()[15:], RAV_recorded_GPS_waypoints, saved_images_dir, no_cameras, #rav_velocity, rav_altitude, images=True, sleep_time = 2, gps_locations=True)
		#assume that directory layout is that specified in IJCAIDemoCode
		rav_no_dict={1:'zero', 2:'one', 3: 'two', 4: 'three'}
		save_python_to_file(python_code, RAV_route_execution_dir + "/rav_{}_mapper.py".format(rav_no_dict[rav_no+1]))


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Automatically write the python files necessary to send the specified number of RAVs on routes given by a file containing GPS coordinates')
	#metavar is a name for the argument in usage messages.
	#nargs -The number of command-line arguments that should be consumed.
	parser.add_argument("no_ravs", type = int, metavar = "no_ravs", help = "Number of RAVS to use in the simulation")

	parser.add_argument("no_cameras", type = int, metavar = "no_cameras", nargs='?', default = 1, help = "Number of cameras to record images from in the simulation")

	parser.add_argument("rav_velocity", type = float, metavar = "rav_velocity", nargs='?', default = 5, help = "Velocticy at which RAVs will operate for simulation")

	parser.add_argument("rav_altitude", type = float, metavar = "rav_altitude", nargs='?', default = 35, help = "Altitude at which RAVs will operate for simulation")
	
	parser.add_argument("RAV_route_execution_dir", type = str, nargs='?', default = "", metavar = "RAV_route_execution_dir", help = "The directory in which to write the python routing files.")

	parser.add_argument("saved_images_dir", type = str, nargs='?', default = "",metavar = "saved_images_dir", help = "The directory in which to save the recorded images.")

	parser.add_argument("RAV_recorded_GPS_waypoints", type = str, nargs='?', default = "",metavar = "RAV_recorded_GPS_waypoints", help = "The directory in which to save the RAV gps routes.")



	
	args = parser.parse_args()
	print("args: ", vars(args))
	main(**vars(args))


