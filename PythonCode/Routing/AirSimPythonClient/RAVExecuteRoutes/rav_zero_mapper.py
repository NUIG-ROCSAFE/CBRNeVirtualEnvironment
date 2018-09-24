import io
import time
import os
import sys
#append folder level up to import AirSimClient
sys.path.append('..')
sys.path.append('../GPSMappings')
from PIL import Image
from AirSimClient import *
gpsCoordsFile = open('D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/GPSCoords\GPSCoords1.txt', 'w')
AirSimgpsCoordsFile = open('D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/GPSCoords\AirSimGPSCoords1.txt', 'w')
AirSimgpsRelativeCoordsFile = open('D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/GPSCoords\AirSimRelativeGPSCoords1.txt', 'w')
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
client.moveToGPSPosition(GPSCoordinate(53.280000000000001136868377216160297393798828125,  -9.07000000000000028421709430404007434844970703125, 30.0), 7)
time.sleep(1)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_0.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_0.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280000000000001136868377216160297393798828125,  -9.07000000000000028421709430404007434844970703125\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27999289959030227193070459179580211639404296875,  -9.0650753974781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_1.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_1.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27999289959030227193070459179580211639404296875,  -9.0650753974781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27999289959030227193070459179580211639404296875,  -9.0647778510781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_2.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_2.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27999289959030227193070459179580211639404296875,  -9.0647778510781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27999289959030227193070459179580211639404296875,  -9.0644803046781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_3.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_3.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27999289959030227193070459179580211639404296875,  -9.0644803046781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27999289959030227193070459179580211639404296875,  -9.0641827582781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_4.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_4.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27999289959030227193070459179580211639404296875,  -9.0641827582781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27999289959030227193070459179580211639404296875,  -9.0638852118781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_5.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_5.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27999289959030227193070459179580211639404296875,  -9.0638852118781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27999289959030227193070459179580211639404296875,  -9.0635876654781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_6.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_6.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27999289959030227193070459179580211639404296875,  -9.0635876654781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27999289959030227193070459179580211639404296875,  -9.0632901190781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_7.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_7.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27999289959030227193070459179580211639404296875,  -9.0632901190781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27999289959030227193070459179580211639404296875,  -9.0629925726781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_8.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_8.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27999289959030227193070459179580211639404296875,  -9.0629925726781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27999289959030227193070459179580211639404296875,  -9.0626950262781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_9.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_9.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27999289959030227193070459179580211639404296875,  -9.0626950262781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27999289959030227193070459179580211639404296875,  -9.0623974798781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_10.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_10.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27999289959030227193070459179580211639404296875,  -9.0623974798781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27999289959030227193070459179580211639404296875,  -9.0620999334781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_11.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_11.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27999289959030227193070459179580211639404296875,  -9.0620999334781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27999289959030227193070459179580211639404296875,  -9.0618023870781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_12.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_12.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27999289959030227193070459179580211639404296875,  -9.0618023870781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27999289959030227193070459179580211639404296875,  -9.0615048406781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_13.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_13.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27999289959030227193070459179580211639404296875,  -9.0615048406781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27980511969030227193070459179580211639404296875,  -9.0615048406781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_14.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_14.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27980511969030227193070459179580211639404296875,  -9.0615048406781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27980511969030227193070459179580211639404296875,  -9.0612072942781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_15.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_15.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27980511969030227193070459179580211639404296875,  -9.0612072942781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27961733979030227193070459179580211639404296875,  -9.0615048406781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_16.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_16.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27961733979030227193070459179580211639404296875,  -9.0615048406781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27961733979030227193070459179580211639404296875,  -9.0618023870781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_17.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_17.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27961733979030227193070459179580211639404296875,  -9.0618023870781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27961733979030227193070459179580211639404296875,  -9.0620999334781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_18.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_18.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27961733979030227193070459179580211639404296875,  -9.0620999334781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27961733979030227193070459179580211639404296875,  -9.0623974798781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_19.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_19.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27961733979030227193070459179580211639404296875,  -9.0623974798781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27961733979030227193070459179580211639404296875,  -9.0626950262781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_20.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_20.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27961733979030227193070459179580211639404296875,  -9.0626950262781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27961733979030227193070459179580211639404296875,  -9.0629925726781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_21.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_21.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27961733979030227193070459179580211639404296875,  -9.0629925726781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27961733979030227193070459179580211639404296875,  -9.0632901190781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_22.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_22.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27961733979030227193070459179580211639404296875,  -9.0632901190781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27961733979030227193070459179580211639404296875,  -9.0635876654781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_23.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_23.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27961733979030227193070459179580211639404296875,  -9.0635876654781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27961733979030227193070459179580211639404296875,  -9.0638852118781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_24.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_24.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27961733979030227193070459179580211639404296875,  -9.0638852118781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27961733979030227193070459179580211639404296875,  -9.0641827582781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_25.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_25.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27961733979030227193070459179580211639404296875,  -9.0641827582781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27961733979030227193070459179580211639404296875,  -9.0644803046781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_26.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_26.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27961733979030227193070459179580211639404296875,  -9.0644803046781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27961733979030227193070459179580211639404296875,  -9.0647778510781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_27.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_27.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27961733979030227193070459179580211639404296875,  -9.0647778510781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27942955989030227193070459179580211639404296875,  -9.0647778510781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_28.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_28.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27942955989030227193070459179580211639404296875,  -9.0647778510781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27942955989030227193070459179580211639404296875,  -9.0644803046781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_29.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_29.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27942955989030227193070459179580211639404296875,  -9.0644803046781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27942955989030227193070459179580211639404296875,  -9.0641827582781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_30.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_30.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27942955989030227193070459179580211639404296875,  -9.0641827582781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27942955989030227193070459179580211639404296875,  -9.0638852118781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_31.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_31.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27942955989030227193070459179580211639404296875,  -9.0638852118781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27942955989030227193070459179580211639404296875,  -9.0635876654781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_32.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_32.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27942955989030227193070459179580211639404296875,  -9.0635876654781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27942955989030227193070459179580211639404296875,  -9.0632901190781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_33.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_33.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27942955989030227193070459179580211639404296875,  -9.0632901190781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27942955989030227193070459179580211639404296875,  -9.0629925726781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_34.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_34.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27942955989030227193070459179580211639404296875,  -9.0629925726781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27942955989030227193070459179580211639404296875,  -9.0626950262781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_35.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_35.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27942955989030227193070459179580211639404296875,  -9.0626950262781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27942955989030227193070459179580211639404296875,  -9.0623974798781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_36.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_36.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27942955989030227193070459179580211639404296875,  -9.0623974798781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27980511969030227193070459179580211639404296875,  -9.0623974798781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_37.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_37.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27980511969030227193070459179580211639404296875,  -9.0623974798781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27980511969030227193070459179580211639404296875,  -9.0626950262781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_38.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_38.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27980511969030227193070459179580211639404296875,  -9.0626950262781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27980511969030227193070459179580211639404296875,  -9.0629925726781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_39.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_39.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27980511969030227193070459179580211639404296875,  -9.0629925726781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27980511969030227193070459179580211639404296875,  -9.0632901190781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_40.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_40.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27980511969030227193070459179580211639404296875,  -9.0632901190781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27924177999030227193070459179580211639404296875,  -9.0632901190781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_41.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_41.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27924177999030227193070459179580211639404296875,  -9.0632901190781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27924177999030227193070459179580211639404296875,  -9.0629925726781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_42.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_42.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27924177999030227193070459179580211639404296875,  -9.0629925726781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27905400009030227193070459179580211639404296875,  -9.0638852118781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_43.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_43.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27905400009030227193070459179580211639404296875,  -9.0638852118781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27905400009030227193070459179580211639404296875,  -9.0641827582781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_44.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_44.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27905400009030227193070459179580211639404296875,  -9.0641827582781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27905400009030227193070459179580211639404296875,  -9.0644803046781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_45.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_45.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27905400009030227193070459179580211639404296875,  -9.0644803046781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.28055623929030227193070459179580211639404296875,  -9.0635876654781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_46.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_46.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.28055623929030227193070459179580211639404296875,  -9.0635876654781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.28055623929030227193070459179580211639404296875,  -9.0629925726781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_47.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_47.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.28055623929030227193070459179580211639404296875,  -9.0629925726781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.28055623929030227193070459179580211639404296875,  -9.0623974798781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_48.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_48.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.28055623929030227193070459179580211639404296875,  -9.0623974798781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.28018067949030227193070459179580211639404296875,  -9.0615048406781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_49.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_49.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.28018067949030227193070459179580211639404296875,  -9.0615048406781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.27980511969030227193070459179580211639404296875,  -9.0618023870781791571955182007513940334320068359375, 30.0), 3.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene)])
print('Writing files to ', "D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_50.png".format('example', saved_images_dir = 'D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:/TempFiles/CBRNeVirtualEnvironment//RAVCollectedData/PNGImages"+"\Images1\Camera{}\image_50.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27980511969030227193070459179580211639404296875,  -9.0618023870781791571955182007513940334320068359375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(gps_mapper.home_position_GPS()[0], gps_mapper.home_position_GPS()[1], 30.0), 3.0)
time.sleep(2)
client.land()
client.armDisarm(False)

gpsCoordsFile.close()
AirSimgpsCoordsFile.close()
AirSimgpsRelativeCoordsFile.close()
