from GPSCoordinate import GPSCoordinate

class RAVGPSMapper:
    # this is taken as origin (0,0)
    # EYRE_SQUARE_COORD = GPSCoordinate(53.2745, -9.049, 0)
    # NUIG
    # EYRE_SQUARE_COORD = GPSCoordinate(53.276, -9.057, 0)
    # not quite eyre square, but close enough!
    #HOME_COORD = GPSCoordinate(53.280, -9.062, 0)
    ORIGIN_GPS = GPSCoordinate(47.641468, -122.140165, 122)
    # transormation that maps a GPS position from the microsoft office origin
    # to the Eyre square coordinate
    #DELTA_TRANSFORM = HOME_COORD - ORIGIN_GPS

    # home_position_GPS is the home gps location of the drone in AirSim
    # (close to microsoft headquarters)
    def __init__(self, home_position_GPS: GPSCoordinate = GPSCoordinate(53.280, -9.062)):
        '''Set the home gps coordinate of the rav'''
        self.home_position_GPS = home_position_GPS
        #self.home_position_GPS = GPSCoordinate(53.280, -9.062, 0)
        #print('calculated GPS Delta transform as: {}'.format(RAVGPSMapper.DELTA_TRANSFORM))
        # set home position reference
        #print('Set home position of the RAV as: {}'.format(self.home_position_GPS))
        #self.home_position_GPS_Rel = home_position_GPS + RAVGPSMapper.DELTA_TRANSFORM
        #print('Set home position relative to RAV as: {}'.format(self.home_position_GPS_Rel))
        # this gets the delta from the origin to home_position
        # self.home_position_GPS_origin_delta = RAVGPSMapper.EYRE_SQUARE_COORD - RAVGPSMapper.ORIGIN_GPS
        

    def getMoveToPosXYZFromGPSCoord(self, desired_GPS_position):
        '''Returns the XYZ Unreal Engine NED coordinatee position to move to in order to reach the desired gps position'''
        metres_lat = self.home_position_GPS.get_lat_metres_to_other(desired_GPS_position)
        metres_long = self.home_position_GPS.get_long_metres_to_other(desired_GPS_position)
        metres_alt = self.home_position_GPS.get_alt_metres_to_other(desired_GPS_position)
        
        #check whether the lat/long difference is positive or negative (metres to other methods give abs values)
        if desired_GPS_position.lat < self.home_position_GPS.lat:
            metres_lat =- metres_lat
        if desired_GPS_position.long < self.home_position_GPS.long:
            metres_long =- metres_long
            
        return (metres_lat, metres_long, -abs(metres_alt))


    #@staticmethod
    #def geoPoint_to_GPSCoordinate(geoPoint):
    #    return GPSCoordinate(geoPoint.latitude, geoPoint.longitude, geoPoint.altitude)
    
    def get_GPS_Pos(self, microsoft_relative_GPS_pos: GPSCoordinate):
        '''AirSim calculates GPS position in relation to microsoft headquarters, 
        this gives the GPS position relative to the home coordinate set by the constructor.'''
        #calculate lat, long distance from current position to microsoft home coordinate
        lat_dist = microsoft_relative_GPS_pos.get_lat_metres_to_other(RAVGPSMapper.ORIGIN_GPS)
        lng_dist = microsoft_relative_GPS_pos.get_long_metres_to_other(RAVGPSMapper.ORIGIN_GPS)
        
        if microsoft_relative_GPS_pos.lat < RAVGPSMapper.ORIGIN_GPS.lat:
            lat_dist =- lat_dist
        if microsoft_relative_GPS_pos.long < RAVGPSMapper.ORIGIN_GPS.long:
            lng_dist =- lng_dist
            
        #then add this distance to home coordinate
        #first calculate azimuth (will probably be ok to do this as dealing with small(ish) angles
        bearing =  RAVGPSMapper.ORIGIN_GPS.get_initial_bearing(microsoft_relative_GPS_pos)
        distance = microsoft_relative_GPS_pos.get_metres_to_other(RAVGPSMapper.ORIGIN_GPS)
        destination = GPSCoordinate._vincentyGeodesicDirect(self.home_position_GPS, distance, bearing)
        return destination
        
        #47.641468, -122.140165
        #47.6477308, -122.1321476
        #return RAVGPSMapper.geoPoint_to_GPSCoordinate(microsoft_relative_GPS_pos) + RAVGPSMapper.DELTA_TRANSFORM


