import io
import time
import os
from PIL import Image
from AirSimClient import *
os.chdir('..\..')
print('Working from directory: ', os.getcwd())
gpsCoordsFile = open(os.getcwd() + '\PythonClientGPSMapping\GPSMappings\GPSCoords\GPSCoords3.txt', 'w')
AirSimgpsCoordsFile = open(os.getcwd() + '\PythonClientGPSMapping\GPSMappings\GPSCoords\AirSimGPSCoords3.txt', 'w')
AirSimgpsRelativeCoordsFile = open(os.getcwd() + '\PythonClientGPSMapping\GPSMappings\GPSCoords\AirSimRelativeGPSCoords3.txt', 'w')
port = 41453
print('Creating new client on port: ',41453)
# connect to the AirSim simulator
client = MultirotorClient(port=41453)
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
client.moveToGPSPosition(GPSCoordinate(53.27980000000000160298441187478601932525634765625,  -9.056499999999999772626324556767940521240234375, 35), 7)
time.sleep(1)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_0.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_0.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.27980000000000160298441187478601932525634765625,  -9.056499999999999772626324556767940521240234375\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2799150529579982395938714034855365753173828125,  -9.0619885920718505859375000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_1.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_1.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2799150529579982395938714034855365753173828125,  -9.0619885920718505859375000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2799150529579982395938714034855365753173828125,  -9.0623593329718505859375000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_2.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_2.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2799150529579982395938714034855365753173828125,  -9.0623593329718505859375000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2799150529579982395938714034855365753173828125,  -9.0627300738718505859375000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_3.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_3.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2799150529579982395938714034855365753173828125,  -9.0627300738718505859375000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2799150529579982395938714034855365753173828125,  -9.0631008147718505859375000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_4.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_4.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2799150529579982395938714034855365753173828125,  -9.0631008147718505859375000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2796787731579982395938714034855365753173828125,  -9.0631008147718505859375000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_5.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_5.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2796787731579982395938714034855365753173828125,  -9.0631008147718505859375000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2796787731579982395938714034855365753173828125,  -9.0627300738718505859375000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_6.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_6.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2796787731579982395938714034855365753173828125,  -9.0627300738718505859375000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2796787731579982395938714034855365753173828125,  -9.0623593329718505859375000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_7.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_7.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2796787731579982395938714034855365753173828125,  -9.0623593329718505859375000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794424933579982395938714034855365753173828125,  -9.0623593329718505859375000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_8.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_8.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2794424933579982395938714034855365753173828125,  -9.0623593329718505859375000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794424933579982395938714034855365753173828125,  -9.0627300738718505859375000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_9.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_9.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2794424933579982395938714034855365753173828125,  -9.0627300738718505859375000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794424933579982395938714034855365753173828125,  -9.0631008147718505859375000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_10.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_10.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2794424933579982395938714034855365753173828125,  -9.0631008147718505859375000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2794424933579982395938714034855365753173828125,  -9.0634715556718505859375000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_11.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_11.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2794424933579982395938714034855365753173828125,  -9.0634715556718505859375000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

client.moveToGPSPosition(GPSCoordinate(53.2801513327579982395938714034855365753173828125,  -9.0619885920718505859375000000000000000000000000000, 35), 5)
time.sleep(2)

responses = client.simGetImages([
	ImageRequest(3, AirSimImageType.Scene)
	])
print('Writing files to ', os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_12.png".format('example'))
for image_index, image in enumerate(responses):
	AirSimClientBase.write_file(os.getcwd() + "\PythonClientGPSMapping\GPSMappings\Images\Images3\Camera{}\image_12.png".format(image_index+1) , image.image_data_uint8)
gpsCoordsFile.write('53.2801513327579982395938714034855365753173828125,  -9.0619885920718505859375000000000000000000000000000\n')
gpsCoordsFile.flush()
AirSimgpsCoordsFile.write(str(client.getGpsLocation().latitude)+', '+str(client.getGpsLocation().longitude) + '\n')
AirSimgpsCoordsFile.flush()
AirSimgpsRelativeCoordsFile.write(str(client.getGPSLocationRelative().lat)+', '+ str(client.getGPSLocationRelative().long)+'\n')
AirSimgpsRelativeCoordsFile.flush()
print('NUIG relative GPS location: ', client.getGPSLocationRelative())

gpsCoordsFile.close()
AirSimgpsCoordsFile.close()
AirSimgpsRelativeCoordsFile.close()
