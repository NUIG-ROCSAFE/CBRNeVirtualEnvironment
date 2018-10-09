import sys

sys.path.append('../../Routing/AirSimPythonClient/GPS')
from GPSToUnreal import GPSToUnreal
from GPSCoordinate import GPSCoordinate
from UE4Coord import UE4Coord

def read_GPS_coords(gps_coords_file_path) -> "A list of gps coords":
	'''Reads in a list of gps coordinates'''
	try:
		#read file but skip header
		gps_coords = open(gps_coords_file_path, 'r').readlines()[1:]
	except FileNotFoundError as e:
		#don't handle this for now...
		raise e
	
	try:
		gps_coords = [GPSCoordinate(coord.replace('\n','').split(',')[0], coord.replace('\n','').split(',')[1], coord.replace('\n','').split(',')[2])for coord in filter(lambda gps_coord: gps_coord != '\n', gps_coords)]
	except IndexError as e:
		#don't handle for now
		gps_coords = [GPSCoordinate(coord.replace('\n','').split(',')[0], coord.replace('\n','').split(',')[1]) for coord in filter(lambda gps_coord: gps_coord != '\n', gps_coords)]
	print('gps_coords: ',gps_coords)
	return gps_coords
	
def write_UE4_coords(ue4_coords_file_path, UE4_coords: "a list of UE4 Coordinates"):
	with open(ue4_coords_file_path, 'w') as out_file:
		#write header
		out_file.write('x, y, z\n')
		for UE4_coord in UE4_coords:
			print(UE4_coord)
			out_file.write(UE4_coord.__str__())
			out_file.write('\n')

class GenerateUECoordsFromGPS:
	def __init__(self, home_position_GPS: GPSCoordinate = GPSCoordinate(53.2793, -9.0638), home_position_UE4 = UE4Coord(0,0,0)):
		#set home gps position
		self.home_position_GPS = home_position_GPS
		self.home_position_UE4 = home_position_UE4
		self.GPS_to_unreal_converter = GPSToUnreal(home_position_GPS)
		
	def convert_GPS_to_UE4(self,gps_coordinate):
		return UE4Coord(*self.GPS_to_unreal_converter.getMoveToPosXYZFromGPSCoord(gps_coordinate)) + self.home_position_UE4
		
	def convert_GPS_list_to_UE4(self, gps_coordinates: "a list of gpscoordinates"):
		ue4_coords = []
		for gps_coordinate in gps_coordinates:
			ue4_coords.append(self.convert_GPS_to_UE4(gps_coordinate))
		return ue4_coords
		
		