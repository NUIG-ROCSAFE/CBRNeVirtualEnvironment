import math
from collections import namedtuple

#theses are just structs
WGS84Ellipsoid = namedtuple("WGS84Ellipsoid", "WGSa WGSb WGSf")
WebMercator = namedtuple("WebMercator", "m1 m2 m3 m4 p1 p2 p3")
#This is outdated! Update with reference to java
class GPSCoordinate:
    #m1 = 111132.92;
    #m2 = -559.82;
    #m3 = 1.175;
    #m4 = -0.0023;

    #p1 = 111412.84;
    #p2 = -93.5;
    #p3 = 0.118;
    
    #semi-major axis
    #WGSa = 6378137.0;
    #semi-minor axis
    #WGSb = 6356752.314245;
    #reciprocal of flattening
    #WGSf = 1 / 298.257223563;
    
    TwoPi = 2.0 * math.pi;
    Ellipsoid = WGS84Ellipsoid(6378137.0, 6356752.314245, 1 / 298.257223563)
    WebMercatorProjection = WebMercator(111132.92, -559.82, 1.175, -0.0023, 111412.84, -93.5, 0.118)
    
    def __init__(self, lat, long, alt = 0):
        '''by default set the altitude to 0 (i.e. the point is on the earths surface'''
        self._lat = lat
        self._long = long
        self._alt = alt
        
    @staticmethod
    def _vincentyGeodesicDirect(coord, distance, initialBearing):
        '''Given a gps coordinate, a desired distance(m) and an initial bearing, returns 
        the GPS coordinate that is the desired distance and bearing away from coord'''
        Phi1 = math.radians(coord.lat)
        Lambda1 = math.radians(coord.long);
        Alpha1 = math.radians(initialBearing);
        s = distance;

        a = GPSCoordinate.Ellipsoid.WGSa;
        b = GPSCoordinate.Ellipsoid.WGSb;
        f = GPSCoordinate.Ellipsoid.WGSf;

        sinAlpha1 = math.sin(Alpha1);
        cosAlpha1 = math.cos(Alpha1);

        tanU1 = (1-f) * math.tan(Phi1)
        cosU1 = 1 / math.sqrt((1 + tanU1*tanU1))
        sinU1 = tanU1 * cosU1;
        Sigma1 = math.atan2(tanU1, cosAlpha1);
        sinAlpha = cosU1 * sinAlpha1;
        cosSqAlpha = 1 - sinAlpha*sinAlpha;
        uSq = cosSqAlpha * (a*a - b*b) / (b*b);
        A = 1 + uSq/16384*(4096+uSq*(-768+uSq*(320-175*uSq)));
        B = uSq/1024 * (256+uSq*(-128+uSq*(74-47*uSq)));

         #cos2SigmaM, sinSigma, cosSigma, DeltaSigma;

        Sigma = s / (b*A)
        iterations = 0;
        
        #hacked do while
        cos2SigmaM = math.cos(2*Sigma1 + Sigma);
        sinSigma = math.sin(Sigma);
        cosSigma = math.cos(Sigma);
        DeltaSigma = B*sinSigma*(cos2SigmaM+B/4*(cosSigma*(-1+2*cos2SigmaM*cos2SigmaM)-B/6*cos2SigmaM*(-3+4*sinSigma*sinSigma)*(-3+4*cos2SigmaM*cos2SigmaM)));
        SigmaPrime = Sigma;
        Sigma = s / (b*A) + DeltaSigma;
        
        while (abs(Sigma-SigmaPrime) > 1e-12 and ++iterations<100):
            cos2SigmaM = math.cos(2*Sigma1 + Sigma);
            sinSigma = math.sin(Sigma);
            cosSigma = math.cos(Sigma);
            DeltaSigma = B*sinSigma*(cos2SigmaM+B/4*(cosSigma*(-1+2*cos2SigmaM*cos2SigmaM)-B/6*cos2SigmaM*(-3+4*sinSigma*sinSigma)*(-3+4*cos2SigmaM*cos2SigmaM)));
            SigmaPrime = Sigma;
            Sigma = s / (b*A) + DeltaSigma;
        
        if (iterations >= 100):
            raise Exception("Formula failed to converge"); #not possible!

        x = sinU1*sinSigma - cosU1*cosSigma*cosAlpha1;
        Phi2 = math.atan2(sinU1*cosSigma + cosU1*sinSigma*cosAlpha1, (1-f)*math.sqrt(sinAlpha*sinAlpha + x*x));
        Lambda = math.atan2(sinSigma*sinAlpha1, cosU1*cosSigma - sinU1*sinSigma*cosAlpha1);
        C = f/16*cosSqAlpha*(4+f*(4-3*cosSqAlpha));
        L = Lambda - (1-C) * f * sinAlpha * (Sigma + C*sinSigma*(cos2SigmaM+C*cosSigma*(-1+2*cos2SigmaM*cos2SigmaM)));
        Lambda2 = (Lambda1+L+3*math.pi)%(2*math.pi) - math.pi;  # normalise to -180..+180

        Alpha2 = math.atan2(sinAlpha, -x);
        Alpha2 = (Alpha2 + 2*math.pi) % (2*math.pi); # normalise to 0..360

        return GPSCoordinate(math.degrees(Phi2), math.degrees(Lambda2), coord.alt);
        
        
    @staticmethod
    def _vincentyGeodesicInverse(from_coord, to_coord):
        '''Given from and to gps coordinates, calculates the distance (m) between them'''
        
        a = GPSCoordinate.Ellipsoid.WGSa
        b = GPSCoordinate.Ellipsoid.WGSb
        f = GPSCoordinate.Ellipsoid.WGSf
        
        phiOne = math.radians(from_coord.lat);
        phiTwo = math.radians(to_coord.lat);

        lambdaOne = math.radians(from_coord.long);
        lambdaTwo = math.radians(to_coord.long);
        
        L = lambdaTwo - lambdaOne;
        
        tanU1 = (1-f) * math.tan(phiOne);
        cosU1 = 1 / math.sqrt((1 + tanU1*tanU1));
        sinU1 = tanU1 * cosU1;
        
        tanU2 = (1-f) * math.tan(phiTwo);
        cosU2 = 1 / math.sqrt((1 + tanU2*tanU2));
        sinU2 = tanU2 * cosU2;

        sinSigma=0;
        cosSigma=0;
        Sigma=0;
        cosSqAlpha=0;
        cos2SigmaM=0;
        

        Lambda = L
        iterations = 0;
        
        antimeridian = abs(L) > math.pi;
        
        #first of do while
        break_do_while = False
        sinLambda = math.sin(Lambda);
        cosLambda = math.cos(Lambda);
        sinSqSigma = (cosU2*sinLambda) * (cosU2*sinLambda) + (cosU1*sinU2-sinU1*cosU2*cosLambda) * (cosU1*sinU2-sinU1*cosU2*cosLambda);
        if (sinSqSigma == 0):
            if (iterations >= 1000):
                raise Exception("Formula failed to converge");
            uSq = cosSqAlpha * (a*a - b*b) / (b*b);
            A = 1 + uSq/16384*(4096+uSq*(-768+uSq*(320-175*uSq)));
            B = uSq/1024 * (256+uSq*(-128+uSq*(74-47*uSq)));
            DeltaSigma = B*sinSigma*(cos2SigmaM+B/4*(cosSigma*(-1+2*cos2SigmaM*cos2SigmaM)-B/6*cos2SigmaM*(-3+4*sinSigma*sinSigma)*(-3+4*cos2SigmaM*cos2SigmaM)));
            s = b*A*(Sigma-DeltaSigma);
            return s
            
        sinSigma = math.sqrt(sinSqSigma);
        cosSigma = sinU1*sinU2 + cosU1*cosU2*cosLambda;
        Sigma = math.atan2(sinSigma, cosSigma);
        sinAlpha = cosU1 * cosU2 * sinLambda / sinSigma;
        cosSqAlpha = 1 - sinAlpha*sinAlpha;
        cos2SigmaM = cosSigma - 2*sinU1*sinU2/cosSqAlpha if cosSqAlpha != 0 else 0
        #(cosSqAlpha != 0) ? (cosSigma - 2*sinU1*sinU2/cosSqAlpha) : 0; // equatorial line: cosSqAlpha=0 (S6)
        
        C = f/16*cosSqAlpha*(4+f*(4-3*cosSqAlpha));
        LambdaPrime = Lambda;
        Lambda = L + (1-C) * f * sinAlpha * (Sigma + C*sinSigma*(cos2SigmaM+C*cosSigma*(-1+2*cos2SigmaM*cos2SigmaM)));
        iterationCheck = abs(Lambda)-math.pi if antimeridian else abs(Lambda)
        #antimeridian ? abs(Lambda)-math.pi : abs(Lambda);
        if (iterationCheck > math.pi):
            raise Exception("Lambda > pi after " + iterations + " iterations.");
        
        while (abs(Lambda-LambdaPrime) > 1e-12 and ++iterations<1000):
            sinLambda = math.sin(Lambda);
            cosLambda = math.cos(Lambda);
            sinSqSigma = (cosU2*sinLambda) * (cosU2*sinLambda) + (cosU1*sinU2-sinU1*cosU2*cosLambda) * (cosU1*sinU2-sinU1*cosU2*cosLambda);
            if (sinSqSigma == 0):
                break; # co-incident points
            sinSigma = math.sqrt(sinSqSigma);
            cosSigma = sinU1*sinU2 + cosU1*cosU2*cosLambda;
            Sigma = math.atan2(sinSigma, cosSigma);
            sinAlpha = cosU1 * cosU2 * sinLambda / sinSigma;
            cosSqAlpha = 1 - sinAlpha*sinAlpha;
            cos2SigmaM = cosSigma - 2*sinU1*sinU2/cosSqAlpha if cosSqAlpha != 0 else 0
            #(cosSqAlpha != 0) ? (cosSigma - 2*sinU1*sinU2/cosSqAlpha) : 0; 
            # equatorial line: cosSqAlpha=0 (S6)
            C = f/16*cosSqAlpha*(4+f*(4-3*cosSqAlpha));
            LambdaPrime = Lambda;
            Lambda = L + (1-C) * f * sinAlpha * (Sigma + C*sinSigma*(cos2SigmaM+C*cosSigma*(-1+2*cos2SigmaM*cos2SigmaM)));
            iterationCheck = abs(Lambda)-math.pi if antimeridian else abs(Lambda)
            #antimeridian ? abs(Lambda)-math.pi : abs(Lambda);
            #System.out.println("iterationCheck: " + iterationCheck);
            if (iterationCheck > math.pi):
                raise Exception("Lambda > pi after " + iterations + " iterations.");
            
        
        
        if (iterations >= 1000):
            raise Exception("Formula failed to converge");

        uSq = cosSqAlpha * (a*a - b*b) / (b*b);
        A = 1 + uSq/16384*(4096+uSq*(-768+uSq*(320-175*uSq)));
        B = uSq/1024 * (256+uSq*(-128+uSq*(74-47*uSq)));
        DeltaSigma = B*sinSigma*(cos2SigmaM+B/4*(cosSigma*(-1+2*cos2SigmaM*cos2SigmaM)-
                B/6*cos2SigmaM*(-3+4*sinSigma*sinSigma)*(-3+4*cos2SigmaM*cos2SigmaM)));

        s = b*A*(Sigma-DeltaSigma);
        return s;
        
    def get_initial_bearing(self, end_coordinate):
        '''Returns the initial bearing, which if followed in a straight line along a great-circle
        arc will take you from the start point to the end point'''
        y = math.sin(end_coordinate.long - self.long) * math.cos(end_coordinate.lat)
        x = math.cos(self.lat) * math.sin(end_coordinate.lat) - (math.sin(self.lat) * math.cos(end_coordinate.lat) * math.cos(end_coordinate.long - self.long))
        bearing = math.atan2(y,x)
        return (math.degrees(bearing) + 360) % 360
        
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

    def get_metres_to_other(self, otherCoord):
        return GPSCoordinate._vincentyGeodesicInverse(self, otherCoord)
        
    def get_lat_metres_to_other(self, otherCoord):
        # delta = self - otherCoord
        return GPSCoordinate._vincentyGeodesicInverse(self, GPSCoordinate(otherCoord.lat,self.long))
        


    def get_long_metres_to_other(self, otherCoord):
        # delta = self - otherCoord
        #return GPSCoordinate.convert_long_degree_difference_to_metres(self.long, otherCoord.long, self.lat)
        return GPSCoordinate._vincentyGeodesicInverse(self, GPSCoordinate(self.lat,otherCoord.long))

    def get_alt_metres_to_other(self, other_coord):
        return self.alt - other_coord.alt

