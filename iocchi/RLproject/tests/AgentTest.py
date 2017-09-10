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
		self.minimal_board =  Board.Board("111/111/111/111/1P1/11K")
		self.initial_board =  Board.Board("1k1/ppp/111/111/PPP/1K1")
		self.capture_board =  Board.Board("k11/111/pKp/1P1/111/111")
		self.minimal_agent= self.minimal_board.white
		self.initial_agent= self.initial_board.white
		self.capture_agent= self.capture_board.white


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

		true_list = [ act_1, act_2 , act_3]

		action_list= self.minimal_board.white.compute_possible_actions()

		self.assertEqual( true_list, action_list)


if __name__ == '__main__':
	unittest.main()