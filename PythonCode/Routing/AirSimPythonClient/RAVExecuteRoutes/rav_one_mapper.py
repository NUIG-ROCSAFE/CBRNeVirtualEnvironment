import io
import time
import os
from PIL import Image
from AirSimClient import *
gpsCoordsFile = open('D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\GPSCoords\GPSCoords2.txt', 'w')
AirSimgpsCoordsFile = open('D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\GPSCoords\AirSimGPSCoords2.txt', 'w')
AirSimgpsRelativeCoordsFile = open('D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\GPSCoords\AirSimRelativeGPSCoords2.txt', 'w')
port = 41452
print('Creating new client on port: ',41452)
# connect to the AirSim simulator
client = MultirotorClient(port=41452)
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
client.moveToGPSPosition(GPSCoordinate(53.28600000000000136424205265939235687255859375,  -9.0587999999999997413624441833235323429107666015625, 18.5), 7)
time.sleep(1)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_0.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_0.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.28600000000000136424205265939235687255859375,  -9.0587999999999997413624441833235323429107666015625\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807806916220017552419449202716350555419921875,  -9.0627300740897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_1.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_1.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2807806916220017552419449202716350555419921875,  -9.0627300740897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807806916220017552419449202716350555419921875,  -9.0629625321897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_2.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_2.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2807806916220017552419449202716350555419921875,  -9.0629625321897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807806916220017552419449202716350555419921875,  -9.0631949902897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_3.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_3.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2807806916220017552419449202716350555419921875,  -9.0631949902897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807806916220017552419449202716350555419921875,  -9.0634274483897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_4.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_4.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2807806916220017552419449202716350555419921875,  -9.0634274483897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807806916220017552419449202716350555419921875,  -9.0636599064897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_5.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_5.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2807806916220017552419449202716350555419921875,  -9.0636599064897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807806916220017552419449202716350555419921875,  -9.0638923645897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_6.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_6.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2807806916220017552419449202716350555419921875,  -9.0638923645897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807806916220017552419449202716350555419921875,  -9.0641248226897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_7.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_7.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2807806916220017552419449202716350555419921875,  -9.0641248226897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807806916220017552419449202716350555419921875,  -9.0643572807897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_8.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_8.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2807806916220017552419449202716350555419921875,  -9.0643572807897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807806916220017552419449202716350555419921875,  -9.0645897388897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_9.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_9.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2807806916220017552419449202716350555419921875,  -9.0645897388897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805526089220017552419449202716350555419921875,  -9.0645897388897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_10.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_10.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2805526089220017552419449202716350555419921875,  -9.0645897388897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805526089220017552419449202716350555419921875,  -9.0643572807897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_11.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_11.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2805526089220017552419449202716350555419921875,  -9.0643572807897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805526089220017552419449202716350555419921875,  -9.0641248226897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_12.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_12.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2805526089220017552419449202716350555419921875,  -9.0641248226897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805526089220017552419449202716350555419921875,  -9.0638923645897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_13.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_13.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2805526089220017552419449202716350555419921875,  -9.0638923645897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805526089220017552419449202716350555419921875,  -9.0636599064897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_14.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_14.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2805526089220017552419449202716350555419921875,  -9.0636599064897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805526089220017552419449202716350555419921875,  -9.0634274483897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_15.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_15.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2805526089220017552419449202716350555419921875,  -9.0634274483897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805526089220017552419449202716350555419921875,  -9.0631949902897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_16.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_16.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2805526089220017552419449202716350555419921875,  -9.0631949902897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805526089220017552419449202716350555419921875,  -9.0629625321897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_17.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_17.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2805526089220017552419449202716350555419921875,  -9.0629625321897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805526089220017552419449202716350555419921875,  -9.0627300740897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_18.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_18.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2805526089220017552419449202716350555419921875,  -9.0627300740897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805526089220017552419449202716350555419921875,  -9.0624976159897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_19.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_19.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2805526089220017552419449202716350555419921875,  -9.0624976159897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805526089220017552419449202716350555419921875,  -9.0622651578897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_20.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_20.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2805526089220017552419449202716350555419921875,  -9.0622651578897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803245262220017552419449202716350555419921875,  -9.0622651578897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_21.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_21.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2803245262220017552419449202716350555419921875,  -9.0622651578897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803245262220017552419449202716350555419921875,  -9.0620326997897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_22.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_22.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2803245262220017552419449202716350555419921875,  -9.0620326997897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803245262220017552419449202716350555419921875,  -9.0618002416897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_23.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_23.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2803245262220017552419449202716350555419921875,  -9.0618002416897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2800964435220017552419449202716350555419921875,  -9.0618002416897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_24.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_24.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2800964435220017552419449202716350555419921875,  -9.0618002416897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2800964435220017552419449202716350555419921875,  -9.0620326997897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_25.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_25.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2800964435220017552419449202716350555419921875,  -9.0620326997897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2800964435220017552419449202716350555419921875,  -9.0622651578897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_26.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_26.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2800964435220017552419449202716350555419921875,  -9.0622651578897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2800964435220017552419449202716350555419921875,  -9.0624976159897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_27.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_27.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2800964435220017552419449202716350555419921875,  -9.0624976159897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2800964435220017552419449202716350555419921875,  -9.0627300740897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_28.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_28.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2800964435220017552419449202716350555419921875,  -9.0627300740897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2800964435220017552419449202716350555419921875,  -9.0629625321897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_29.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_29.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2800964435220017552419449202716350555419921875,  -9.0629625321897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2800964435220017552419449202716350555419921875,  -9.0631949902897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_30.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_30.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2800964435220017552419449202716350555419921875,  -9.0631949902897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2800964435220017552419449202716350555419921875,  -9.0634274483897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_31.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_31.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2800964435220017552419449202716350555419921875,  -9.0634274483897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2800964435220017552419449202716350555419921875,  -9.0636599064897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_32.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_32.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2800964435220017552419449202716350555419921875,  -9.0636599064897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2800964435220017552419449202716350555419921875,  -9.0638923645897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_33.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_33.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2800964435220017552419449202716350555419921875,  -9.0638923645897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803245262220017552419449202716350555419921875,  -9.0638923645897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_34.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_34.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2803245262220017552419449202716350555419921875,  -9.0638923645897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803245262220017552419449202716350555419921875,  -9.0636599064897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_35.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_35.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2803245262220017552419449202716350555419921875,  -9.0636599064897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803245262220017552419449202716350555419921875,  -9.0634274483897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_36.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_36.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2803245262220017552419449202716350555419921875,  -9.0634274483897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803245262220017552419449202716350555419921875,  -9.0631949902897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_37.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_37.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2803245262220017552419449202716350555419921875,  -9.0631949902897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803245262220017552419449202716350555419921875,  -9.0629625321897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_38.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_38.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2803245262220017552419449202716350555419921875,  -9.0629625321897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803245262220017552419449202716350555419921875,  -9.0627300740897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_39.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_39.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2803245262220017552419449202716350555419921875,  -9.0627300740897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2803245262220017552419449202716350555419921875,  -9.0624976159897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_40.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_40.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2803245262220017552419449202716350555419921875,  -9.0624976159897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2800964435220017552419449202716350555419921875,  -9.0615677835897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_41.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_41.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2800964435220017552419449202716350555419921875,  -9.0615677835897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2800964435220017552419449202716350555419921875,  -9.0613353254897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_42.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_42.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2800964435220017552419449202716350555419921875,  -9.0613353254897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2798683608220017552419449202716350555419921875,  -9.0615677835897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_43.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_43.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2798683608220017552419449202716350555419921875,  -9.0615677835897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794121954220017552419449202716350555419921875,  -9.0620326997897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_44.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_44.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2794121954220017552419449202716350555419921875,  -9.0620326997897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794121954220017552419449202716350555419921875,  -9.0622651578897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_45.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_45.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2794121954220017552419449202716350555419921875,  -9.0622651578897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794121954220017552419449202716350555419921875,  -9.0624976159897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_46.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_46.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2794121954220017552419449202716350555419921875,  -9.0624976159897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2791841127220017552419449202716350555419921875,  -9.0624976159897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_47.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_47.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2791841127220017552419449202716350555419921875,  -9.0624976159897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2791841127220017552419449202716350555419921875,  -9.0629625321897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_48.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_48.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2791841127220017552419449202716350555419921875,  -9.0629625321897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2791841127220017552419449202716350555419921875,  -9.0634274483897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_49.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_49.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2791841127220017552419449202716350555419921875,  -9.0634274483897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2791841127220017552419449202716350555419921875,  -9.0638923645897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_50.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_50.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2791841127220017552419449202716350555419921875,  -9.0638923645897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2791841127220017552419449202716350555419921875,  -9.0643572807897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_51.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_51.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2791841127220017552419449202716350555419921875,  -9.0643572807897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2791841127220017552419449202716350555419921875,  -9.0648221969897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_52.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_52.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2791841127220017552419449202716350555419921875,  -9.0648221969897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794121954220017552419449202716350555419921875,  -9.0650546550897008183386788005009293556213378906250, 18.5), 2.0)
time.sleep(2)

responses = client.simGetImages([ImageRequest(3, AirSimImageType.Scene), ImageRequest(2, AirSimImageType.Scene), ImageRequest(1, AirSimImageType.Scene), ImageRequest(4, AirSimImageType.Scene)])
print('Writing files to ', "D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_53.png".format('example', saved_images_dir = 'D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file("D:\IJCAI2018\IJCAIDemoCodeAll\PythonCode\PythonClientGPSMapping\GPSMappings\Images"+"\Images2\Camera{}\image_53.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2794121954220017552419449202716350555419921875,  -9.0650546550897008183386788005009293556213378906250\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

gpsCoordsFile.close()
AirSimgpsCoordsFile.close()
AirSimgpsRelativeCoordsFile.close()
