import io
import time
import os
from PIL import Image
from AirSimClient import *
os.chdir('..\..')
print('Working from directory: ', os.getcwd())
gpsCoordsFile = open(os.getcwd() + '\PythonClientGPSMapping\GPSMappings\GPSCoords\GPSCoords2.txt', 'w')
AirSimgpsCoordsFile = open(os.getcwd() + '\PythonClientGPSMapping\GPSMappings\GPSCoords\AirSimGPSCoords2.txt', 'w')
AirSimgpsRelativeCoordsFile = open(os.getcwd() + '\PythonClientGPSMapping\GPSMappings\GPSCoords\AirSimRelativeGPSCoords2.txt', 'w')
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
client.moveToGPSPosition(GPSCoordinate(53.28600000000000136424205265939235687255859375,  -9.0587999999999997413624441833235323429107666015625, 35), 7)
time.sleep(1)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_0.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_0.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.28600000000000136424205265939235687255859375,  -9.0587999999999997413624441833235323429107666015625\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807874630985979304168722592294216156005859375,  -9.0618968009079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_1.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_1.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2807874630985979304168722592294216156005859375,  -9.0618968009079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807874630985979304168722592294216156005859375,  -9.0621328353079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_2.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_2.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2807874630985979304168722592294216156005859375,  -9.0621328353079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807874630985979304168722592294216156005859375,  -9.0623688697079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_3.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_3.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2807874630985979304168722592294216156005859375,  -9.0623688697079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2807874630985979304168722592294216156005859375,  -9.0626049041079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_4.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_4.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2807874630985979304168722592294216156005859375,  -9.0626049041079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805404925985979304168722592294216156005859375,  -9.0626049041079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_5.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_5.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2805404925985979304168722592294216156005859375,  -9.0626049041079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805404925985979304168722592294216156005859375,  -9.0628409385079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_6.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_6.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2805404925985979304168722592294216156005859375,  -9.0628409385079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805404925985979304168722592294216156005859375,  -9.0630769729079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_7.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_7.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2805404925985979304168722592294216156005859375,  -9.0630769729079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805404925985979304168722592294216156005859375,  -9.0633130073079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_8.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_8.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2805404925985979304168722592294216156005859375,  -9.0633130073079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805404925985979304168722592294216156005859375,  -9.0635490417079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_9.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_9.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2805404925985979304168722592294216156005859375,  -9.0635490417079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805404925985979304168722592294216156005859375,  -9.0637850761079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_10.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_10.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2805404925985979304168722592294216156005859375,  -9.0637850761079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805404925985979304168722592294216156005859375,  -9.0640211105079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_11.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_11.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2805404925985979304168722592294216156005859375,  -9.0640211105079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805404925985979304168722592294216156005859375,  -9.0642571449079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_12.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_12.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2805404925985979304168722592294216156005859375,  -9.0642571449079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805404925985979304168722592294216156005859375,  -9.0644931793079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_13.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_13.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2805404925985979304168722592294216156005859375,  -9.0644931793079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2805404925985979304168722592294216156005859375,  -9.0647292137079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_14.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_14.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2805404925985979304168722592294216156005859375,  -9.0647292137079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2802935220985979304168722592294216156005859375,  -9.0647292137079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_15.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_15.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2802935220985979304168722592294216156005859375,  -9.0647292137079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2802935220985979304168722592294216156005859375,  -9.0644931793079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_16.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_16.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2802935220985979304168722592294216156005859375,  -9.0644931793079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2802935220985979304168722592294216156005859375,  -9.0642571449079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_17.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_17.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2802935220985979304168722592294216156005859375,  -9.0642571449079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2802935220985979304168722592294216156005859375,  -9.0640211105079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_18.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_18.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2802935220985979304168722592294216156005859375,  -9.0640211105079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2802935220985979304168722592294216156005859375,  -9.0637850761079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_19.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_19.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2802935220985979304168722592294216156005859375,  -9.0637850761079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2802935220985979304168722592294216156005859375,  -9.0635490417079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_20.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_20.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2802935220985979304168722592294216156005859375,  -9.0635490417079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2802935220985979304168722592294216156005859375,  -9.0633130073079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_21.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_21.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2802935220985979304168722592294216156005859375,  -9.0633130073079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2802935220985979304168722592294216156005859375,  -9.0630769729079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_22.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_22.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2802935220985979304168722592294216156005859375,  -9.0630769729079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2797995810985979304168722592294216156005859375,  -9.0630769729079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_23.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_23.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2797995810985979304168722592294216156005859375,  -9.0630769729079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2797995810985979304168722592294216156005859375,  -9.0633130073079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_24.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_24.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2797995810985979304168722592294216156005859375,  -9.0633130073079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2797995810985979304168722592294216156005859375,  -9.0635490417079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_25.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_25.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2797995810985979304168722592294216156005859375,  -9.0635490417079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2797995810985979304168722592294216156005859375,  -9.0637850761079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_26.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_26.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2797995810985979304168722592294216156005859375,  -9.0637850761079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2797995810985979304168722592294216156005859375,  -9.0640211105079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_27.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_27.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2797995810985979304168722592294216156005859375,  -9.0640211105079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2797995810985979304168722592294216156005859375,  -9.0642571449079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_28.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_28.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2797995810985979304168722592294216156005859375,  -9.0642571449079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2797995810985979304168722592294216156005859375,  -9.0644931793079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_29.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_29.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2797995810985979304168722592294216156005859375,  -9.0644931793079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2797995810985979304168722592294216156005859375,  -9.0647292137079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_30.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_30.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2797995810985979304168722592294216156005859375,  -9.0647292137079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2795526105985979304168722592294216156005859375,  -9.0647292137079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_31.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_31.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2795526105985979304168722592294216156005859375,  -9.0647292137079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2795526105985979304168722592294216156005859375,  -9.0644931793079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_32.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_32.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2795526105985979304168722592294216156005859375,  -9.0644931793079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2795526105985979304168722592294216156005859375,  -9.0642571449079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_33.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_33.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2795526105985979304168722592294216156005859375,  -9.0642571449079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2795526105985979304168722592294216156005859375,  -9.0640211105079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_34.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_34.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2795526105985979304168722592294216156005859375,  -9.0640211105079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2795526105985979304168722592294216156005859375,  -9.0637850761079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_35.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_35.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2795526105985979304168722592294216156005859375,  -9.0637850761079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2793056400985979304168722592294216156005859375,  -9.0637850761079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_36.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_36.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2793056400985979304168722592294216156005859375,  -9.0637850761079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2793056400985979304168722592294216156005859375,  -9.0640211105079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_37.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_37.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2793056400985979304168722592294216156005859375,  -9.0640211105079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2793056400985979304168722592294216156005859375,  -9.0642571449079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_38.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_38.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2793056400985979304168722592294216156005859375,  -9.0642571449079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2793056400985979304168722592294216156005859375,  -9.0644931793079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_39.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_39.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2793056400985979304168722592294216156005859375,  -9.0644931793079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2793056400985979304168722592294216156005859375,  -9.0647292137079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_40.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_40.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2793056400985979304168722592294216156005859375,  -9.0647292137079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2795526105985979304168722592294216156005859375,  -9.0626049041079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_41.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_41.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2795526105985979304168722592294216156005859375,  -9.0626049041079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2795526105985979304168722592294216156005859375,  -9.0623688697079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_42.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_42.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2795526105985979304168722592294216156005859375,  -9.0623688697079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2795526105985979304168722592294216156005859375,  -9.0621328353079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_43.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_43.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2795526105985979304168722592294216156005859375,  -9.0621328353079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2795526105985979304168722592294216156005859375,  -9.0618968009079101562500000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_44.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images2\Camera{}\image_44.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2795526105985979304168722592294216156005859375,  -9.0618968009079101562500000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

gpsCoordsFile.close()
AirSimgpsCoordsFile.close()
AirSimgpsRelativeCoordsFile.close()
