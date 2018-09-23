from GPSCoordinate import GPSCoordinate
import unittest

class TestTTTBoard(unittest.TestCase):

	def setUp(self):
		self.OConnellStreetCoordinate = GPSCoordinate(53.3512416, -6.2629676, 0)
		self.EyreSquareCoordinate = GPSCoordinate(53.2743394, -9.0514163)
		self.NUIGCoordinate = GPSCoordinate(53.2809159, -9.0692133, 20)

	def testLatLongAlt(self):
		self.assertEqual(self.OConnellStreetCoordinate.lat, 53.3512416)
		self.assertEqual(self.EyreSquareCoordinate.long, -9.0514163)
		self.assertEqual(self.NUIGCoordinate.alt, 20)
		
	def testGetMetresBetweenPoints(self):
		self.assertAlmostEqual(GPSCoordinate.getMetresBetweenPoints(self.OConnellStreetCoordinate, self.EyreSquareCoordinate),185629, delta = 5000)
		self.assertAlmostEqual(GPSCoordinate.getMetresBetweenPoints(self.EyreSquareCoordinate, self.NUIGCoordinate),1394 , delta = 50)
		
	def testGetInitialBearing(self):
		#taken from https://www.movable-type.co.uk/scripts/latlong.html
		osaka = GPSCoordinate(35, 135)
		baghdad = GPSCoordinate(35, 45)
		self.assertAlmostEqual(osaka.get_initial_bearing(baghdad), 60, delta = 5)
		self.assertAlmostEqual(baghdad.get_initial_bearing(osaka), 360-60, delta = 5)