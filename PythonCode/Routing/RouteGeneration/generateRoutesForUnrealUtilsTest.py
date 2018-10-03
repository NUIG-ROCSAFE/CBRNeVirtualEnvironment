import unittest
import sys
sys.path.append('..')

from generateRoutesForUnrealUtils import (generate_close_file_code, generate_image_requests_code, generate_record_gps_loc_code, generate_route_text, generate_save_images_code, generate_save_images_loc, get_connect_and_arm_code, get_imports, get_land_and_disarm_code, get_move_to_gps_position_string, get_recorded_GPS_coords_file, open_gps_coords_code, save_python_to_file)


#some very basic tests, hard-coded some parts
class generateRoutesForUnrealUtilsTest(unittest.TestCase):
	
	def test_generate_save_images_code(self):

		saved_images_dir = "C:/Images"
		rav_images_dir = "/RAVImages"
		drone_number = 1
		camera_images_dir = "/Camera1"
		file_name = "/image1.png"
		

		#expected_code = "responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])"
		expected_code = '''
for camera_number, image in enumerate(responses):
	AirSimClientBase.write_file("{}", image.image_data_uint8)'''.format(saved_images_dir + rav_images_dir + str(drone_number) + camera_images_dir + file_name)
	
		actual_code = generate_save_images_code(saved_images_dir, rav_images_dir, drone_number, camera_images_dir, file_name)
		self.assertEqual(expected_code, actual_code)
		
	def test_generate_image_requests_code(self):
		expected_code = '''\nresponses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])'''
		actual_code = generate_image_requests_code(2)
		self.assertEqual(actual_code, expected_code)
		
	def test_get_move_to_gps_position_string(self):
		lat, long, altitude = 23.12, -35.87, 50
		velocity, sleep_time = 7, 0.5
		#this shouldn't be hard-coded..
		expected_code = "\nclient.moveToGPSPosition(GPSCoordinate(23.12, -35.87, 50), 7)\ntime.sleep(0.5)\n"
		actual_code = get_move_to_gps_position_string(lat, long, altitude, velocity, sleep_time)
		self.assertEqual(actual_code, expected_code)
	
	def test_open_gps_coords_code(self):
		expected_code = '''
RAVRecordedGPSWaypointsFileHandle = open('D:/Test/Test1.txt', 'w')'''

		actual_code = open_gps_coords_code("RAVRecordedGPSWaypointsFileHandle","'D:/Test/Test1.txt'")
		self.assertEqual(expected_code, actual_code)
		
	def test_generate_record_gps_loc_code(self):
		expected_code = '''
RAVRecordedGPSWaypointsFileHandle.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')'''

		actual_code = generate_record_gps_loc_code("client.getGpsLocation().latitude", "client.getGpsLocation().longitude", "RAVRecordedGPSWaypointsFileHandle")
		
		
	def test_generate_route_text(self):
		drone_number = 1
		RAV_recorded_GPS_waypoints_dir = "/RAVCollectedData/GPSCoords/RecordedGPSCoords"
		RAV_recorded_GPS_waypoints_file_format_str = "/RecordedGPSCoordsAgent{}.txt"
		RAV_recorded_GPS_waypoints_relative_dir = "/RAVCollectedData/GPSCoords/RecordedGPSCoordsRelative"
		saved_images_dir = "/RAVCollectedData/PNGImages"
		rav_images_dir = "/ImagesRAV{}"
		camera_images_dir = "/Camera{}"
		image_file_format_str = "/image_{}.png"
		no_cameras = 1
		rav_velocity = 5
		rav_altitude = 35
		sleep_time = 0.5
		images = True
		gps_locations=True
		lat1, long1, alt1 = 12, 23, 50
		vel = 5
		
		expected_code = '''
import io
import time
import os
import sys
#append folder level up to import AirSimClient
sys.path.append('..')

from PIL import Image
from AirSimClient import *
'''+'''
RAVRecordedGPSWaypointsFileHandle = open('/RAVCollectedData/GPSCoords/RecordedGPSCoords/RecordedGPSCoordsAgent1.txt', 'w')
RAVRelativeRecordedGPSWaypointsFileHandle = open('/RAVCollectedData/GPSCoords/RecordedGPSCoordsRelative/RecordedGPSCoordsAgent1.txt', 'w')
'''+'''
port = 41451
print('Creating new client on port: ',41451)
# connect to the AirSim simulator
client = MultirotorClient(port=41451)
''' + '''
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)
print('Taking off...')
client.takeoff()
print('Moving clear of tree line')
client.moveToPosition(client.getPosition().x_val, client.getPosition().y_val, client.getPosition().z_val-25, 6)
print('Client position: {}'.format(client.getPosition()))\n
''' + '''
client.moveToGPSPosition(GPSCoordinate({}, {}, {}), {})
'''.format(lat1, long1, alt1, rav_velocity) + '''
time.sleep(1)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])''' + '''
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("/RAVCollectedData/PNGImages/ImagesRAV1/Camera1/image_1.png", image.image_data_uint8)
RAVRecordedGPSWaypointsFileHandle.write('{}, {}\n')
RAVRecordedGPSWaypointsFileHandle.flush()
RAVRelativeRecordedGPSWaypointsFileHandle.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
RAVRelativeRecordedGPSWaypointsFileHandle.flush()
'''.format(lat1, long1) + '''
RAVRecordedGPSWaypointsFileHandle.close()
RAVRelativeRecordedGPSWaypointsFileHandle.close()
client.land()
client.armDisarm(False)
'''
		expected_code = expected_code.replace('\n\n', '\n')
		actual_code = generate_route_text(drone_number,'''
lat, long, alt
12, 23, 20''',RAV_recorded_GPS_waypoints_dir, RAV_recorded_GPS_waypoints_file_format_str, RAV_recorded_GPS_waypoints_relative_dir, saved_images_dir, rav_images_dir, camera_images_dir, image_file_format_str, no_cameras = 1, rav_velocity = 5, rav_altitude = 35, sleep_time = 0.5, images= True, gps_locations=True).replace('\n\n','\n')
		print('expected_code', expected_code)
		print('actual_code', actual_code)
		self.assertEqual(expected_code, actual_code)

		
if __name__ == '__main__':
	unittest.main()