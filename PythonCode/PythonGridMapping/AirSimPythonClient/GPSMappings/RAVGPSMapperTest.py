from RAVGPSMapper import RAVGPSMapper
from GPSCoordinate import GPSCoordinate
import unittest

class TestRAVGPSMapper(unittest.TestCase):

	def setUp(self):
		self.OConnellStreetCoordinate = GPSCoordinate(53.3512416, -6.2629676, 0)
		self.EyreSquareCoordinate = GPSCoordinate(53.2743394, -9.0514163)
		self.NUIGCoordinate = GPSCoordinate(53.2809159, -9.0692133, 20)
		

	def testGetMoveToPosXYZFromGPSCoord(self):
		mapper1 = RAVGPSMapper(self.NUIGCoordinate)
		UECoord1 = mapper1.getMoveToPosXYZFromGPSCoord(self.EyreSquareCoordinate)
		self.assertAlmostEqual(UECoord1[0], -730, delta = 20)
		self.assertAlmostEqual(UECoord1[1], 1183, delta = 20)
		
		#check that signs change
		mapper2 = RAVGPSMapper(self.EyreSquareCoordinate)
		UECoord2 = mapper2.getMoveToPosXYZFromGPSCoord(self.NUIGCoordinate)
		self.assertAlmostEqual(UECoord2[0], 730, delta = 20)
		self.assertAlmostEqual(UECoord2[1], -1183, delta = 20)
		
	def testGet_GPS_Pos(self):
		mapper1 = RAVGPSMapper(self.NUIGCoordinate)
		#pos = mapper1.get_GPS_Pos()
		redmond_campus_coord = GPSCoordinate(47.6477308, -122.1321476)
		#should be 696 m lat, 600 long
		#close enough
		print(mapper1.get_GPS_Pos(redmond_campus_coord))
		
		
		
#		self.assertAlmostEqual(OConnellStreetCoordinate.getMetresBetweenPoints(EyreSquareCoordinate),186270 delta = 5000)
#		self.assertAlmostEqual(NUIGCoordinate.getMetresBetweenPoints(EyreSquareCoordinate),836 delta = 50)