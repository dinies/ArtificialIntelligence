import unittest
from context import src
from src import Action
from src import Square
from src import King

class ActionTest(unittest.TestCase):
	def setUp(self):
		piece= King.King("white")
		s = Square.Square("a", 2)
		piece.add_square(s)
		target_square1 = Square.Square("a", 3)
		target_square2 = Square.Square("a", 1)
		self.action1= Action.Action(piece,target_square1)
		self.action2= Action.Action(piece,target_square2)
		self.action3= Action.Action(piece,target_square2, capture = True)
		self.action4= Action.Action(piece,target_square2, check = True)

	def test_eq__(self):
		self.assertFalse(self.action1.__eq__(self.action2))

	def test_str__(self):
		self.assertEqual( self.action1.__str__() , "K.a2-a3")
		self.assertEqual( self.action2.__str__() , "K.a2-a1")

		self.assertEqual( self.action3.__str__() , "K.a2xa1")
		self.assertEqual( self.action4.__str__() , "K.a2-a1+")


	def tearDown(self):
		self.action1= None
		self.action2= None
		self.action3= None
		self.action4= None

if __name__ == '__main__':
    unittest.main()