#    @staticmethod
#    def getMetresBetweenPoints(p1: 'GPSCoordinate', p2: "GPSCoordinate") -> float:
#        return math.sqrt(math.pow(p1.get_lat_metres_to_other(p2), 2) + math.pow(p1.get_long_metres_to_other(p2), 2))

    @staticmethod
    def getMetresBetweenPoints(p1: 'GPSCoordinate', p2: "GPSCoordinate") -> float:
        return GPSCoordinate._vincentyGeodesicInverse(p1, p2)
        
    #@staticmethod
    #def convert_lat_degree_difference_to_metres(lat1, lat2) -> float:
    #    return abs(lat1 - lat2) * GPSCoordinate._getLenMetresOneDegreeLat(lat1)

    #@staticmethod
    #def convert_long_degree_difference_to_metres(long1, long2, lat) -> float:
    #    return abs(long1 - long2) * GPSCoordinate._getLenMetresOneDegreeLong(lat);

    #@staticmethod
    #def _getLenMetresOneDegreeLong(lat):
    #    lat = math.radians(lat);
    #    return (GPSCoordinate.WebMercatorProjection.p1 * math.cos(lat)) + (GPSCoordinate.WebMercatorProjection.p2 * math.cos(3 * lat)) +\
    #           (GPSCoordinate.WebMercatorProjection.p3 * math.cos(5 * lat))

    #@staticmethod
    #def _getLenMetresOneDegreeLat(lat):
    #    lat = math.radians(lat)
    #    return (GPSCoordinate.WebMercatorProjection.m1 + (GPSCoordinate.WebMercatorProjection.m2 * math.cos(2 * lat)) + (GPSCoordinate.WebMercatorProjection.m3 * math.cos(4 * lat)) +
    #            (GPSCoordinate.WebMercatorProjection.m4 * math.cos(6 * lat)))

#
# #run some tests
if __name__ == '__main__':
    GPSCoordinate1 = GPSCoordinate(53.2745, -9.049, 0)
    GPSCoordinate2 = GPSCoordinate(53.2779115341, -9.0597334278, 0)
    print(GPSCoordinate1 - GPSCoordinate2)
    print(GPSCoordinate1.lat)    # #a 1.1 km walk
    print('metres from NUIG to square: {}'.format(GPSCoordinate.getMetresBetweenPoints(GPSCoordinate1, GPSCoordinate2)))
# #metres from NUIG to square: 810.4670076485374