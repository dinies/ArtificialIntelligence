import unittest
from context import src 
from src import Square
from src import Pawn


class SquareTest(unittest.TestCase):
	def setUp(self):
		self.square1= Square.Square("a",1)
		self.square2= Square.Square("a",1)
		self.square3= Square.Square("b",1)
		self.square4= Square.Square("b",1)

	def test_is_occupied(self):
		piece= Pawn.Pawn("white")
		self.square1.piece= piece
		self.assertTrue( self.square1.is_occupied())
		self.assertFalse( self.square2.is_occupied())

	def test_eq__(self):
		self.assertEqual( self.square1, self.square2)
		self.assertNotEqual( self.square1, self.square3)
		self.assertNotEqual( self.square2, self.square3)
		self.assertNotEqual( self.square2, self.square4)

	def test_hash__(self):
		self.assertEqual( self.square1.__hash__ , self.square2.__hash__)
		self.assertNotEqual( self.square1.__hash__ , self.square3.__hash__)
		self.assertNotEqual( self.square2.__hash__ , self.square3.__hash__)
		self.assertNotEqual( self.square2.__hash__ , self.square4.__hash__)


	def test_str__(self):
		self.assertEqual( "a1" , self.square1.__str__())
		self.assertEqual( "b1" , self.square3.__str__())

	
	def tearDown(self):
		self.square1= None
		self.square2= None
		self.square3= None
		self.square4= None


if __name__ == '__main__':
    unittest.main()