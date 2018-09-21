import io
import time
import os
from PIL import Image
from AirSimClient import *
gpsCoordsFile = open('D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\GPSCoords\GPSCoords1.txt', 'w')
AirSimgpsCoordsFile = open('D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\GPSCoords\AirSimGPSCoords1.txt', 'w')
AirSimgpsRelativeCoordsFile = open('D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\GPSCoords\AirSimRelativeGPSCoords1.txt', 'w')
port = 41451
print('Creating new client on port: ',41451)
# connect to the AirSim simulator
client = MultirotorClient(port=41451)
print('Confirming connection...')
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
print('Client position: {}'.format(client.getPosition()))
client.moveToGPSPosition(GPSCoordinate(53.280000000000001136868377216160297393798828125,  -9.07000000000000028421709430404007434844970703125, 18.5), 7)
time.sleep(1)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_0.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_0.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280000000000001136868377216160297393798828125,  -9.07000000000000028421709430404007434844970703125\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279447836528299682424403727054595947265625,  -9.0653917193157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_1.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_1.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279447836528299682424403727054595947265625,  -9.0653917193157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279447836528299682424403727054595947265625,  -9.0651315450157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_2.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_2.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279447836528299682424403727054595947265625,  -9.0651315450157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279447836528299682424403727054595947265625,  -9.0648713707157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_3.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_3.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279447836528299682424403727054595947265625,  -9.0648713707157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279447836528299682424403727054595947265625,  -9.0646111964157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_4.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_4.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279447836528299682424403727054595947265625,  -9.0646111964157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279447836528299682424403727054595947265625,  -9.0643510221157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_5.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_5.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279447836528299682424403727054595947265625,  -9.0643510221157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279447836528299682424403727054595947265625,  -9.0640908478157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_6.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_6.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279447836528299682424403727054595947265625,  -9.0640908478157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279447836528299682424403727054595947265625,  -9.0638306735157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_7.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_7.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279447836528299682424403727054595947265625,  -9.0638306735157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279447836528299682424403727054595947265625,  -9.0635704992157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_8.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_8.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279447836528299682424403727054595947265625,  -9.0635704992157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279447836528299682424403727054595947265625,  -9.0633103249157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_9.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_9.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279447836528299682424403727054595947265625,  -9.0633103249157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279447836528299682424403727054595947265625,  -9.0630501506157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_10.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_10.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279447836528299682424403727054595947265625,  -9.0630501506157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279447836528299682424403727054595947265625,  -9.0627899763157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_11.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_11.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279447836528299682424403727054595947265625,  -9.0627899763157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279447836528299682424403727054595947265625,  -9.0625298020157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_12.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_12.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279447836528299682424403727054595947265625,  -9.0625298020157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279447836528299682424403727054595947265625,  -9.0622696277157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_13.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_13.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279447836528299682424403727054595947265625,  -9.0622696277157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279636005028299682424403727054595947265625,  -9.0622696277157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_14.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_14.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279636005028299682424403727054595947265625,  -9.0622696277157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279636005028299682424403727054595947265625,  -9.0625298020157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_15.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_15.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279636005028299682424403727054595947265625,  -9.0625298020157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279636005028299682424403727054595947265625,  -9.0627899763157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_16.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_16.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279636005028299682424403727054595947265625,  -9.0627899763157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279636005028299682424403727054595947265625,  -9.0630501506157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_17.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_17.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279636005028299682424403727054595947265625,  -9.0630501506157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279636005028299682424403727054595947265625,  -9.0633103249157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_18.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_18.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279636005028299682424403727054595947265625,  -9.0633103249157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279636005028299682424403727054595947265625,  -9.0635704992157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_19.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_19.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279636005028299682424403727054595947265625,  -9.0635704992157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279636005028299682424403727054595947265625,  -9.0638306735157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_20.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_20.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279636005028299682424403727054595947265625,  -9.0638306735157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279636005028299682424403727054595947265625,  -9.0640908478157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_21.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_21.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279636005028299682424403727054595947265625,  -9.0640908478157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279636005028299682424403727054595947265625,  -9.0643510221157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_22.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_22.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279636005028299682424403727054595947265625,  -9.0643510221157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279636005028299682424403727054595947265625,  -9.0646111964157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_23.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_23.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279636005028299682424403727054595947265625,  -9.0646111964157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279636005028299682424403727054595947265625,  -9.0648713707157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_24.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_24.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279636005028299682424403727054595947265625,  -9.0648713707157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279636005028299682424403727054595947265625,  -9.0651315450157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_25.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_25.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279636005028299682424403727054595947265625,  -9.0651315450157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279824173528299682424403727054595947265625,  -9.0648713707157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_26.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_26.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279824173528299682424403727054595947265625,  -9.0648713707157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279824173528299682424403727054595947265625,  -9.0646111964157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_27.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_27.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279824173528299682424403727054595947265625,  -9.0646111964157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279824173528299682424403727054595947265625,  -9.0643510221157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_28.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_28.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279824173528299682424403727054595947265625,  -9.0643510221157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279824173528299682424403727054595947265625,  -9.0640908478157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_29.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_29.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279824173528299682424403727054595947265625,  -9.0640908478157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279824173528299682424403727054595947265625,  -9.0638306735157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_30.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_30.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279824173528299682424403727054595947265625,  -9.0638306735157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279824173528299682424403727054595947265625,  -9.0635704992157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_31.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_31.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279824173528299682424403727054595947265625,  -9.0635704992157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279824173528299682424403727054595947265625,  -9.0633103249157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_32.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_32.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279824173528299682424403727054595947265625,  -9.0633103249157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279824173528299682424403727054595947265625,  -9.0630501506157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_33.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_33.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279824173528299682424403727054595947265625,  -9.0630501506157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279824173528299682424403727054595947265625,  -9.0627899763157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_34.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_34.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279824173528299682424403727054595947265625,  -9.0627899763157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279824173528299682424403727054595947265625,  -9.0625298020157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_35.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_35.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279824173528299682424403727054595947265625,  -9.0625298020157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279824173528299682424403727054595947265625,  -9.0622696277157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_36.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_36.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279824173528299682424403727054595947265625,  -9.0622696277157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279824173528299682424403727054595947265625,  -9.0620094534157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_37.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_37.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279824173528299682424403727054595947265625,  -9.0620094534157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279824173528299682424403727054595947265625,  -9.0617492791157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_38.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_38.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279824173528299682424403727054595947265625,  -9.0617492791157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279636005028299682424403727054595947265625,  -9.0617492791157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_39.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_39.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279636005028299682424403727054595947265625,  -9.0617492791157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279636005028299682424403727054595947265625,  -9.0620094534157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_40.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_40.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279636005028299682424403727054595947265625,  -9.0620094534157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280012342028299682424403727054595947265625,  -9.0620094534157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_41.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_41.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280012342028299682424403727054595947265625,  -9.0620094534157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280012342028299682424403727054595947265625,  -9.0622696277157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_42.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_42.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280012342028299682424403727054595947265625,  -9.0622696277157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280012342028299682424403727054595947265625,  -9.0625298020157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_43.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_43.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280012342028299682424403727054595947265625,  -9.0625298020157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280012342028299682424403727054595947265625,  -9.0627899763157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_44.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_44.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280012342028299682424403727054595947265625,  -9.0627899763157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280012342028299682424403727054595947265625,  -9.0630501506157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_45.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_45.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280012342028299682424403727054595947265625,  -9.0630501506157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280012342028299682424403727054595947265625,  -9.0633103249157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_46.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_46.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280012342028299682424403727054595947265625,  -9.0633103249157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280012342028299682424403727054595947265625,  -9.0635704992157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_47.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_47.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280012342028299682424403727054595947265625,  -9.0635704992157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280012342028299682424403727054595947265625,  -9.0638306735157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_48.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_48.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280012342028299682424403727054595947265625,  -9.0638306735157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280012342028299682424403727054595947265625,  -9.0640908478157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_49.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_49.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280012342028299682424403727054595947265625,  -9.0640908478157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280012342028299682424403727054595947265625,  -9.0643510221157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_50.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_50.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280012342028299682424403727054595947265625,  -9.0643510221157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280012342028299682424403727054595947265625,  -9.0646111964157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_51.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_51.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280012342028299682424403727054595947265625,  -9.0646111964157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280012342028299682424403727054595947265625,  -9.0648713707157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_52.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_52.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280012342028299682424403727054595947265625,  -9.0648713707157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280200510528299682424403727054595947265625,  -9.0646111964157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_53.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_53.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280200510528299682424403727054595947265625,  -9.0646111964157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280200510528299682424403727054595947265625,  -9.0643510221157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_54.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_54.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280200510528299682424403727054595947265625,  -9.0643510221157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280200510528299682424403727054595947265625,  -9.0640908478157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_55.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_55.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280200510528299682424403727054595947265625,  -9.0640908478157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280200510528299682424403727054595947265625,  -9.0638306735157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_56.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_56.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280200510528299682424403727054595947265625,  -9.0638306735157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280200510528299682424403727054595947265625,  -9.0635704992157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_57.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_57.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280200510528299682424403727054595947265625,  -9.0635704992157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280200510528299682424403727054595947265625,  -9.0633103249157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_58.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_58.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280200510528299682424403727054595947265625,  -9.0633103249157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280200510528299682424403727054595947265625,  -9.0630501506157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_59.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_59.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280200510528299682424403727054595947265625,  -9.0630501506157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280200510528299682424403727054595947265625,  -9.0627899763157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_60.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_60.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280200510528299682424403727054595947265625,  -9.0627899763157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280200510528299682424403727054595947265625,  -9.0625298020157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_61.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_61.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280200510528299682424403727054595947265625,  -9.0625298020157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280200510528299682424403727054595947265625,  -9.0622696277157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_62.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_62.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280200510528299682424403727054595947265625,  -9.0622696277157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280200510528299682424403727054595947265625,  -9.0620094534157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_63.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_63.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280200510528299682424403727054595947265625,  -9.0620094534157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280388679028299682424403727054595947265625,  -9.0620094534157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_64.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_64.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280388679028299682424403727054595947265625,  -9.0620094534157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280388679028299682424403727054595947265625,  -9.0622696277157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_65.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_65.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280388679028299682424403727054595947265625,  -9.0622696277157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280388679028299682424403727054595947265625,  -9.0625298020157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_66.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_66.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280388679028299682424403727054595947265625,  -9.0625298020157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280388679028299682424403727054595947265625,  -9.0627899763157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_67.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_67.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280388679028299682424403727054595947265625,  -9.0627899763157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280388679028299682424403727054595947265625,  -9.0630501506157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_68.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_68.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280388679028299682424403727054595947265625,  -9.0630501506157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280388679028299682424403727054595947265625,  -9.0633103249157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_69.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_69.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280388679028299682424403727054595947265625,  -9.0633103249157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280388679028299682424403727054595947265625,  -9.0635704992157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_70.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_70.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280388679028299682424403727054595947265625,  -9.0635704992157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280388679028299682424403727054595947265625,  -9.0638306735157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_71.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_71.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280388679028299682424403727054595947265625,  -9.0638306735157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280388679028299682424403727054595947265625,  -9.0640908478157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_72.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_72.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280388679028299682424403727054595947265625,  -9.0640908478157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280388679028299682424403727054595947265625,  -9.0643510221157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_73.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_73.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280388679028299682424403727054595947265625,  -9.0643510221157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280576847528299682424403727054595947265625,  -9.0640908478157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_74.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_74.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280576847528299682424403727054595947265625,  -9.0640908478157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280576847528299682424403727054595947265625,  -9.0638306735157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_75.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_75.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280576847528299682424403727054595947265625,  -9.0638306735157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280576847528299682424403727054595947265625,  -9.0635704992157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_76.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_76.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280576847528299682424403727054595947265625,  -9.0635704992157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280576847528299682424403727054595947265625,  -9.0633103249157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_77.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_77.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280576847528299682424403727054595947265625,  -9.0633103249157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280576847528299682424403727054595947265625,  -9.0630501506157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_78.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_78.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280576847528299682424403727054595947265625,  -9.0630501506157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280576847528299682424403727054595947265625,  -9.0627899763157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_79.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_79.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280576847528299682424403727054595947265625,  -9.0627899763157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280576847528299682424403727054595947265625,  -9.0625298020157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_80.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_80.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280576847528299682424403727054595947265625,  -9.0625298020157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280576847528299682424403727054595947265625,  -9.0622696277157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_81.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_81.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280576847528299682424403727054595947265625,  -9.0622696277157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.280012342028299682424403727054595947265625,  -9.0617492791157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_82.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_82.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.280012342028299682424403727054595947265625,  -9.0617492791157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279259668028299682424403727054595947265625,  -9.0627899763157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_83.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_83.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279259668028299682424403727054595947265625,  -9.0627899763157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279259668028299682424403727054595947265625,  -9.0630501506157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_84.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_84.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279259668028299682424403727054595947265625,  -9.0630501506157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279259668028299682424403727054595947265625,  -9.0633103249157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_85.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_85.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279259668028299682424403727054595947265625,  -9.0633103249157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279259668028299682424403727054595947265625,  -9.0635704992157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_86.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_86.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279259668028299682424403727054595947265625,  -9.0635704992157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279259668028299682424403727054595947265625,  -9.0638306735157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_87.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_87.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279259668028299682424403727054595947265625,  -9.0638306735157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279259668028299682424403727054595947265625,  -9.0640908478157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_88.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_88.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279259668028299682424403727054595947265625,  -9.0640908478157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279259668028299682424403727054595947265625,  -9.0643510221157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_89.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_89.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279259668028299682424403727054595947265625,  -9.0643510221157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279259668028299682424403727054595947265625,  -9.0646111964157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_90.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_90.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279259668028299682424403727054595947265625,  -9.0646111964157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279259668028299682424403727054595947265625,  -9.0648713707157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_91.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_91.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279259668028299682424403727054595947265625,  -9.0648713707157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.279259668028299682424403727054595947265625,  -9.0651315450157208798931605997495353221893310546875, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_92.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images1\Camera{}\image_92.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.279259668028299682424403727054595947265625,  -9.0651315450157208798931605997495353221893310546875\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

gpsCoordsFile.close()
AirSimgpsCoordsFile.close()
AirSimgpsRelativeCoordsFile.close()
