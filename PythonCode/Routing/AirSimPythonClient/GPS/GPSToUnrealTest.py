#stdlib imports 
import unittest
import sys
sys.path.append('..')

#3rd party imports

#user defined imports
from GPSToUnreal import GPSToUnreal
from GPSCoordinate import GPSCoordinate

class TestGPSToUnreal(unittest.TestCase):

	def setUp(self):
		self.OConnellStreetCoordinate = GPSCoordinate(53.3512416, -6.2629676, 0)
		self.EyreSquareCoordinate = GPSCoordinate(53.2743394, -9.0514163)
		self.NUIGCoordinate = GPSCoordinate(53.2809159, -9.0692133, 20)
		

	def testGetMoveToPosXYZFromGPSCoord(self):
		mapper1 = GPSToUnreal(self.NUIGCoordinate)
		UECoord1 = mapper1.getMoveToPosXYZFromGPSCoord(self.EyreSquareCoordinate)
		#nuig coordinate to eyre square coordinate
		self.assertAlmostEqual(UECoord1[0], -731.3, delta = 10)
		self.assertAlmostEqual(UECoord1[1], 1183, delta = 20)
		
		#check that signs change
		mapper2 = GPSToUnreal(self.EyreSquareCoordinate)
		UECoord2 = mapper2.getMoveToPosXYZFromGPSCoord(self.NUIGCoordinate)
		self.assertAlmostEqual(UECoord2[0], 730, delta = 20)
		self.assertAlmostEqual(UECoord2[1], -1183, delta = 20)
		
		nuigRectCoord1 = GPSCoordinate(53.2787637762, -9.0634679794)
		nuigRectCoord2 = GPSCoordinate(53.2787637762, -9.0601420403)
		nuigRectCoord3 = GPSCoordinate(53.2810987761, -9.0601420403)
		nuigRectCoord4 = GPSCoordinate(53.2810987761, -9.0634679794)
		
		mapper3 = GPSToUnreal(GPSCoordinate(53.280, -9.062, 0))
		rect_coords = [nuigRectCoord1, nuigRectCoord2, nuigRectCoord3, nuigRectCoord4]
		for coord in rect_coords:
			print(mapper1.getMoveToPosXYZFromGPSCoord(coord))
		
	def testGet_GPS_Pos(self):
		mapper1 = GPSToUnreal(self.NUIGCoordinate)
		#pos = mapper1.get_GPS_Pos()
		redmond_campus_coord = GPSCoordinate(47.6477308, -122.1321476)
		#should be 696 m lat, 600 long
		#close enough
		print(mapper1.get_GPS_Pos(redmond_campus_coord))
		
		
		
#		self.assertAlmostEqual(OConnellStreetCoordinate.getMetresBetweenPoints(EyreSquareCoordinate),186270 delta = 5000)
#		self.assertAlmostEqual(NUIGCoordinate.getMetresBetweenPoints(EyreSquareCoordinate),836 delta = 50)