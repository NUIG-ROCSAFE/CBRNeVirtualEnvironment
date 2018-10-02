import io
import time
import os
import sys
#append folder level up to import AirSimClient
sys.path.append('..')

from PIL import Image
from AirSimClient import *
gpsCoordsFile = open('D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/GPSCoords/GPSCoords1.txt', 'w')
AirSimgpsCoordsFile = open('D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/GPSCoords/AirSimGPSCoords1.txt', 'w')
AirSimgpsRelativeCoordsFile = open('D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/GPSCoords/AirSimRelativeGPSCoords1.txt', 'w')
port = 41451
print('Creating new client on port: ',41451)
# connect to the AirSim simulator
client = MultirotorClient(port=41451)
client.confirmConnection()

client.enableApiControl(True)
client.armDisarm(True)

state = client.getGpsLocation()
print("state: %s" % state)

print('Taking off...')
client.takeoff()
print('Moving clear of tree line')
client.moveToPosition(client.getPosition().x_val, client.getPosition().y_val, client.getPosition().z_val-25, 6)
print('Client position: {}'.format(client.getPosition()))
client.moveToGPSPosition(GPSCoordinate(53.27929999999999921556081972084939479827880859375,  -9.0638000000000005229594535194337368011474609375, 55.0), 7)
time.sleep(1)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_0.png", image.image_data_uint8)
gpsCoordsFile.write('53.27929999999999921556081972084939479827880859375,  -9.0638000000000005229594535194337368011474609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2792737664999996556129190139472484588623046875,  -9.0638355817000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_1.png", image.image_data_uint8)
gpsCoordsFile.write('53.2792737664999996556129190139472484588623046875,  -9.0638355817000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2792737664999996556129190139472484588623046875,  -9.0636149455000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_2.png", image.image_data_uint8)
gpsCoordsFile.write('53.2792737664999996556129190139472484588623046875,  -9.0636149455000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2792737664999996556129190139472484588623046875,  -9.0633943093000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_3.png", image.image_data_uint8)
gpsCoordsFile.write('53.2792737664999996556129190139472484588623046875,  -9.0633943093000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2792737664999996556129190139472484588623046875,  -9.0631736731000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_4.png", image.image_data_uint8)
gpsCoordsFile.write('53.2792737664999996556129190139472484588623046875,  -9.0631736731000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2792737664999996556129190139472484588623046875,  -9.0629530369000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_5.png", image.image_data_uint8)
gpsCoordsFile.write('53.2792737664999996556129190139472484588623046875,  -9.0629530369000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2792737664999996556129190139472484588623046875,  -9.0627324007000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_6.png", image.image_data_uint8)
gpsCoordsFile.write('53.2792737664999996556129190139472484588623046875,  -9.0627324007000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2792737664999996556129190139472484588623046875,  -9.0625117645000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_7.png", image.image_data_uint8)
gpsCoordsFile.write('53.2792737664999996556129190139472484588623046875,  -9.0625117645000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2792737664999996556129190139472484588623046875,  -9.0622911283000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_8.png", image.image_data_uint8)
gpsCoordsFile.write('53.2792737664999996556129190139472484588623046875,  -9.0622911283000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2792737664999996556129190139472484588623046875,  -9.0620704921000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_9.png", image.image_data_uint8)
gpsCoordsFile.write('53.2792737664999996556129190139472484588623046875,  -9.0620704921000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2792737664999996556129190139472484588623046875,  -9.0618498559000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_10.png", image.image_data_uint8)
gpsCoordsFile.write('53.2792737664999996556129190139472484588623046875,  -9.0618498559000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2792737664999996556129190139472484588623046875,  -9.0616292197000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_11.png", image.image_data_uint8)
gpsCoordsFile.write('53.2792737664999996556129190139472484588623046875,  -9.0616292197000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2790665126999996556129190139472484588623046875,  -9.0616292197000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_12.png", image.image_data_uint8)
gpsCoordsFile.write('53.2790665126999996556129190139472484588623046875,  -9.0616292197000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2790665126999996556129190139472484588623046875,  -9.0618498559000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_13.png", image.image_data_uint8)
gpsCoordsFile.write('53.2790665126999996556129190139472484588623046875,  -9.0618498559000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2790665126999996556129190139472484588623046875,  -9.0620704921000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_14.png", image.image_data_uint8)
gpsCoordsFile.write('53.2790665126999996556129190139472484588623046875,  -9.0620704921000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2790665126999996556129190139472484588623046875,  -9.0622911283000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_15.png", image.image_data_uint8)
gpsCoordsFile.write('53.2790665126999996556129190139472484588623046875,  -9.0622911283000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2790665126999996556129190139472484588623046875,  -9.0625117645000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_16.png", image.image_data_uint8)
gpsCoordsFile.write('53.2790665126999996556129190139472484588623046875,  -9.0625117645000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2790665126999996556129190139472484588623046875,  -9.0627324007000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_17.png", image.image_data_uint8)
gpsCoordsFile.write('53.2790665126999996556129190139472484588623046875,  -9.0627324007000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2790665126999996556129190139472484588623046875,  -9.0629530369000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_18.png", image.image_data_uint8)
gpsCoordsFile.write('53.2790665126999996556129190139472484588623046875,  -9.0629530369000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2790665126999996556129190139472484588623046875,  -9.0631736731000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_19.png", image.image_data_uint8)
gpsCoordsFile.write('53.2790665126999996556129190139472484588623046875,  -9.0631736731000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2790665126999996556129190139472484588623046875,  -9.0633943093000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_20.png", image.image_data_uint8)
gpsCoordsFile.write('53.2790665126999996556129190139472484588623046875,  -9.0633943093000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2790665126999996556129190139472484588623046875,  -9.0636149455000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_21.png", image.image_data_uint8)
gpsCoordsFile.write('53.2790665126999996556129190139472484588623046875,  -9.0636149455000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2790665126999996556129190139472484588623046875,  -9.0638355817000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_22.png", image.image_data_uint8)
gpsCoordsFile.write('53.2790665126999996556129190139472484588623046875,  -9.0638355817000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2790665126999996556129190139472484588623046875,  -9.0640562179000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_23.png", image.image_data_uint8)
gpsCoordsFile.write('53.2790665126999996556129190139472484588623046875,  -9.0640562179000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2790665126999996556129190139472484588623046875,  -9.0642768541000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_24.png", image.image_data_uint8)
gpsCoordsFile.write('53.2790665126999996556129190139472484588623046875,  -9.0642768541000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2790665126999996556129190139472484588623046875,  -9.0644974903000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_25.png", image.image_data_uint8)
gpsCoordsFile.write('53.2790665126999996556129190139472484588623046875,  -9.0644974903000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2790665126999996556129190139472484588623046875,  -9.0647181265000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_26.png", image.image_data_uint8)
gpsCoordsFile.write('53.2790665126999996556129190139472484588623046875,  -9.0647181265000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2788592588999996556129190139472484588623046875,  -9.0647181265000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_27.png", image.image_data_uint8)
gpsCoordsFile.write('53.2788592588999996556129190139472484588623046875,  -9.0647181265000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2788592588999996556129190139472484588623046875,  -9.0644974903000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_28.png", image.image_data_uint8)
gpsCoordsFile.write('53.2788592588999996556129190139472484588623046875,  -9.0644974903000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2788592588999996556129190139472484588623046875,  -9.0642768541000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_29.png", image.image_data_uint8)
gpsCoordsFile.write('53.2788592588999996556129190139472484588623046875,  -9.0642768541000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2788592588999996556129190139472484588623046875,  -9.0640562179000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_30.png", image.image_data_uint8)
gpsCoordsFile.write('53.2788592588999996556129190139472484588623046875,  -9.0640562179000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2788592588999996556129190139472484588623046875,  -9.0638355817000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_31.png", image.image_data_uint8)
gpsCoordsFile.write('53.2788592588999996556129190139472484588623046875,  -9.0638355817000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2788592588999996556129190139472484588623046875,  -9.0636149455000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_32.png", image.image_data_uint8)
gpsCoordsFile.write('53.2788592588999996556129190139472484588623046875,  -9.0636149455000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2788592588999996556129190139472484588623046875,  -9.0633943093000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_33.png", image.image_data_uint8)
gpsCoordsFile.write('53.2788592588999996556129190139472484588623046875,  -9.0633943093000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2788592588999996556129190139472484588623046875,  -9.0631736731000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_34.png", image.image_data_uint8)
gpsCoordsFile.write('53.2788592588999996556129190139472484588623046875,  -9.0631736731000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2788592588999996556129190139472484588623046875,  -9.0629530369000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_35.png", image.image_data_uint8)
gpsCoordsFile.write('53.2788592588999996556129190139472484588623046875,  -9.0629530369000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2788592588999996556129190139472484588623046875,  -9.0627324007000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_36.png", image.image_data_uint8)
gpsCoordsFile.write('53.2788592588999996556129190139472484588623046875,  -9.0627324007000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2788592588999996556129190139472484588623046875,  -9.0625117645000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_37.png", image.image_data_uint8)
gpsCoordsFile.write('53.2788592588999996556129190139472484588623046875,  -9.0625117645000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2788592588999996556129190139472484588623046875,  -9.0622911283000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_38.png", image.image_data_uint8)
gpsCoordsFile.write('53.2788592588999996556129190139472484588623046875,  -9.0622911283000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2788592588999996556129190139472484588623046875,  -9.0620704921000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_39.png", image.image_data_uint8)
gpsCoordsFile.write('53.2788592588999996556129190139472484588623046875,  -9.0620704921000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2788592588999996556129190139472484588623046875,  -9.0618498559000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_40.png", image.image_data_uint8)
gpsCoordsFile.write('53.2788592588999996556129190139472484588623046875,  -9.0618498559000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2788592588999996556129190139472484588623046875,  -9.0616292197000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_41.png", image.image_data_uint8)
gpsCoordsFile.write('53.2788592588999996556129190139472484588623046875,  -9.0616292197000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794810202999996556129190139472484588623046875,  -9.0616292197000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_42.png", image.image_data_uint8)
gpsCoordsFile.write('53.2794810202999996556129190139472484588623046875,  -9.0616292197000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794810202999996556129190139472484588623046875,  -9.0618498559000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_43.png", image.image_data_uint8)
gpsCoordsFile.write('53.2794810202999996556129190139472484588623046875,  -9.0618498559000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794810202999996556129190139472484588623046875,  -9.0620704921000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_44.png", image.image_data_uint8)
gpsCoordsFile.write('53.2794810202999996556129190139472484588623046875,  -9.0620704921000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794810202999996556129190139472484588623046875,  -9.0622911283000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_45.png", image.image_data_uint8)
gpsCoordsFile.write('53.2794810202999996556129190139472484588623046875,  -9.0622911283000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794810202999996556129190139472484588623046875,  -9.0625117645000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_46.png", image.image_data_uint8)
gpsCoordsFile.write('53.2794810202999996556129190139472484588623046875,  -9.0625117645000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794810202999996556129190139472484588623046875,  -9.0627324007000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_47.png", image.image_data_uint8)
gpsCoordsFile.write('53.2794810202999996556129190139472484588623046875,  -9.0627324007000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794810202999996556129190139472484588623046875,  -9.0629530369000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_48.png", image.image_data_uint8)
gpsCoordsFile.write('53.2794810202999996556129190139472484588623046875,  -9.0629530369000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794810202999996556129190139472484588623046875,  -9.0631736731000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_49.png", image.image_data_uint8)
gpsCoordsFile.write('53.2794810202999996556129190139472484588623046875,  -9.0631736731000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794810202999996556129190139472484588623046875,  -9.0633943093000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_50.png", image.image_data_uint8)
gpsCoordsFile.write('53.2794810202999996556129190139472484588623046875,  -9.0633943093000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794810202999996556129190139472484588623046875,  -9.0636149455000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_51.png", image.image_data_uint8)
gpsCoordsFile.write('53.2794810202999996556129190139472484588623046875,  -9.0636149455000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794810202999996556129190139472484588623046875,  -9.0638355817000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_52.png", image.image_data_uint8)
gpsCoordsFile.write('53.2794810202999996556129190139472484588623046875,  -9.0638355817000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794810202999996556129190139472484588623046875,  -9.0640562179000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_53.png", image.image_data_uint8)
gpsCoordsFile.write('53.2794810202999996556129190139472484588623046875,  -9.0640562179000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794810202999996556129190139472484588623046875,  -9.0642768541000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_54.png", image.image_data_uint8)
gpsCoordsFile.write('53.2794810202999996556129190139472484588623046875,  -9.0642768541000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794810202999996556129190139472484588623046875,  -9.0644974903000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_55.png", image.image_data_uint8)
gpsCoordsFile.write('53.2794810202999996556129190139472484588623046875,  -9.0644974903000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794810202999996556129190139472484588623046875,  -9.0647181265000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_56.png", image.image_data_uint8)
gpsCoordsFile.write('53.2794810202999996556129190139472484588623046875,  -9.0647181265000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2792737664999996556129190139472484588623046875,  -9.0647181265000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_57.png", image.image_data_uint8)
gpsCoordsFile.write('53.2792737664999996556129190139472484588623046875,  -9.0647181265000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2792737664999996556129190139472484588623046875,  -9.0644974903000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_58.png", image.image_data_uint8)
gpsCoordsFile.write('53.2792737664999996556129190139472484588623046875,  -9.0644974903000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2792737664999996556129190139472484588623046875,  -9.0642768541000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_59.png", image.image_data_uint8)
gpsCoordsFile.write('53.2792737664999996556129190139472484588623046875,  -9.0642768541000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2792737664999996556129190139472484588623046875,  -9.0640562179000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_60.png", image.image_data_uint8)
gpsCoordsFile.write('53.2792737664999996556129190139472484588623046875,  -9.0640562179000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2796882740999996556129190139472484588623046875,  -9.0640562179000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_61.png", image.image_data_uint8)
gpsCoordsFile.write('53.2796882740999996556129190139472484588623046875,  -9.0640562179000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2796882740999996556129190139472484588623046875,  -9.0642768541000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_62.png", image.image_data_uint8)
gpsCoordsFile.write('53.2796882740999996556129190139472484588623046875,  -9.0642768541000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2796882740999996556129190139472484588623046875,  -9.0644974903000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_63.png", image.image_data_uint8)
gpsCoordsFile.write('53.2796882740999996556129190139472484588623046875,  -9.0644974903000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2796882740999996556129190139472484588623046875,  -9.0647181265000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_64.png", image.image_data_uint8)
gpsCoordsFile.write('53.2796882740999996556129190139472484588623046875,  -9.0647181265000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2798955278999996556129190139472484588623046875,  -9.0647181265000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_65.png", image.image_data_uint8)
gpsCoordsFile.write('53.2798955278999996556129190139472484588623046875,  -9.0647181265000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2798955278999996556129190139472484588623046875,  -9.0644974903000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_66.png", image.image_data_uint8)
gpsCoordsFile.write('53.2798955278999996556129190139472484588623046875,  -9.0644974903000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2798955278999996556129190139472484588623046875,  -9.0642768541000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_67.png", image.image_data_uint8)
gpsCoordsFile.write('53.2798955278999996556129190139472484588623046875,  -9.0642768541000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2798955278999996556129190139472484588623046875,  -9.0640562179000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_68.png", image.image_data_uint8)
gpsCoordsFile.write('53.2798955278999996556129190139472484588623046875,  -9.0640562179000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2798955278999996556129190139472484588623046875,  -9.0638355817000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_69.png", image.image_data_uint8)
gpsCoordsFile.write('53.2798955278999996556129190139472484588623046875,  -9.0638355817000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2798955278999996556129190139472484588623046875,  -9.0636149455000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_70.png", image.image_data_uint8)
gpsCoordsFile.write('53.2798955278999996556129190139472484588623046875,  -9.0636149455000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2798955278999996556129190139472484588623046875,  -9.0633943093000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_71.png", image.image_data_uint8)
gpsCoordsFile.write('53.2798955278999996556129190139472484588623046875,  -9.0633943093000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2798955278999996556129190139472484588623046875,  -9.0631736731000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_72.png", image.image_data_uint8)
gpsCoordsFile.write('53.2798955278999996556129190139472484588623046875,  -9.0631736731000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2798955278999996556129190139472484588623046875,  -9.0629530369000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_73.png", image.image_data_uint8)
gpsCoordsFile.write('53.2798955278999996556129190139472484588623046875,  -9.0629530369000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2798955278999996556129190139472484588623046875,  -9.0627324007000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_74.png", image.image_data_uint8)
gpsCoordsFile.write('53.2798955278999996556129190139472484588623046875,  -9.0627324007000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2798955278999996556129190139472484588623046875,  -9.0625117645000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_75.png", image.image_data_uint8)
gpsCoordsFile.write('53.2798955278999996556129190139472484588623046875,  -9.0625117645000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2798955278999996556129190139472484588623046875,  -9.0622911283000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_76.png", image.image_data_uint8)
gpsCoordsFile.write('53.2798955278999996556129190139472484588623046875,  -9.0622911283000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2798955278999996556129190139472484588623046875,  -9.0620704921000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_77.png", image.image_data_uint8)
gpsCoordsFile.write('53.2798955278999996556129190139472484588623046875,  -9.0620704921000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2798955278999996556129190139472484588623046875,  -9.0618498559000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_78.png", image.image_data_uint8)
gpsCoordsFile.write('53.2798955278999996556129190139472484588623046875,  -9.0618498559000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2798955278999996556129190139472484588623046875,  -9.0616292197000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_79.png", image.image_data_uint8)
gpsCoordsFile.write('53.2798955278999996556129190139472484588623046875,  -9.0616292197000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2796882740999996556129190139472484588623046875,  -9.0616292197000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_80.png", image.image_data_uint8)
gpsCoordsFile.write('53.2796882740999996556129190139472484588623046875,  -9.0616292197000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2796882740999996556129190139472484588623046875,  -9.0618498559000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_81.png", image.image_data_uint8)
gpsCoordsFile.write('53.2796882740999996556129190139472484588623046875,  -9.0618498559000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2796882740999996556129190139472484588623046875,  -9.0620704921000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_82.png", image.image_data_uint8)
gpsCoordsFile.write('53.2796882740999996556129190139472484588623046875,  -9.0620704921000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2796882740999996556129190139472484588623046875,  -9.0622911283000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_83.png", image.image_data_uint8)
gpsCoordsFile.write('53.2796882740999996556129190139472484588623046875,  -9.0622911283000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2796882740999996556129190139472484588623046875,  -9.0625117645000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_84.png", image.image_data_uint8)
gpsCoordsFile.write('53.2796882740999996556129190139472484588623046875,  -9.0625117645000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2796882740999996556129190139472484588623046875,  -9.0627324007000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_85.png", image.image_data_uint8)
gpsCoordsFile.write('53.2796882740999996556129190139472484588623046875,  -9.0627324007000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2796882740999996556129190139472484588623046875,  -9.0629530369000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_86.png", image.image_data_uint8)
gpsCoordsFile.write('53.2796882740999996556129190139472484588623046875,  -9.0629530369000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2796882740999996556129190139472484588623046875,  -9.0631736731000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_87.png", image.image_data_uint8)
gpsCoordsFile.write('53.2796882740999996556129190139472484588623046875,  -9.0631736731000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2796882740999996556129190139472484588623046875,  -9.0633943093000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_88.png", image.image_data_uint8)
gpsCoordsFile.write('53.2796882740999996556129190139472484588623046875,  -9.0633943093000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2796882740999996556129190139472484588623046875,  -9.0636149455000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_89.png", image.image_data_uint8)
gpsCoordsFile.write('53.2796882740999996556129190139472484588623046875,  -9.0636149455000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2796882740999996556129190139472484588623046875,  -9.0638355817000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_90.png", image.image_data_uint8)
gpsCoordsFile.write('53.2796882740999996556129190139472484588623046875,  -9.0638355817000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2801027816999996556129190139472484588623046875,  -9.0638355817000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_91.png", image.image_data_uint8)
gpsCoordsFile.write('53.2801027816999996556129190139472484588623046875,  -9.0638355817000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2801027816999996556129190139472484588623046875,  -9.0636149455000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_92.png", image.image_data_uint8)
gpsCoordsFile.write('53.2801027816999996556129190139472484588623046875,  -9.0636149455000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2801027816999996556129190139472484588623046875,  -9.0633943093000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_93.png", image.image_data_uint8)
gpsCoordsFile.write('53.2801027816999996556129190139472484588623046875,  -9.0633943093000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2801027816999996556129190139472484588623046875,  -9.0631736731000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_94.png", image.image_data_uint8)
gpsCoordsFile.write('53.2801027816999996556129190139472484588623046875,  -9.0631736731000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2801027816999996556129190139472484588623046875,  -9.0629530369000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_95.png", image.image_data_uint8)
gpsCoordsFile.write('53.2801027816999996556129190139472484588623046875,  -9.0629530369000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2801027816999996556129190139472484588623046875,  -9.0627324007000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_96.png", image.image_data_uint8)
gpsCoordsFile.write('53.2801027816999996556129190139472484588623046875,  -9.0627324007000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2801027816999996556129190139472484588623046875,  -9.0625117645000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_97.png", image.image_data_uint8)
gpsCoordsFile.write('53.2801027816999996556129190139472484588623046875,  -9.0625117645000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2801027816999996556129190139472484588623046875,  -9.0622911283000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_98.png", image.image_data_uint8)
gpsCoordsFile.write('53.2801027816999996556129190139472484588623046875,  -9.0622911283000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2801027816999996556129190139472484588623046875,  -9.0620704921000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_99.png", image.image_data_uint8)
gpsCoordsFile.write('53.2801027816999996556129190139472484588623046875,  -9.0620704921000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2801027816999996556129190139472484588623046875,  -9.0618498559000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_100.png", image.image_data_uint8)
gpsCoordsFile.write('53.2801027816999996556129190139472484588623046875,  -9.0618498559000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2801027816999996556129190139472484588623046875,  -9.0616292197000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_101.png", image.image_data_uint8)
gpsCoordsFile.write('53.2801027816999996556129190139472484588623046875,  -9.0616292197000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803100354999996556129190139472484588623046875,  -9.0616292197000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_102.png", image.image_data_uint8)
gpsCoordsFile.write('53.2803100354999996556129190139472484588623046875,  -9.0616292197000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803100354999996556129190139472484588623046875,  -9.0618498559000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_103.png", image.image_data_uint8)
gpsCoordsFile.write('53.2803100354999996556129190139472484588623046875,  -9.0618498559000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803100354999996556129190139472484588623046875,  -9.0620704921000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_104.png", image.image_data_uint8)
gpsCoordsFile.write('53.2803100354999996556129190139472484588623046875,  -9.0620704921000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803100354999996556129190139472484588623046875,  -9.0622911283000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_105.png", image.image_data_uint8)
gpsCoordsFile.write('53.2803100354999996556129190139472484588623046875,  -9.0622911283000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803100354999996556129190139472484588623046875,  -9.0625117645000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_106.png", image.image_data_uint8)
gpsCoordsFile.write('53.2803100354999996556129190139472484588623046875,  -9.0625117645000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803100354999996556129190139472484588623046875,  -9.0627324007000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_107.png", image.image_data_uint8)
gpsCoordsFile.write('53.2803100354999996556129190139472484588623046875,  -9.0627324007000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803100354999996556129190139472484588623046875,  -9.0629530369000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_108.png", image.image_data_uint8)
gpsCoordsFile.write('53.2803100354999996556129190139472484588623046875,  -9.0629530369000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803100354999996556129190139472484588623046875,  -9.0631736731000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_109.png", image.image_data_uint8)
gpsCoordsFile.write('53.2803100354999996556129190139472484588623046875,  -9.0631736731000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803100354999996556129190139472484588623046875,  -9.0633943093000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_110.png", image.image_data_uint8)
gpsCoordsFile.write('53.2803100354999996556129190139472484588623046875,  -9.0633943093000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803100354999996556129190139472484588623046875,  -9.0636149455000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_111.png", image.image_data_uint8)
gpsCoordsFile.write('53.2803100354999996556129190139472484588623046875,  -9.0636149455000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803100354999996556129190139472484588623046875,  -9.0638355817000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_112.png", image.image_data_uint8)
gpsCoordsFile.write('53.2803100354999996556129190139472484588623046875,  -9.0638355817000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803100354999996556129190139472484588623046875,  -9.0640562179000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_113.png", image.image_data_uint8)
gpsCoordsFile.write('53.2803100354999996556129190139472484588623046875,  -9.0640562179000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803100354999996556129190139472484588623046875,  -9.0642768541000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_114.png", image.image_data_uint8)
gpsCoordsFile.write('53.2803100354999996556129190139472484588623046875,  -9.0642768541000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803100354999996556129190139472484588623046875,  -9.0644974903000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_115.png", image.image_data_uint8)
gpsCoordsFile.write('53.2803100354999996556129190139472484588623046875,  -9.0644974903000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803100354999996556129190139472484588623046875,  -9.0647181265000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_116.png", image.image_data_uint8)
gpsCoordsFile.write('53.2803100354999996556129190139472484588623046875,  -9.0647181265000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2801027816999996556129190139472484588623046875,  -9.0647181265000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_117.png", image.image_data_uint8)
gpsCoordsFile.write('53.2801027816999996556129190139472484588623046875,  -9.0647181265000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2801027816999996556129190139472484588623046875,  -9.0644974903000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_118.png", image.image_data_uint8)
gpsCoordsFile.write('53.2801027816999996556129190139472484588623046875,  -9.0644974903000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2801027816999996556129190139472484588623046875,  -9.0642768541000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_119.png", image.image_data_uint8)
gpsCoordsFile.write('53.2801027816999996556129190139472484588623046875,  -9.0642768541000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2801027816999996556129190139472484588623046875,  -9.0640562179000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_120.png", image.image_data_uint8)
gpsCoordsFile.write('53.2801027816999996556129190139472484588623046875,  -9.0640562179000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805172892999996556129190139472484588623046875,  -9.0640562179000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_121.png", image.image_data_uint8)
gpsCoordsFile.write('53.2805172892999996556129190139472484588623046875,  -9.0640562179000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805172892999996556129190139472484588623046875,  -9.0642768541000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_122.png", image.image_data_uint8)
gpsCoordsFile.write('53.2805172892999996556129190139472484588623046875,  -9.0642768541000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805172892999996556129190139472484588623046875,  -9.0644974903000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_123.png", image.image_data_uint8)
gpsCoordsFile.write('53.2805172892999996556129190139472484588623046875,  -9.0644974903000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805172892999996556129190139472484588623046875,  -9.0647181265000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_124.png", image.image_data_uint8)
gpsCoordsFile.write('53.2805172892999996556129190139472484588623046875,  -9.0647181265000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807245430999996556129190139472484588623046875,  -9.0647181265000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_125.png", image.image_data_uint8)
gpsCoordsFile.write('53.2807245430999996556129190139472484588623046875,  -9.0647181265000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807245430999996556129190139472484588623046875,  -9.0644974903000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_126.png", image.image_data_uint8)
gpsCoordsFile.write('53.2807245430999996556129190139472484588623046875,  -9.0644974903000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807245430999996556129190139472484588623046875,  -9.0642768541000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_127.png", image.image_data_uint8)
gpsCoordsFile.write('53.2807245430999996556129190139472484588623046875,  -9.0642768541000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807245430999996556129190139472484588623046875,  -9.0640562179000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_128.png", image.image_data_uint8)
gpsCoordsFile.write('53.2807245430999996556129190139472484588623046875,  -9.0640562179000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807245430999996556129190139472484588623046875,  -9.0638355817000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_129.png", image.image_data_uint8)
gpsCoordsFile.write('53.2807245430999996556129190139472484588623046875,  -9.0638355817000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807245430999996556129190139472484588623046875,  -9.0636149455000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_130.png", image.image_data_uint8)
gpsCoordsFile.write('53.2807245430999996556129190139472484588623046875,  -9.0636149455000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807245430999996556129190139472484588623046875,  -9.0633943093000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_131.png", image.image_data_uint8)
gpsCoordsFile.write('53.2807245430999996556129190139472484588623046875,  -9.0633943093000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807245430999996556129190139472484588623046875,  -9.0631736731000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_132.png", image.image_data_uint8)
gpsCoordsFile.write('53.2807245430999996556129190139472484588623046875,  -9.0631736731000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807245430999996556129190139472484588623046875,  -9.0629530369000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_133.png", image.image_data_uint8)
gpsCoordsFile.write('53.2807245430999996556129190139472484588623046875,  -9.0629530369000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807245430999996556129190139472484588623046875,  -9.0627324007000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_134.png", image.image_data_uint8)
gpsCoordsFile.write('53.2807245430999996556129190139472484588623046875,  -9.0627324007000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807245430999996556129190139472484588623046875,  -9.0625117645000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_135.png", image.image_data_uint8)
gpsCoordsFile.write('53.2807245430999996556129190139472484588623046875,  -9.0625117645000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807245430999996556129190139472484588623046875,  -9.0622911283000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_136.png", image.image_data_uint8)
gpsCoordsFile.write('53.2807245430999996556129190139472484588623046875,  -9.0622911283000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807245430999996556129190139472484588623046875,  -9.0620704921000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_137.png", image.image_data_uint8)
gpsCoordsFile.write('53.2807245430999996556129190139472484588623046875,  -9.0620704921000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807245430999996556129190139472484588623046875,  -9.0618498559000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_138.png", image.image_data_uint8)
gpsCoordsFile.write('53.2807245430999996556129190139472484588623046875,  -9.0618498559000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807245430999996556129190139472484588623046875,  -9.0616292197000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_139.png", image.image_data_uint8)
gpsCoordsFile.write('53.2807245430999996556129190139472484588623046875,  -9.0616292197000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805172892999996556129190139472484588623046875,  -9.0616292197000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_140.png", image.image_data_uint8)
gpsCoordsFile.write('53.2805172892999996556129190139472484588623046875,  -9.0616292197000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805172892999996556129190139472484588623046875,  -9.0618498559000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_141.png", image.image_data_uint8)
gpsCoordsFile.write('53.2805172892999996556129190139472484588623046875,  -9.0618498559000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805172892999996556129190139472484588623046875,  -9.0620704921000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_142.png", image.image_data_uint8)
gpsCoordsFile.write('53.2805172892999996556129190139472484588623046875,  -9.0620704921000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805172892999996556129190139472484588623046875,  -9.0622911283000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_143.png", image.image_data_uint8)
gpsCoordsFile.write('53.2805172892999996556129190139472484588623046875,  -9.0622911283000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805172892999996556129190139472484588623046875,  -9.0625117645000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_144.png", image.image_data_uint8)
gpsCoordsFile.write('53.2805172892999996556129190139472484588623046875,  -9.0625117645000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805172892999996556129190139472484588623046875,  -9.0627324007000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_145.png", image.image_data_uint8)
gpsCoordsFile.write('53.2805172892999996556129190139472484588623046875,  -9.0627324007000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805172892999996556129190139472484588623046875,  -9.0629530369000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_146.png", image.image_data_uint8)
gpsCoordsFile.write('53.2805172892999996556129190139472484588623046875,  -9.0629530369000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805172892999996556129190139472484588623046875,  -9.0631736731000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_147.png", image.image_data_uint8)
gpsCoordsFile.write('53.2805172892999996556129190139472484588623046875,  -9.0631736731000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805172892999996556129190139472484588623046875,  -9.0633943093000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_148.png", image.image_data_uint8)
gpsCoordsFile.write('53.2805172892999996556129190139472484588623046875,  -9.0633943093000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805172892999996556129190139472484588623046875,  -9.0636149455000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_149.png", image.image_data_uint8)
gpsCoordsFile.write('53.2805172892999996556129190139472484588623046875,  -9.0636149455000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805172892999996556129190139472484588623046875,  -9.0638355817000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_150.png", image.image_data_uint8)
gpsCoordsFile.write('53.2805172892999996556129190139472484588623046875,  -9.0638355817000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2809317968999996556129190139472484588623046875,  -9.0638355817000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_151.png", image.image_data_uint8)
gpsCoordsFile.write('53.2809317968999996556129190139472484588623046875,  -9.0638355817000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2809317968999996556129190139472484588623046875,  -9.0636149455000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_152.png", image.image_data_uint8)
gpsCoordsFile.write('53.2809317968999996556129190139472484588623046875,  -9.0636149455000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2809317968999996556129190139472484588623046875,  -9.0633943093000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_153.png", image.image_data_uint8)
gpsCoordsFile.write('53.2809317968999996556129190139472484588623046875,  -9.0633943093000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2809317968999996556129190139472484588623046875,  -9.0631736731000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_154.png", image.image_data_uint8)
gpsCoordsFile.write('53.2809317968999996556129190139472484588623046875,  -9.0631736731000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2809317968999996556129190139472484588623046875,  -9.0629530369000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_155.png", image.image_data_uint8)
gpsCoordsFile.write('53.2809317968999996556129190139472484588623046875,  -9.0629530369000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2809317968999996556129190139472484588623046875,  -9.0627324007000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_156.png", image.image_data_uint8)
gpsCoordsFile.write('53.2809317968999996556129190139472484588623046875,  -9.0627324007000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2809317968999996556129190139472484588623046875,  -9.0625117645000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_157.png", image.image_data_uint8)
gpsCoordsFile.write('53.2809317968999996556129190139472484588623046875,  -9.0625117645000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2809317968999996556129190139472484588623046875,  -9.0622911283000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_158.png", image.image_data_uint8)
gpsCoordsFile.write('53.2809317968999996556129190139472484588623046875,  -9.0622911283000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2809317968999996556129190139472484588623046875,  -9.0620704921000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_159.png", image.image_data_uint8)
gpsCoordsFile.write('53.2809317968999996556129190139472484588623046875,  -9.0620704921000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2809317968999996556129190139472484588623046875,  -9.0618498559000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_160.png", image.image_data_uint8)
gpsCoordsFile.write('53.2809317968999996556129190139472484588623046875,  -9.0618498559000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2809317968999996556129190139472484588623046875,  -9.0616292197000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_161.png", image.image_data_uint8)
gpsCoordsFile.write('53.2809317968999996556129190139472484588623046875,  -9.0616292197000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2809317968999996556129190139472484588623046875,  -9.0640562179000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_162.png", image.image_data_uint8)
gpsCoordsFile.write('53.2809317968999996556129190139472484588623046875,  -9.0640562179000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2809317968999996556129190139472484588623046875,  -9.0642768541000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_163.png", image.image_data_uint8)
gpsCoordsFile.write('53.2809317968999996556129190139472484588623046875,  -9.0642768541000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2809317968999996556129190139472484588623046875,  -9.0644974903000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_164.png", image.image_data_uint8)
gpsCoordsFile.write('53.2809317968999996556129190139472484588623046875,  -9.0644974903000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2809317968999996556129190139472484588623046875,  -9.0647181265000006517619112855754792690277099609375, 55.0), 2.2)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_165.png", image.image_data_uint8)
gpsCoordsFile.write('53.2809317968999996556129190139472484588623046875,  -9.0647181265000006517619112855754792690277099609375/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(client.GPS_to_unreal.home_position_GPS.lat, gps_mapper.home_position_GPS.long, 55.0), 2.2)
time.sleep(2)
client.land()
client.armDisarm(False)

gpsCoordsFile.close()
AirSimgpsCoordsFile.close()
AirSimgpsRelativeCoordsFile.close()
