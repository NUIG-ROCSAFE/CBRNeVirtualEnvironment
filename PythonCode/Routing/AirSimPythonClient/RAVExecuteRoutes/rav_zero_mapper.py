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

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.280000000000001136868377216160297393798828125,  -9.0619999999999993889332472463138401508331298828125/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279963157689398138588876463472843170166015625,  -9.0621447562722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.279963157689398138588876463472843170166015625,  -9.0621447562722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279963157689398138588876463472843170166015625,  -9.0626835822722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.279963157689398138588876463472843170166015625,  -9.0626835822722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279963157689398138588876463472843170166015625,  -9.0632224082722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.279963157689398138588876463472843170166015625,  -9.0632224082722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279963157689398138588876463472843170166015625,  -9.0637612342722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.279963157689398138588876463472843170166015625,  -9.0637612342722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279446763889398138588876463472843170166015625,  -9.0637612342722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.279446763889398138588876463472843170166015625,  -9.0637612342722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279446763889398138588876463472843170166015625,  -9.0632224082722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.279446763889398138588876463472843170166015625,  -9.0632224082722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279446763889398138588876463472843170166015625,  -9.0626835822722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.279446763889398138588876463472843170166015625,  -9.0626835822722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279446763889398138588876463472843170166015625,  -9.0621447562722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.279446763889398138588876463472843170166015625,  -9.0621447562722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279446763889398138588876463472843170166015625,  -9.0616059302722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.279446763889398138588876463472843170166015625,  -9.0616059302722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279446763889398138588876463472843170166015625,  -9.0610671042722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.279446763889398138588876463472843170166015625,  -9.0610671042722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279446763889398138588876463472843170166015625,  -9.0605282782722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.279446763889398138588876463472843170166015625,  -9.0605282782722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279446763889398138588876463472843170166015625,  -9.0599894522722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.279446763889398138588876463472843170166015625,  -9.0599894522722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279963157689398138588876463472843170166015625,  -9.0599894522722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.279963157689398138588876463472843170166015625,  -9.0599894522722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279963157689398138588876463472843170166015625,  -9.0605282782722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.279963157689398138588876463472843170166015625,  -9.0605282782722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279963157689398138588876463472843170166015625,  -9.0610671042722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.279963157689398138588876463472843170166015625,  -9.0610671042722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279963157689398138588876463472843170166015625,  -9.0616059302722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.279963157689398138588876463472843170166015625,  -9.0616059302722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280479551489398138588876463472843170166015625,  -9.0616059302722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.280479551489398138588876463472843170166015625,  -9.0616059302722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280479551489398138588876463472843170166015625,  -9.0621447562722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.280479551489398138588876463472843170166015625,  -9.0621447562722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280479551489398138588876463472843170166015625,  -9.0626835822722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.280479551489398138588876463472843170166015625,  -9.0626835822722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280479551489398138588876463472843170166015625,  -9.0632224082722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.280479551489398138588876463472843170166015625,  -9.0632224082722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280479551489398138588876463472843170166015625,  -9.0637612342722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.280479551489398138588876463472843170166015625,  -9.0637612342722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280479551489398138588876463472843170166015625,  -9.0610671042722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.280479551489398138588876463472843170166015625,  -9.0610671042722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280479551489398138588876463472843170166015625,  -9.0605282782722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.280479551489398138588876463472843170166015625,  -9.0605282782722203495886788005009293556213378906250/n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '/n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'/n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280479551489398138588876463472843170166015625,  -9.0599894522722203495886788005009293556213378906250, 30.0), 10.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Cameraexample camera"+ "/image_0.png")
for camera_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment/RAVCollectedData/PNGImages"+"/ImagesRAV1" + "/Camera{}"+ "/image_{}.png".format(camera_index, line_index))
gpsCoordsFile.write('53.280479551489398138588876463472843170166015625,  -9.0599894522722203495886788005009293556213378906250/n')
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
