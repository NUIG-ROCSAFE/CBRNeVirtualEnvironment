import argparse
import sys
import os
import configparser
from generateRoutesForUnrealUtils import generate_route_text, save_python_to_file, get_txt

def get_config() -> configparser.ConfigParser:
	config = configparser.ConfigParser()
	#read the global default config
	config.read(os.getcwd().replace("\\", "/") + '/../../../Config/config.ini')
	return config


def main(no_ravs, no_cameras = 1, rav_velocity = 4, rav_altitude = 35, RAV_route_execution_dir = "", RAV_recorded_GPS_waypoints="", saved_images_dir=""):
	config = get_config()
	print('config: ', config.sections())
	print("Generating routes for ", no_ravs, " ravs")
	base_dir = os.path.abspath(__file__).split('PythonCode')[0].replace('\\', '/')
	#READ DEFAULTS
	RAVGPSRoutesDir = base_dir + config["DATA"]["RAVGPSRoutesDir"]
	if saved_images_dir == "":
			#saved_images_dir = base_dir + "/PythonCode/PythonClientGPSMapping/GPSMappings/Images"
			saved_images_dir = base_dir + config["DATA"]["CollectedPNGImagesDir"]
			
	if not os.path.isdir(saved_images_dir):
			#exit program and ask for valid path
			print('Directory {} does not exist, creating'.format(saved_images_dir))
			os.makedirs(saved_images_dir)
			
	if RAV_recorded_GPS_waypoints == "":
		RAV_recorded_GPS_waypoints = base_dir + config["DATA"]["RAVRecordedGPSWaypoints"]
		#RAV_recorded_GPS_waypoints = base_dir + "/PythonCode/PythonClientGPSMapping/GPSMappings/GPSCoords"
		
	if RAV_route_execution_dir == "":
		RAV_route_execution_dir = base_dir + config['PYTHON']['PythonRAVRouteExecutionDir']
		#RAV_route_execution_dir = base_dir + "/PythonCode/PythonGridMapping/AirSimPythonClient"
		
	
	if not os.path.isdir(RAV_recorded_GPS_waypoints):
		print('Directory {} does not exist, creating in default location'.format(saved_images_dir))
		os.makedirs(RAV_recorded_GPS_waypoints)

	if not os.path.exists(RAV_recorded_GPS_waypoints):
		print('Directory {} does not exist, creating in default location'.format(RAV_recorded_GPS_waypoints))
		os.makedirs(RAV_recorded_GPS_waypoints)

	for rav_no in range(int(no_ravs)):
		if not os.path.exists(saved_images_dir + 'ImagesRAV%d/' % (rav_no + 1)):
			os.makedirs(saved_images_dir + '/ImagesRAV%d/' % (rav_no + 1))
		#set default directories if not provided. Assume that directory layout is that specified in IJCAIDemoCode			
		python_code = generate_route_text(rav_no+1, open(RAVGPSRoutesDir+"Agent{}.csv".format(rav_no+1)).read()[15:], RAV_recorded_GPS_waypoints, saved_images_dir, no_cameras, rav_velocity=rav_velocity, rav_altitude = rav_altitude, images=True, sleep_time = 2, gps_locations=True)
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

