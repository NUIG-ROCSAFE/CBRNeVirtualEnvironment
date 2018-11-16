import argparse
import sys
sys.path.append('..')
sys.path.append('../..')
from generateUnrealCoordinatesFromGPS import read_GPS_coords, write_UE4_coords, GenerateUECoordsFromGPS
from GPSCoordinate import GPSCoordinate

def main(GPS_CSV: 'file path to csv containing gps coordinates', desination_UE4_coord_file = 'file to save converted UE4 coordinates', GPS_home_pos: "GPSCoordinate which records where the RAV home position is located" = GPSCoordinate(53.2793, -9.0638)):
	gps_coords = read_GPS_coords(GPS_CSV)
	converter = GenerateUECoordsFromGPS(GPS_home_pos)
	UE4_coords = converter.convert_GPS_list_to_UE4(gps_coords)
	write_UE4_coords(desination_UE4_coord_file, UE4_coords)
	


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Automatically write the python files necessary to send the specified number of RAVs on routes given by a file containing GPS coordinates')
	#metavar is a name for the argument in usage messages.
	#nargs -The number of command-line arguments that should be consumed.
	parser.add_argument("GPS_CSV", type = str, metavar = "GPS_CSV", help = "CSV of GPS locations for RAV to visit")
	parser.add_argument("desination_UE4_coord_file", type = str, metavar = "desination_UE4_coord_file", help = "file to save converted UE4 coordinates")
	parser.add_argument("GPS_home_pos_lat", type = float, metavar = "GPS_home_pos_lat", nargs = '?', help = "latitude which records where the RAV home position is located")
	parser.add_argument("GPS_home_pos_lng", type = float, metavar = "GPS_home_pos_lng", nargs = '?', help = "longitude which records where the RAV home position is located")
	parser.add_argument("GPS_home_pos_alt", type = float, metavar = "GPS_home_pos_alt", nargs = '?', help = "altitude which records where the RAV home position is located")
	
	args = vars(parser.parse_args())
	print(args)
	if args["GPS_home_pos_lat"] and args["GPS_home_pos_lng"]:
		args["GPS_home_pos"] = GPSCoordinate(args["GPS_home_pos_lat"], args["GPS_home_pos_lng"], args["GPS_home_pos_alt"])
		
	del args["GPS_home_pos_lat"]
	del args["GPS_home_pos_lng"]
	del args["GPS_home_pos_alt"]
	
	main(**args)