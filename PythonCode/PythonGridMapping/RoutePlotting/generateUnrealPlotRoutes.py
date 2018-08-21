import os
import sys

def generate_route(drone_number, gps_coords, RAV_velocity = 5, RAV_altitude = 35, sleep_time = 0.5, images: bool = True, gps_locations: bool=True):
	return_txt = '''import io
	import time
	import os
	from PIL import Image
	from AirSimClient import *
	os.chdir('..\\..')
	print('Working from directory: ', os.getcwd())
	'''
	return_txt += '''gpsCoordsFile = open(os.getcwd() + '\\PythonClientGPSMapping\\GPSMappings\\GPSCoords\\GPSCoords{drone_number}.txt', 'w')
	AirSimgpsCoordsFile = open(os.getcwd() + '\\PythonClientGPSMapping\\GPSMappings\\GPSCoords\\AirSimGPSCoords{drone_number}.txt', 'w')
	AirSimgpsRelativeCoordsFile = open(os.getcwd() + '\\PythonClientGPSMapping\\GPSMappings\\GPSCoords\\AirSimRelativeGPSCoords{drone_number}.txt', 'w')
	'''.format(drone_number=drone_number)

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
	return_txt = return_txt.replace('\t','').replace('i = input("Press \'m\' to begin mapping")', '\ti = input("Press \'m\' to begin mapping")')
	
	format_txt = "\nclient.moveToGPSPosition(GPSCoordinate({{}}, {{}}, {altitude}), {velocity})\ntime.sleep({sleep_time})\n".format(altitude = RAV_altitude,velocity=RAV_velocity, sleep_time=sleep_time)

	for line_index, line in enumerate(gps_coords.split('\n')):
		if line == '':
			continue
		if line_index == 0:
		#full steam ahead to first location
			return_txt+=("client.moveToGPSPosition(GPSCoordinate({}, {}, {altitude}), 7)\ntime.sleep(1)\n".format(line.split(',')[0], line.split(',')[1], altitude = RAV_altitude))
		else:
			return_txt+=(format_txt.format(line.split(',')[0], line.split(',')[1], altitude = RAV_altitude))
		
		if images:
			return_txt += '''
responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])'''
#	return_txt += '''
#responses = client.simGetImages([
#	ImageRequest(1, AirSimImageType.Scene),
#	ImageRequest(2, AirSimImageType.Scene),
#	ImageRequest(3, AirSimImageType.Scene),
#	ImageRequest(4, AirSimImageType.Scene)])'''
			return_txt += '''
print('Writing files to ', os.getcwd() + "\\PythonClientGPSMapping\\GPSMappings\\Images\\Images{drone_number}\\Camera{{}}\\image_{line_index}.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\\PythonClientGPSMapping\\GPSMappings\\Images\\Images{drone_number}\\Camera{{}}\\image_{line_index}.png".format(image_index+1) , image.image_data_uint8)
'''.format(drone_number=drone_number,line_index=line_index)
				
				
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

	drone_numbers={1:'zero', 2:'one', 3: 'two', 4: 'three'}
	print("writing to directory: ", os.getcwd())
	file_loc = os.getcwd() + '\\PythonGridMapping\\AirSimPythonClient\\rav_{}_mapper.py'.format(drone_numbers[drone_number])
	print("writing to file: ", file_loc)
	file = open(file_loc, 'w')
	print('writing missions for drone: {}'.format(drone_number))
	#print(return_txt)

	file.write(return_txt)
	file.close()	

os.chdir('../..')
print('current directory: ', os.getcwd())
#drone_code = open(os.getcwd() + '\\PythonClientGPSMapping\\RAVRoutes\\test_work_resolver31.txt', 'r')
#drone_code = open("D:\\IJCAIDemoCode\\CommsHubCode\\work_resolver_runner.txt", 'r')


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
	
def main():
	no_ravs = sys.argv[1]
	print("generating routes for ", no_ravs, " ravs")
	rav_0_locs = open("../RCode/ShinyApp/Data/Agent1.csv").read()[15:]
	print("rav_0_locs: ", rav_0_locs)
	rav_1_locs = open("../RCode/ShinyApp/Data/Agent2.csv").read()[15:]
	rav_2_locs = open("../RCode/ShinyApp/Data/Agent3.csv").read()[15:]
	rav_locs = [rav_0_locs, rav_1_locs, rav_2_locs]
	for i in range(int(no_ravs)):
		generate_route(i+1, rav_locs[i], RAV_velocity=5, RAV_altitude = 35, images=True, sleep_time = 2, gps_locations=True)


if __name__ == '__main__':
	main()
#generate_route(1, get_txt(), RAV_velocity=5, RAV_altitude = 35, images=True, sleep_time = 2, gps_locations=True)
#generate_route(1, rav_0_locs, RAV_velocity=5, RAV_altitude = 35, images=True, sleep_time = 2, gps_locations=True)

#generate_route(2, get_txt(), RAV_velocity=5, RAV_altitude = 35, images=True, sleep_time = 2, gps_locations = True)

#generate_route(2, rav_1_locs, RAV_velocity=5, RAV_altitude = 35, images=True, sleep_time = 2, gps_locations = True)

#generate_route(3, rav_2_locs, RAV_velocity=5, RAV_altitude = 35, images=True, sleep_time = 2, gps_locations = True)

