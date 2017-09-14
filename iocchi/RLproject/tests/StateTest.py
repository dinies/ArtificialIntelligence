import unittest
from context import src
from src import State

class StateTest(unittest.TestCase):
	def setUp(self):
		self.final_state_checkmate= State.State("k11/1PP/K11/111/111/111")
		self.final_state_stalemate= State.State("k11/P11/1K1/111/111/111")
		self.final_state_pawn_in_last_row= State.State("11K/111/1k1/111/1K1/111")

	def test_is_final_state_stalemate(self):
		self.assertTrue( self.final_state_stalemate.is_final_state())

	def test_is_final_state_pawn_in_last_row(self):
		self.assertTrue( self.final_state_pawn_in_last_row.is_final_state())

	def test_is_final_state_checkmate(self):
		self.assertTrue( self.final_state_checkmate.is_final_state())

	def tearDown(self):
		self.final_state_stalemate= None
		self.final_state_pawn_in_last_row= None