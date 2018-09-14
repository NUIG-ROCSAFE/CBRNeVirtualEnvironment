import math

#This is outdated! Update with reference to java
class GPSCoordinate:
    m1 = 111132.92;
    m2 = -559.82;
    m3 = 1.175;
    m4 = -0.0023;

    p1 = 111412.84;
    p2 = -93.5;
    p3 = 0.118;

    def __init__(self, lat, long, alt):
        self._lat = lat
        self._long = long
        self._alt = alt

    @property
    def lat(self):
        return self._lat

    @lat.setter
    def lat(self, new_lat):
        self._lat = new_lat

    @property
    def long(self):
        return self._long

    @long.setter
    def long(self, new_long):
        self._long = new_long

    @property
    def alt(self):
        return self._alt

    @alt.setter
    def alt(self, new_alt):
        self._alt = new_alt

    def __str__(self):
        return 'Lat: {}\t Long: {}\t Alt: {}'.format(self.lat, self.long, self.alt)

    def __sub__(self, other):
        return GPSCoordinate(self.lat - other.lat, self.long - other.long, self.alt - other.alt)

    def __add__(self, other):
        return GPSCoordinate(self.lat + other.lat, self.long + other.long, self.alt + other.alt)


    def get_lat_metres_to_other(self, otherCoord):
        # delta = self - otherCoord
        print('otherCoord: ', otherCoord)
        return GPSCoordinate.convert_lat_degree_difference_to_metres(self._lat, otherCoord.lat)


    def get_long_metres_to_other(self, otherCoord):
        # delta = self - otherCoord
        return GPSCoordinate.convert_long_degree_difference_to_metres(self.long, otherCoord.long, self.lat)

    def get_alt_metres_to_other(self, other_coord):
        return self.alt - other_coord.alt

    @staticmethod
    def getMetresBetweenPoints(p1: 'GPSCoordinate', p2: "GPSCoordinate") -> float:
        return math.sqrt(math.pow(p1.get_lat_metres_to_other(p2), 2) + math.pow(p1.get_long_metres_to_other(p2), 2))

    @staticmethod
    def convert_lat_degree_difference_to_metres(lat1, lat2) -> float:
        return abs(lat1 - lat2) * GPSCoordinate._getLenMetresOneDegreeLat(lat1)

    @staticmethod
    def convert_long_degree_difference_to_metres(long1, long2, lat) -> float:
        return abs(long1 - long2) * GPSCoordinate._getLenMetresOneDegreeLong(lat);

    @staticmethod
    def _getLenMetresOneDegreeLong(lat):
        lat = math.radians(lat);
        return (GPSCoordinate.p1 * math.cos(lat)) + (GPSCoordinate.p2 * math.cos(3 * lat)) +\
               (GPSCoordinate.p3 * math.cos(5 * lat))

    @staticmethod
    def _getLenMetresOneDegreeLat(lat):
        lat = math.radians(lat)
        return (GPSCoordinate.m1 + (GPSCoordinate.m2 * math.cos(2 * lat)) + (GPSCoordinate.m3 * math.cos(4 * lat)) +
                (GPSCoordinate.m4 * math.cos(6 * lat)))

#
# #run some tests
# GPSCoordinate1 = GPSCoordinate(53.2745, -9.049, 0)
# GPSCoordinate2 = GPSCoordinate(53.2779115341, -9.0597334278, 0)
# print(GPSCoordinate1 - GPSCoordinate2)
# print(GPSCoordinate1.lat)
# #a 1.1 km walk
# print('metres from NUIG to square: {}'.format(GPSCoordinate.getMetresBetweenPoints(GPSCoordinate1, GPSCoordinate2)))
# #metres from NUIG to square: 810.4670076485374