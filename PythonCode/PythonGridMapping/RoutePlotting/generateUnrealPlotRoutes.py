import argparse
import sys
import os
from RAVRouteWritingUtils import generate_route_text, save_python_to_file, get_txt


def main(no_ravs, no_cameras = 1, rav_velocity = 4, rav_altitude = 35, rav_route_write_dir = "", gps_coords_write_dir="", saved_images_dir=""):
	
	print("generating routes for ", no_ravs, " ravs")
	rav_locs = "../../../RCode/ShinyApp/Data/"
	#rav_0_locs = open("../RCode/ShinyApp/Data/Agent1.csv").read()[15:]
	#print("rav_0_locs: ", rav_0_locs)
	#rav_1_locs = open("../RCode/ShinyApp/Data/Agent2.csv").read()[15:]
	#rav_2_locs = open("../RCode/ShinyApp/Data/Agent3.csv").read()[15:]
	#rav_locs = [rav_0_locs, rav_1_locs, rav_2_locs]
	
	base_dir = os.getcwd().split('IJCAIDemoCodeAll')[0]+'IJCAIDemoCodeAll'
	
	if saved_images_dir == "":
			saved_images_dir = base_dir + "\\PythonCode\\PythonClientGPSMapping\\GPSMappings\\Images"
	if not os.path.isdir(saved_images_dir):
			#exit program and ask for valid path
			pass
	if gps_coords_write_dir == "":
		gps_coords_write_dir = base_dir + "\\PythonCode\\PythonClientGPSMapping\\GPSMappings\\GPSCoords"
		
	if rav_route_write_dir == "":
		rav_route_write_dir = base_dir + "\\PythonCode\\PythonGridMapping\\AirSimPythonClient"
		
	if not os.path.isdir(saved_images_dir):
		#exit program and ask for valid path
		pass	
	
	if not os.path.isdir(gps_coords_write_dir):
		#exit program and ask for valid path
		pass
		
	for rav_no in range(int(no_ravs)):
		#set default directories if not provided. Assume that directory layout is that specified in IJCAIDemoCode			
		python_code = generate_route_text(rav_no+1, open(rav_locs+"Agent{}.csv".format(rav_no+1)).read()[15:], gps_coords_write_dir, saved_images_dir, no_cameras, rav_velocity=rav_velocity, rav_altitude = rav_altitude, images=True, sleep_time = 2, gps_locations=True)
		#assume that directory layout is that specified in IJCAIDemoCode
		rav_no_dict={1:'zero', 2:'one', 3: 'two', 4: 'three'}
		save_python_to_file(python_code, rav_route_write_dir + "\\rav_{}_mapper.py".format(rav_no_dict[rav_no+1]))


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Automatically write the python files necessary to send the specified number of RAVs on routes given by a file containing GPS coordinates')
	#metavar is a name for the argument in usage messages.
	#nargs -The number of command-line arguments that should be consumed.
	parser.add_argument("no_ravs", type = int, metavar = "no_ravs", help = "Number of RAVS to use in the simulation")

	parser.add_argument("no_cameras", type = int, metavar = "no_cameras", nargs='?', default = 1, help = "Number of cameras to record images from in the simulation")

	parser.add_argument("rav_velocity", type = float, metavar = "rav_velocity", nargs='?', default = 5, help = "Velocticy at which RAVs will operate for simulation")

	parser.add_argument("rav_altitude", type = float, metavar = "rav_altitude", nargs='?', default = 35, help = "Altitude at which RAVs will operate for simulation")
	
	parser.add_argument("rav_route_write_dir", type = str, nargs='?', default = "", metavar = "rav_route_write_dir", help = "The directory in which to write the python routing files.")

	parser.add_argument("saved_images_dir", type = str, nargs='?', default = "",metavar = "saved_images_dir", help = "The directory in which to save the recorded images.")

	parser.add_argument("gps_coords_write_dir", type = str, nargs='?', default = "",metavar = "gps_coords_write_dir", help = "The directory in which to save the RAV gps routes.")



	
	args = parser.parse_args()
	print("args: ", vars(args))
	main(**vars(args))


