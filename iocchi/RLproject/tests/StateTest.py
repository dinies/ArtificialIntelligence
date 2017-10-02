import unittest
from context import src
from src import State
from src import Action
from src import Square
from src import King
from src import Pawn
import pdb

class StateTest(unittest.TestCase):
	def setUp(self):
		self.initial_state= State.State("1k1/ppp/111/111/PPP/1K1")
		self.final_state_checkmate= State.State("k11/1PP/K11/111/111/111")
		self.final_state_stalemate= State.State("k11/P11/1K1/111/111/111")
		self.final_state_pawn_in_last_row= State.State("11P/111/1k1/111/1K1/111")
		self.reduced_state=State.State("k11/11P/KP1")

	def test_discard_not_admissible_actions(self):

		state_str="11k/11P/111/111/1pP/K11"

		white_king= King.King("white")
		K_pos = Square.Square("a", 1)
		white_king.add_square(K_pos)
		target_square_K= Square.Square("b", 2)
		admissible_action= Action.Action(white_king,target_square_K, capture=True)


		white_pawn=Pawn.Pawn("white")
		P_pos = Square.Square("c",2)
		white_pawn.add_square(P_pos)
		target_square_P=Square.Square("c",3)
		not_admissible_action= Action.Action(white_pawn,target_square_P)

		input_possible_action= {
		"P.c2-c3": not_admissible_action,
		"K.a1xb2": admissible_action
		}

		true_admissible_action= {
		"K.a1xb2": admissible_action
		}
		state= State.State("11k/11P/111/111/1pP/K11")
		result= state.discard_not_admissible_actions(input_possible_action,"white")

		self.assertEqual(result, true_admissible_action)




	def test_execute_action(self):
		piece= King.King("black")
		from_s= Square.Square("b", 1)
		piece.add_square(from_s)
		to_s = Square.Square("a", 1)
		action= Action.Action(piece,to_s)
		true_next_board_state= "1k1/ppp/111/111/PPP/K11"
		self.assertEqual(self.initial_state.execute_action(action), true_next_board_state)


	def test_get_reward_win(self):
		self.assertEqual( 100, self.final_state_checkmate.get_reward("white"))
		self.assertEqual( 100, self.final_state_pawn_in_last_row.get_reward("white"))

	def test_get_reward_lose(self):
		self.assertEqual( -100, self.final_state_checkmate.get_reward("black"))
		self.assertEqual( -100, self.final_state_pawn_in_last_row.get_reward("black"))


	def test_get_reward_stalemate(self):
		self.assertEqual( -5, self.final_state_stalemate.get_reward("white"))
		self.assertEqual( -5, self.final_state_stalemate.get_reward("black"))

	
	def test_is_losing_state_for_agent_stalemate(self):
		self.assertTrue( self.final_state_stalemate.is_losing_state_for_agent("black"))
		self.assertFalse( self.final_state_stalemate.is_losing_state_for_agent("white"))	
	

	def test_is_losing_state_for_agent_pawn_in_last_row(self):
		self.assertTrue( self.final_state_pawn_in_last_row.is_losing_state_for_agent("black"))
		self.assertFalse( self.final_state_pawn_in_last_row.is_losing_state_for_agent("white"))

	def test_is_losing_state_for_agent_checkmate(self):
		self.assertTrue( self.final_state_checkmate.is_losing_state_for_agent("black"))
		self.assertFalse( self.final_state_checkmate.is_losing_state_for_agent("white"))

	def test_is_losing_state_for_agent_reduced(self):
		self.assertFalse( self.reduced_state.is_losing_state_for_agent("white"))
		self.assertTrue( self.reduced_state.is_losing_state_for_agent("black"))



	def tearDown(self):
		self.initial_state= None
		self.final_state_checkmate= None
		self.final_state_stalemate= None
		self.final_state_pawn_in_last_row= None


if __name__ == '__main__':
    unittest.main()
