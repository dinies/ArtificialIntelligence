import unittest
from context import src
from src import Action
from src import Square
from src import King
from src import Board

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


	def test_parse_action_1_string(self):

		board_1 = Board.Board("1k1/ppp/111/111/KPP/111")
		new_action_1= Action.Action(action_string="K.a2-a3", board= board_1)
		self.assertEqual( new_action_1, self.action1)
		
		
	def test_parse_action_2_string(self):
		board_2= Board.Board("1k1/ppp/111/111/KPP/111")
		new_action_2= Action.Action(action_string="K.a2-a1",board= board_2)
		self.assertEqual( new_action_2, self.action2)
		
		
	def test_parse_action_3_string(self):
		board_3= Board.Board("1k1/ppp/111/111/KPP/p11")
		new_action_3= Action.Action(action_string="K.a2xa1",board= board_3)
		self.assertEqual( new_action_3, self.action3)
		
	def test_parse_action_4_string(self):
		board_4= Board.Board("111/ppp/111/111/KPP/1k1")
		new_action_4= Action.Action(action_string="K.a2-a1+", board= board_4)
		self.assertEqual( new_action_4, self.action4)
		


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