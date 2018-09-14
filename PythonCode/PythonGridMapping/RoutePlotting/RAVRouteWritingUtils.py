import os
import sys

def generate_route_text(drone_number, gps_coords, gps_coords_file_dir, saved_images_dir, no_cameras = 1, rav_velocity = 5, rav_altitude = 35, sleep_time = 0.5, images: bool = True, gps_locations: bool=True):
	'''Given a drone number, list of gps coordinates, writes a file to \\PythonGridMapping\\AirSimPythonClient\\rav_{}_mapper.py which contains 
	the AirSim api commands which send the RAV to the generated GPS coordinates to gather image data'''
	#if the user wants one camera, let that be camera 3 (downward facing). 
	camera_mapping = {1:3, 2:2, 3:1, 4:4}
	
	return_txt = '''import io
	import time
	import os
	from PIL import Image
	from AirSimClient import *
	'''
	
	#return_txt += '''gpsCoordsFile = open({gps_coords_file_dir}\\GPSCoords{drone_number}.txt', 'w')
	#AirSimgpsCoordsFile = open(os.getcwd() + '\\PythonClientGPSMapping\\GPSMappings\\GPSCoords\\AirSimGPSCoords{drone_number}.txt', 'w')
	#AirSimgpsRelativeCoordsFile = open(os.getcwd() + '\\PythonClientGPSMapping\\GPSMappings\\GPSCoords\\AirSimRelativeGPSCoords{drone_number}.txt', 'w')
	#'''.format(gps_coords_file_dir = gps_coords_file_dir, drone_number=drone_number)

	return_txt += '''gpsCoordsFile = open('{gps_coords_file_dir}\\GPSCoords{drone_number}.txt', 'w')
	AirSimgpsCoordsFile = open('{gps_coords_file_dir}\\AirSimGPSCoords{drone_number}.txt', 'w')
	AirSimgpsRelativeCoordsFile = open('{gps_coords_file_dir}\\AirSimRelativeGPSCoords{drone_number}.txt', 'w')
	'''.format(gps_coords_file_dir = gps_coords_file_dir, drone_number=drone_number)
	
	return_txt += '''port = {port}
	print('Creating new client on port: ',{port})
	# connect to the AirSim simulator
	client = MultirotorClient(port={port})
	'''.format(port=(41451 + drone_number - 1))
	
	return_txt +='''print('Confirming connection...')
	client.confirmConnection()

	client.enableApiControl(True)
	client.armDisarm(True)

	state = client.getGpsLocation()
	print("state: %s" % state)

	print('Taking off...')
	client.takeoff()

	#wait before taking off
	time.sleep(0.5)
	print('Moving clear of tree line')
	client.moveToPosition(client.getPosition().x_val, client.getPosition().y_val, client.getPosition().z_val-25, 6)
	print('Client position: {}'.format(client.getPosition()))\n'''
	return_txt = return_txt.replace('\t','')
	
	format_txt = "\nclient.moveToGPSPosition(GPSCoordinate({{}}, {{}}, {altitude}), {velocity})\ntime.sleep({sleep_time})\n".format(altitude = rav_altitude,velocity=rav_velocity, sleep_time=sleep_time)
	#new gps coordinate on each line
	for line_index, line in enumerate(gps_coords.split('\n')):
		if line == '':
			continue
		if line_index == 0:
		#full steam ahead to first location
			return_txt+=("client.moveToGPSPosition(GPSCoordinate({}, {}, {altitude}), 7)\ntime.sleep(1)\n".format(line.split(',')[0], line.split(',')[1], altitude = rav_altitude))
		else:
			return_txt+=(format_txt.format(line.split(',')[0], line.split(',')[1], altitude = rav_altitude))
		
		if images and no_cameras > 0:
			image_requests_wrapper = '''
responses = client.simGetImages([{}])'''
			image_requests = ', '.join("ImageRequest({}, AirSimImageType.Scene)".format(camera_mapping[i]) for i in range(1, no_cameras+1))
			return_txt += image_requests_wrapper.format(image_requests)

