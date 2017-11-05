import unittest
from context import src
from src import Board
from src import Agent
from src import Action
from src import Pawn
from src import King
from src import Square

class AgentTest(unittest.TestCase):
	def setUp(self):
		self.minimal_board =  Board.Board("1k1/111/111/111/1P1/11K")
		self.initial_board =  Board.Board("1k1/ppp/111/111/PPP/1K1")
		# self.capture_board =  Board.Board("k11/111/pKp/1P1/111/111")
		self.reduced_board =  Board.Board("k11/11P/KP1")



	def test_compute_possible_actions_white_minimal_board(self):

		king = King.King("white")
		pawn = Pawn.Pawn("white")
		s_c1= Square.Square("c", 1)
		s_b1= Square.Square("b", 1)
		s_c2= Square.Square("c", 2)
		s_b2= Square.Square("b", 2)
		s_b3= Square.Square("b", 3)

		king.add_square(s_c1)
		pawn.add_square(s_b2)

		act_1= Action.Action( king , s_b1)
		act_2= Action.Action( king , s_c2)
		act_3= Action.Action( pawn , s_b3)

		true_dict = { 
			act_1.__str__() : act_1,
			act_2.__str__() : act_2,
			act_3.__str__() : act_3
			}

		action_dict= self.minimal_board.white.compute_possible_actions()

		self.assertEqual( true_dict, action_dict)

	def test_compute_possible_actions_black_minimal_board(self):

		king = King.King("black")
		s_a6= Square.Square("a", 6)
		s_b6= Square.Square("b", 6)
		s_c6= Square.Square("c", 6)
		s_a5= Square.Square("a", 5)
		s_b5= Square.Square("b", 5)
		s_c5= Square.Square("c", 5)

		king.add_square(s_b6)

		act_1= Action.Action( king , s_a6)
		act_2= Action.Action( king , s_c6)
		act_3= Action.Action( king , s_a5)
		act_4= Action.Action( king , s_b5)
		act_5= Action.Action( king , s_c5)


		true_dict = { 
			act_1.__str__() : act_1,
			act_2.__str__() : act_2,
			act_3.__str__() : act_3,
			act_4.__str__() : act_4,
			act_5.__str__() : act_5
			}

		action_dict= self.minimal_board.black.compute_possible_actions()

		self.assertEqual( true_dict, action_dict)

	def test_compute_possible_actions_white_reduced_board(self):
		king = King.King("white")
		pawn_1 = Pawn.Pawn("white")
		pawn_2 = Pawn.Pawn("white")
		
		s_b1= Square.Square("b", 1)
		s_b2= Square.Square("b", 2)
		s_c2= Square.Square("c", 2)
		s_c3= Square.Square("c", 3)

		pawn_1.add_square(s_b1)
		pawn_2.add_square(s_c2)

		act_1= Action.Action( pawn_1 , s_b2 , check=True)
		act_2= Action.Action( pawn_2 , s_c3)

		true_dict = { 
			act_1.__str__() : act_1,
			act_2.__str__() : act_2,
			}

		action_dict= self.reduced_board.white.compute_possible_actions()

		self.assertEqual( true_dict, action_dict)


	def test_compute_possible_actions_black_reduced_board(self):
		true_dict = {}

		action_dict= self.reduced_board.black.compute_possible_actions()

		self.assertEqual( true_dict, action_dict)

	def test_compute_possible_actions_white_initial_board(self):

		king = King.King("white")
		pawn_a = Pawn.Pawn("white")
		pawn_b = Pawn.Pawn("white")
		pawn_c = Pawn.Pawn("white")


		s_a1= Square.Square("a", 1)
		s_b1= Square.Square("b", 1)
		s_c1= Square.Square("c", 1)
		s_a2= Square.Square("a", 2)
		s_b2= Square.Square("b", 2)
		s_c2= Square.Square("c", 2)
		s_a3= Square.Square("a", 3)
		s_b3= Square.Square("b", 3)
		s_c3= Square.Square("c", 3)

		king.add_square(s_b1)
		pawn_a.add_square(s_a2)
		pawn_b.add_square(s_b2)
		pawn_c.add_square(s_c2)


		act_1= Action.Action( king , s_a1)
		act_2= Action.Action( king , s_c1)
		act_3= Action.Action( pawn_a , s_a3)
		act_4= Action.Action( pawn_b , s_b3)
		act_5= Action.Action( pawn_c , s_c3)


		true_dict = { 
			act_1.__str__() : act_1,
			act_2.__str__() : act_2,
			act_3.__str__() : act_3,
			act_4.__str__() : act_4,
			act_5.__str__() : act_5

			}

		action_dict= self.initial_board.white.compute_possible_actions()

		self.assertEqual( true_dict, action_dict)


	def test_compute_possible_actions_black_initial_board(self):

		king = King.King("black")
		pawn_a = Pawn.Pawn("black")
		pawn_b = Pawn.Pawn("black")
		pawn_c = Pawn.Pawn("black")


		s_a6= Square.Square("a", 6)
		s_b6= Square.Square("b", 6)
		s_c6= Square.Square("c", 6)
		s_a5= Square.Square("a", 5)
		s_b5= Square.Square("b", 5)
		s_c5= Square.Square("c", 5)
		s_a4= Square.Square("a", 4)
		s_b4= Square.Square("b", 4)
		s_c4= Square.Square("c", 4)

		king.add_square(s_b6)
		pawn_a.add_square(s_a5)
		pawn_b.add_square(s_b5)
		pawn_c.add_square(s_c5)


		act_1= Action.Action( king , s_a6)
		act_2= Action.Action( king , s_c6)
		act_3= Action.Action( pawn_a , s_a4)
		act_4= Action.Action( pawn_b , s_b4)
		act_5= Action.Action( pawn_c , s_c4)


		true_dict = { 
			act_1.__str__() : act_1,
			act_2.__str__() : act_2,
			act_3.__str__() : act_3,
			act_4.__str__() : act_4,
			act_5.__str__() : act_5

			}

		action_dict= self.initial_board.black.compute_possible_actions()

		self.assertEqual( true_dict, action_dict)



if __name__ == '__main__':
	unittest.main()