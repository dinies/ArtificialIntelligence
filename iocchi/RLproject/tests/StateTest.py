import unittest
from context import src
from src import State
from src import Action
from src import Square
from src import King

class StateTest(unittest.TestCase):
	def setUp(self):
		self.initial_state= State.State("1k1/ppp/111/111/PPP/1K1")
		self.final_state_checkmate= State.State("k11/1PP/K11/111/111/111")
		self.final_state_stalemate= State.State("k11/P11/1K1/111/111/111")
		self.final_state_pawn_in_last_row= State.State("11P/111/1k1/111/1K1/111")


	def test_execute_action(self):
		piece= King.King("black")
		from_s= Square.Square("b", 1)
		piece.add_square(from_s)
		to_s = Square.Square("a", 1)
		action= Action.Action(piece,to_s)
		true_next_board_state= "1k1/ppp/111/111/PPP/K11"
		self.assertEqual(self.initial_state.execute_action(action), true_next_board_state)

	def test_is_final_state_stalemate(self):
		self.assertTrue( self.final_state_stalemate.is_final_state())	

	def test_is_final_state_pawn_in_last_row(self):
		self.assertTrue( self.final_state_pawn_in_last_row.is_final_state())
	
	def test_is_final_state_checkmate(self):
		self.assertTrue( self.final_state_checkmate.is_final_state())

	def tearDown(self):
		self.initial_state= None
		self.final_state_checkmate= None
		self.final_state_stalemate= None
		self.final_state_pawn_in_last_row= None


if __name__ == '__main__':
    unittest.main()
