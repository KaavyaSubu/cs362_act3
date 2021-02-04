import unittest
import calc_fxns




class TestCase(unittest.TestCase):

	def addtest1(self):
		self.assertEqual(add(9,10),19)
	def addtest2(self):
		self.assertEqual(add(-3.5,3.5),0)
	def addtest3(self):
		self.assertEqual(add(5,15.6),20.6)
	
	def subtest1(self):
		self.assertEqual(subtract(9,10),-1)
	def subtest2(self):
		self.assertEqual(subtract(-3.5,3.5),-7)
	def subtest3(self):
		self.assertEqual(subtract(5,15.6),-10.6)

	def multest1(self):
		self.assertEqual(multiply(9,10),90)
	def multest2(self):
		self.assertEqual(multiply(-3.5,3.5),-12.25)
	def subtest3(self):
		self.assertEqual(multiply(5,15.6),78)
	
	def divtest1(self):
		self.assertEqual(divide(9,10),90)
	def divtest2(self):
		self.assertEqual(divide(-3.5,3.5),-1)
	def divtest3(self):
		self.assertEqual(divide(5,10),0.5)
	def divtest4(self):
		self.assertRaises(DividByZero,divide(5,0))

if __name__ == '__main__':
	unittest.main()


