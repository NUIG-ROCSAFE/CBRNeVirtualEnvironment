import os
import sys



def get_imports():
	return '''
import io
import time
import os
import sys
#append folder level up to import AirSimClient
sys.path.append('..')

from PIL import Image
from AirSimClient import *
'''

def get_recorded_GPS_coords_file(RAVRecordedGPSWaypointsDir,RAVRecordedGPSWaypointsFileFormatStr, drone_number):
	return ''.join([RAVRecordedGPSWaypointsDir,RAVRecordedGPSWaypointsFileFormatStr.format(drone_number)])
	#return '{gps_coords_file_dir}/AirSimGPSCoords{drone_number}.txt'
		
def open_gps_coords_code(file_handle_name, gps_coords_file_loc):
	'''Returns code which opens a file handle assigned to file_handle_name'''
	return '''
{file_handle_name} = open({gps_coords_file_loc}, 'w')'''.format(file_handle_name=file_handle_name, gps_coords_file_loc=gps_coords_file_loc)

	
def get_connect_and_arm_code(port, rav_number):
	'''returns airsim api code to create a new client and connect it to the simulator'''
	
	create_client = '''
port = {port}
print('Creating new client on port: ',{port})
# connect to the AirSim simulator
client = MultirotorClient(port={port})'''.format(port=(41451 + rav_number - 1))

	connect_client = '''
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)
print('Taking off...')
client.takeoff()
print('Moving clear of tree line')
client.moveToPosition(client.getPosition().x_val, client.getPosition().y_val, client.getPosition().z_val-25, 6)
print('Client position: {}'.format(client.getPosition()))\n'''
	
	return create_client + connect_client
	
def get_land_and_disarm_code():
	return "client.land()\n" + "client.armDisarm(False)\n"

def get_move_to_gps_position_string(lat, long, altitude,velocity, sleep_time):
	'''returns a string which can be formatted to send RAV to gps coordinate'''
	return "\nclient.moveToGPSPosition(GPSCoordinate({lat}, {long}, {altitude}), {velocity})\ntime.sleep({sleep_time})\n".format(lat = lat, long = long, altitude = altitude,velocity=velocity, sleep_time=sleep_time)
	
def generate_image_requests_code(no_cameras):
	'''Generates code to request images from AirSim api'''
	image_requests_wrapper = '''\nresponses = client.simGetImages([{}])'''
	camera_mapping = {1:3, 2:2, 3:1}
	camera_mapping_extra = {i:i for i in range(4,20)}
	camera_mapping = {**camera_mapping, **camera_mapping_extra}
	image_requests = ', '.join("ImageRequest({}, AirSimImageType.Scene)".format(camera_mapping[i]) for i in range(1, no_cameras+1))
	return image_requests_wrapper.format(image_requests)
	
	

def generate_save_images_loc(saved_images_dir, rav_images_dir, drone_number, camera_images_dir, file_name):
	return ''.join([saved_images_dir, rav_images_dir + str(drone_number), camera_images_dir, file_name])
	#return "{saved_images_dir}"+"{rav_images_dir}" + "{camera_images_dir}"+ "{file_name}"
	
	
def generate_save_images_code(saved_images_dir, rav_images_dir, drone_number, camera_images_dir, file_name):
	return '''
for camera_number, image in enumerate(responses):
	AirSimClientBase.write_file("{}", image.image_data_uint8)'''.format(generate_save_images_loc(saved_images_dir, rav_images_dir, drone_number, camera_images_dir, file_name))
	
	#.format(saved_images_dir=saved_images_dir, rav_images_dir = rav_images_dir.format(drone_number), camera_images_dir = camera_images_dir, drone_number=drone_number, #file_name=image_file_format_str.format(waypoint_number))

def generate_record_gps_loc_code(lat, long, file_handle_name):
	return "{file_handle_name}.write('str({lat}), str({long}\n'))\n".format(lat=lat, long=long, file_handle_name=file_handle_name) + "{file_handle_name}.flush()\n".format(file_handle_name=file_handle_name)
			
def generate_close_file_code(file_handle_name):
	return "{file_handle_name}.close()".format(file_handle_name=file_handle_name)
	
