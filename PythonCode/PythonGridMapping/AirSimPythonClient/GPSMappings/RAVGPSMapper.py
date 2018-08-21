from GPSMappings.GPSCoordinate import GPSCoordinate


class RAVGPSMapper:
    # this is taken as origin (0,0)
    # EYRE_SQUARE_COORD = GPSCoordinate(53.2745, -9.049, 0)
    # NUIG
    # EYRE_SQUARE_COORD = GPSCoordinate(53.276, -9.057, 0)
    # not quite eyre square, but close enough!
    EYRE_SQUARE_COORD = GPSCoordinate(53.280, -9.062, 0)
    ORIGIN_GPS = GPSCoordinate(47.641468, -122.140165, 122)
    # transormation that maps a GPS position from the microsoft office origin
    # to the Eyre square coordinate
    DELTA_TRANSFORM = EYRE_SQUARE_COORD - ORIGIN_GPS

    # home_position_GPS is the home gps location of the drone in AirSim
    # (close to microsoft headquarters)
    def __init__(self, home_position_GPS: GPSCoordinate):
        print('calculated GPS Delta transform as: {}'.format(RAVGPSMapper.DELTA_TRANSFORM))
        # set home position reference
        self.home_position_GPS = home_position_GPS
        print('Set home position of the RAV as: {}'.format(self.home_position_GPS))
        self.home_position_GPS_Rel = home_position_GPS + RAVGPSMapper.DELTA_TRANSFORM
        print('Set home position relative of the RAV as: {}'.format(self.home_position_GPS_Rel))
        # this gets the delta from the origin to home_position
        # self.home_position_GPS_origin_delta = RAVGPSMapper.EYRE_SQUARE_COORD - RAVGPSMapper.ORIGIN_GPS

    def getMoveToPosXYZFromGPSCoord(self, desired_GPS_position):
        metres_lat = self.home_position_GPS_Rel.get_lat_metres_to_other(desired_GPS_position)
        metres_long = self.home_position_GPS_Rel.get_long_metres_to_other(desired_GPS_position)
        metres_alt = self.home_position_GPS_Rel.get_alt_metres_to_other(desired_GPS_position)
        return (metres_lat, metres_long, -abs(metres_alt))

    def convertGPSToNED(self, current_GPS_position: "somewhere near eyre square",
                        desired_GPS_position: "somewhere near eyre square"):
        print('Converting GPS to NED\n')
        # should validate GPS_position here probably
        GPS_delta = desired_GPS_position - current_GPS_position
        print('GPS delta: {}'.format(GPS_delta))
        # calculate NED coordinates
        metres_lat = current_GPS_position.get_lat_metres_to_other(desired_GPS_position)
        metres_long = current_GPS_position.get_long_metres_to_other(desired_GPS_position)
        metres_alt = current_GPS_position.alt - desired_GPS_position.alt
        print('returning\t metres lat: {}\nmetres long: {}\nmetres alt: {}'.format(metres_lat, metres_long, metres_alt))
        # north, east, down
        return metres_lat, metres_long, metres_alt

    @staticmethod
    def geoPoint_to_GPSCoordinate(geoPoint):
        return GPSCoordinate(geoPoint.latitude, geoPoint.longitude, geoPoint.altitude)
	
    def get_GPS_Pos(self, microsoft_relative_GPS_pos: GPSCoordinate):
        return RAVGPSMapper.geoPoint_to_GPSCoordinate(microsoft_relative_GPS_pos) + RAVGPSMapper.DELTA_TRANSFORM

# quick test
# c = GPSCoordinate(47.6414680480957,-122.14016723632812, 123.49796295166016)

# r = RAVGPSMapper(c)