#			return_txt += '''
#print('Writing files to ', os.getcwd() + "\\PythonClientGPSMapping\\GPSMappings\\Images\\Images{drone_number}\\Camera{{}}\\image_{line_index}.png".format('example'))
#for image_index, image in enumerate(responses):
#	AirSimClientBase.write_file(os.getcwd() + "\\PythonClientGPSMapping\\GPSMappings\\Images\\Images{drone_number}\\Camera{{}}\\image_{line_index}.png".format(image_index+1) , #image.image_data_uint8)
#'''.format(drone_number=drone_number,line_index=line_index)
			if line_index == 0:
				return_txt += '''
print('Writing files to ', "{saved_images_dir}" + "\\Images{drone_number}\\Camera{{}}\\image_{line_index}.png".format('example'))
for image_index, image in enumerate(responses):
	if not os.path.exists("{saved_images_dir}" + "\\Images{drone_number}\\Camera{{}}".format(image_index+1)):
		os.makedirs("{saved_images_dir}" + "\\Images{drone_number}\\Camera{{}}".format(image_index+1))
	AirSimClientBase.write_file("{saved_images_dir}"+"\\Images{drone_number}\\Camera{{}}\\image_{line_index}.png".format(image_index+1) , image.image_data_uint8)
'''.format(saved_images_dir=saved_images_dir, drone_number=drone_number,line_index=line_index)

			else:
				return_txt += '''
print('Writing files to ', "{saved_images_dir}"+"\\Images{drone_number}\\Camera{{}}\\image_{line_index}.png".format('example', saved_images_dir = '{saved_images_dir}'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("{saved_images_dir}"+"\\Images{drone_number}\\Camera{{}}\\image_{line_index}.png".format(image_index+1) , image.image_data_uint8)
'''.format(saved_images_dir=saved_images_dir, drone_number=drone_number,line_index=line_index)
				
				
			#return_txt += "png_image = client.simGetImage(4, AirSimImageType.Scene)\n"
			#return_txt += "Image.open(io.BytesIO(png_image)).save('D:/IJCAIDemoCode/PythonClientGPSMapping/GPSMappings/Images/Images{}/Camera4/image_{}.png')\n".format(drone_number, line_index)
			#return_txt += "png_image = client.simGetImage(3, AirSimImageType.Scene)\n"
			#return_txt += "Image.open(io.BytesIO(png_image)).save('D:/IJCAIDemoCode/PythonClientGPSMapping/GPSMappings/Images/Images{}/Camera3/image_{}.png')\n".format(drone_number, line_index)
			#return_txt += "png_image = client.simGetImage(2, AirSimImageType.Scene)\n"
			#return_txt += "Image.open(io.BytesIO(png_image)).save('D:/IJCAIDemoCode/PythonClientGPSMapping/GPSMappings/Images/Images{}/Camera2/image_{}.png')\n".format(drone_number, line_index)
			#return_txt += "png_image = client.simGetImage(1, AirSimImageType.Scene)\n"
			#return_txt += "Image.open(io.BytesIO(png_image)).save('D:/IJCAIDemoCode/PythonClientGPSMapping/GPSMappings/Images/Images{}/Camera1/image_{}.png')\n".format(drone_number, line_index)
			
		if gps_locations:
			return_txt += "gpsCoordsFile.write('{}, {}\\n')\n".format(line.split(',')[0], line.split(',')[1])
			return_txt += "gpsCoordsFile.flush()\n"
			return_txt += "AirSimgpsCoordsFile.write(str({})+', '+str({}) + '\\n')\n".format("client.getGpsLocation().latitude", "client.getGpsLocation().longitude")
			return_txt += "AirSimgpsCoordsFile.flush()\n"
			return_txt += "AirSimgpsRelativeCoordsFile.write(str({})+', '+ str({})+'\\n')\n".format("client.getGPSLocationRelative().lat", "client.getGPSLocationRelative().long")
			return_txt += "AirSimgpsRelativeCoordsFile.flush()\n"
			return_txt += "print('NUIG relative GPS location: ', client.getGPSLocationRelative())\n"
			
	return_txt += "\ngpsCoordsFile.close()\n"
	return_txt += "AirSimgpsCoordsFile.close()\n"
	return_txt += "AirSimgpsRelativeCoordsFile.close()\n"

	return return_txt	
	
def save_python_to_file(python_code, file_loc):
	'''Saves python_code to file_loc. Python code should contain the code necessary to send virtual RAVs to collect images at specified GPS coordinates''' 
	
	#print("writing to directory: ", os.getcwd())
	#file_loc = os.getcwd() + '\\PythonGridMapping\\AirSimPythonClient\\rav_{}_mapper.py'.format(drone_numbers[drone_number])
	print("writing to file: ", file_loc)
	file = open(file_loc, 'w')
	#print('writing missions for drone: {}'.format(drone_number))
	file.write(python_code)
	file.close()	
	
def get_txt():
	txt = ''
	line = ''
	drone_code.readline()
	drone_code.readline()
	while line != '\n':
		line = drone_code.readline()
		txt+=line
	txt = txt[:-2]
	return txt