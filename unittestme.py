import unittest
from Testy import NetTest

class TestMe(unittest.TestCase):
	def test_it(self):
		self.assertAlmostEqual(NetTest(5), 50)
		self.assertAlmostEqual(NetTest(1), 10)
		self.assertAlmostEqual(NetTest(0), 0)
		self.assertAlmostEqual(NetTest(0), 0)
		#this last test will cause failure for obvs

if __name__ == '__main__':
    unittest.main()
