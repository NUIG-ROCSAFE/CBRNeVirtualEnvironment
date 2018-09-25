import io
import time
import os
import sys
#append folder level up to import AirSimClient
sys.path.append('..')
sys.path.append('../GPSMappings')
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
client.moveToGPSPosition(GPSCoordinate(53.280000000000001136868377216160297393798828125,  -9.0619999999999993889332472463138401508331298828125, 30.0), 7)
time.sleep(1)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_0.png", image.image_data_uint8)
gpsCoordsFile.write('53.280000000000001136868377216160297393798828125,  -9.0619999999999993889332472463138401508331298828125/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27990222262589912109760916791856288909912109375,  -9.0619665383316894531250000000000000000000000000000, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_1.png", image.image_data_uint8)
gpsCoordsFile.write('53.27990222262589912109760916791856288909912109375,  -9.0619665383316894531250000000000000000000000000000/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27990222262589912109760916791856288909912109375,  -9.0623460709316894531250000000000000000000000000000, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_2.png", image.image_data_uint8)
gpsCoordsFile.write('53.27990222262589912109760916791856288909912109375,  -9.0623460709316894531250000000000000000000000000000/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27990222262589912109760916791856288909912109375,  -9.0627256035316894531250000000000000000000000000000, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_3.png", image.image_data_uint8)
gpsCoordsFile.write('53.27990222262589912109760916791856288909912109375,  -9.0627256035316894531250000000000000000000000000000/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27990222262589912109760916791856288909912109375,  -9.0631051361316894531250000000000000000000000000000, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_4.png", image.image_data_uint8)
gpsCoordsFile.write('53.27990222262589912109760916791856288909912109375,  -9.0631051361316894531250000000000000000000000000000/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27952535082589912109760916791856288909912109375,  -9.0631051361316894531250000000000000000000000000000, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_5.png", image.image_data_uint8)
gpsCoordsFile.write('53.27952535082589912109760916791856288909912109375,  -9.0631051361316894531250000000000000000000000000000/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27952535082589912109760916791856288909912109375,  -9.0627256035316894531250000000000000000000000000000, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_6.png", image.image_data_uint8)
gpsCoordsFile.write('53.27952535082589912109760916791856288909912109375,  -9.0627256035316894531250000000000000000000000000000/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27952535082589912109760916791856288909912109375,  -9.0623460709316894531250000000000000000000000000000, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_7.png", image.image_data_uint8)
gpsCoordsFile.write('53.27952535082589912109760916791856288909912109375,  -9.0623460709316894531250000000000000000000000000000/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27952535082589912109760916791856288909912109375,  -9.0619665383316894531250000000000000000000000000000, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_8.png", image.image_data_uint8)
gpsCoordsFile.write('53.27952535082589912109760916791856288909912109375,  -9.0619665383316894531250000000000000000000000000000/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27952535082589912109760916791856288909912109375,  -9.0615870057316894531250000000000000000000000000000, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_9.png", image.image_data_uint8)
gpsCoordsFile.write('53.27952535082589912109760916791856288909912109375,  -9.0615870057316894531250000000000000000000000000000/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27952535082589912109760916791856288909912109375,  -9.0612074731316894531250000000000000000000000000000, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_10.png", image.image_data_uint8)
gpsCoordsFile.write('53.27952535082589912109760916791856288909912109375,  -9.0612074731316894531250000000000000000000000000000/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27952535082589912109760916791856288909912109375,  -9.0608279405316894531250000000000000000000000000000, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_11.png", image.image_data_uint8)
gpsCoordsFile.write('53.27952535082589912109760916791856288909912109375,  -9.0608279405316894531250000000000000000000000000000/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27990222262589912109760916791856288909912109375,  -9.0608279405316894531250000000000000000000000000000, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_12.png", image.image_data_uint8)
gpsCoordsFile.write('53.27990222262589912109760916791856288909912109375,  -9.0608279405316894531250000000000000000000000000000/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27990222262589912109760916791856288909912109375,  -9.0612074731316894531250000000000000000000000000000, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_13.png", image.image_data_uint8)
gpsCoordsFile.write('53.27990222262589912109760916791856288909912109375,  -9.0612074731316894531250000000000000000000000000000/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27990222262589912109760916791856288909912109375,  -9.0615870057316894531250000000000000000000000000000, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_14.png", image.image_data_uint8)
gpsCoordsFile.write('53.27990222262589912109760916791856288909912109375,  -9.0615870057316894531250000000000000000000000000000/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.28027909442589912109760916791856288909912109375,  -9.0615870057316894531250000000000000000000000000000, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_15.png", image.image_data_uint8)
gpsCoordsFile.write('53.28027909442589912109760916791856288909912109375,  -9.0615870057316894531250000000000000000000000000000/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.28027909442589912109760916791856288909912109375,  -9.0619665383316894531250000000000000000000000000000, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_16.png", image.image_data_uint8)
gpsCoordsFile.write('53.28027909442589912109760916791856288909912109375,  -9.0619665383316894531250000000000000000000000000000/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.28027909442589912109760916791856288909912109375,  -9.0623460709316894531250000000000000000000000000000, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_17.png", image.image_data_uint8)
gpsCoordsFile.write('53.28027909442589912109760916791856288909912109375,  -9.0623460709316894531250000000000000000000000000000/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.28027909442589912109760916791856288909912109375,  -9.0627256035316894531250000000000000000000000000000, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_18.png", image.image_data_uint8)
gpsCoordsFile.write('53.28027909442589912109760916791856288909912109375,  -9.0627256035316894531250000000000000000000000000000/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.28027909442589912109760916791856288909912109375,  -9.0631051361316894531250000000000000000000000000000, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_19.png", image.image_data_uint8)
gpsCoordsFile.write('53.28027909442589912109760916791856288909912109375,  -9.0631051361316894531250000000000000000000000000000/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.28027909442589912109760916791856288909912109375,  -9.0612074731316894531250000000000000000000000000000, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_20.png", image.image_data_uint8)
gpsCoordsFile.write('53.28027909442589912109760916791856288909912109375,  -9.0612074731316894531250000000000000000000000000000/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.28027909442589912109760916791856288909912109375,  -9.0608279405316894531250000000000000000000000000000, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexamplecamera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}".format(camera_index+1)+ "/image_21.png", image.image_data_uint8)
gpsCoordsFile.write('53.28027909442589912109760916791856288909912109375,  -9.0608279405316894531250000000000000000000000000000/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(client.GPS_to_unreal.home_position_GPS()[0], gps_mapper.home_position_GPS()[1], 30.0), 10.0)
time.sleep(2)
client.land()
client.armDisarm(False)

gpsCoordsFile.close()
AirSimgpsCoordsFile.close()
AirSimgpsRelativeCoordsFile.close()