def generate_route_text(drone_number, gps_coordinates_text, RAV_recorded_GPS_waypoints_dir, RAV_recorded_GPS_waypoints_file_format_str, RAV_recorded_GPS_waypoints_relative_dir, saved_images_dir, rav_images_dir, camera_images_dir, image_file_format_str, no_cameras = 1, rav_velocity = 5, rav_altitude = 35, sleep_time = 0.5, images: bool = True, gps_locations: bool=True):
#def generate_route_text(drone_number, RAV_recorded_GPS_waypoints_file_format, RAV_recorded_GPS_waypoints_relative_file_format, saved_images_dir, rav_images_dir, #camera_images_dir, image_file_format_str, no_cameras = 1, rav_velocity = 5, rav_altitude = 35, sleep_time = 0.5, images: bool = True, gps_locations: bool=True):
	'''Given a drone number, list of gps coordinates, writes a file to /PythonGridMapping/AirSimPythonClient/rav_{}_mapper.py which contains 
	the AirSim api commands which send the RAV to the generated GPS coordinates to gather image data'''
	#if the user wants one camera, let that be camera 3 (downward facing). 

	RAVRecordedGPSWaypointsFileHandle = "RAVRecordedGPSWaypointsFile"
	RAVRelativeRecordedGPSWaypointsFileHandle = "RAVRelativeRecordedGPSWaypointsFile"
	
	#append on imports
	return_txt = get_imports()

	#open file to record visited gps locations
	return_txt += open_gps_coords_code(RAVRecordedGPSWaypointsFileHandle, get_recorded_GPS_coords_file(RAV_recorded_GPS_waypoints_dir, RAV_recorded_GPS_waypoints_file_format_str, drone_number))
	#open file to record visited gps locations relative to user-chosen home position
	return_txt += open_gps_coords_code(RAVRelativeRecordedGPSWaypointsFileHandle, get_recorded_GPS_coords_file(RAV_recorded_GPS_waypoints_relative_dir, RAV_recorded_GPS_waypoints_file_format_str, drone_number))
	
	return_txt += get_connect_and_arm_code((41451 + drone_number - 1), drone_number)
	return_txt = return_txt.replace('\t','')
		
	#get rav to visit each gps coordinate
	#new image request for each visited gps coordinate
	for waypoint_number, line in enumerate(gps_coordinates_text.split('\n')):
		#ignore blank lines
		if line == '':
			continue
		else:
			try:
				lat = line.split(',')[0]
				long = line.split(',')[1]
			except Exception as e:
				print('couldnt read lat, long from file, skipping')
				continue
		#set velocity high for first coordinate
		if waypoint_number == 0:
		#full steam ahead to first location
			return_txt += get_move_to_gps_position_string(lat, long, rav_altitude, 7, sleep_time)
		else:
			return_txt += get_move_to_gps_position_string(lat, long, rav_altitude, rav_velocity, sleep_time)
		
		if images and no_cameras > 0:
			return_txt += generate_image_requests_code(no_cameras)
			
			return_txt += generate_save_images_code(saved_images_dir, rav_images_dir.format(drone_number), drone_number, camera_images_dir, image_file_format_str.format(waypoint_number))
			
			
			#pull this into separate function
			#return_txt += '''
#print('Writing files to ', "{saved_images_dir}"+"{rav_images_dir}" + "{camera_images_dir}"+ #"{file_name}")'''.format(saved_images_dir=saved_images_dir, rav_images_dir = rav_images_dir.format(drone_number), camera_images_dir = camera_images_dir.format("examplecamera"), file_name = image_file_format_str.format('0'))

#			return_txt+= '''
#for camera_number, image in enumerate(responses):
#	AirSimClientBase.write_file("{saved_images_dir}"+"{rav_images_dir}" + "{camera_images_dir}".format(camera_number+1)+ "{file_name}", image.image_data_uint8)
#'''.format(saved_images_dir=saved_images_dir, rav_images_dir = rav_images_dir.format(drone_number), camera_images_dir = camera_images_dir,drone_number=drone_number,file_name=image_file_format_str.format(line_index))

				
		#write gps locations
		if gps_locations:
			return_txt += generate_record_gps_loc_code("client.getGpsLocation().latitude", "client.getGpsLocation().longitude", RAVRecordedGPSWaypointsFileHandle)
			return_txt += generate_record_gps_loc_code("client.getGPSLocationRelative().lat", "client.getGPSLocationRelative().long", RAVRelativeRecordedGPSWaypointsFileHandle)
			
			#return_txt += "gpsCoordsFile.write('{}, {}\n')\n".format(line.split(',')[0], line.split(',')[1])
			#return_txt += "gpsCoordsFile.flush()\n"
			#return_txt += "AirSimgpsCoordsFile.write(str({})+', '+str({}) + '\n')\n".format("client.getGpsLocation().latitude", "client.getGpsLocation().longitude")
			#return_txt += "AirSimgpsCoordsFile.flush()\n"
			#return_txt += "AirSimgpsRelativeCoordsFile.write(str({})+', '+ str({})+'\n')\n".format("client.getGPSLocationRelative().lat", "client.getGPSLocationRelative().long")
			#return_txt += "AirSimgpsRelativeCoordsFile.flush()\n"
			#return_txt += "print('NUIG relative GPS location: ', client.getGPSLocationRelative())\n"
			
	#send the rav to its home position and then land it
	return_txt += get_move_to_gps_position_string("client.GPS_to_unreal.home_position_GPS.lat", "client.GPS_to_unreal.home_position_GPS.long", rav_altitude, rav_velocity, sleep_time)
	#land and disarm
	return_txt += get_land_and_disarm_code()
	
	generate_close_file_code(RAVRecordedGPSWaypointsFileHandle)
	generate_close_file_code(RAVRelativeRecordedGPSWaypointsFileHandle)
	
	return return_txt	
	
def save_python_to_file(python_code, file_loc):
	'''Saves python_code to file_loc. Python code should contain the code necessary to send virtual RAVs to collect images at specified GPS coordinates'''
	#print file location for debugging
	print("writing to file: ", file_loc)
	file = open(file_loc, 'w')
	file.write(python_code)
	file.close()	
