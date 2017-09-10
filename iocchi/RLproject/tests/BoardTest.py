import unittest
from context import src
from src import Board
from src import King
from src import Pawn
from src import Square



class BoardTest(unittest.TestCase):
	def setUp(self):
		self.board = Board.Board("1k1/ppp/111/111/PPP/1K1")


	def test_board_constructor(self):
		self.assertEqual(self.board.rows_number, 3)
		self.assertEqual(len( self.board.squares), 18)
		self.assertEqual(len(self.board.white.pieces),4)
		self.assertEqual(len(self.board.black.pieces),4)


		for i in range(0, 2):
			with self.subTest(i=i):
				self.assertTrue(isinstance(self.board.white.pieces[i] , Pawn.Pawn))
		self.assertTrue(isinstance(self.board.white.pieces[3] , King.King))

		self.assertTrue(isinstance(self.board.black.pieces[0] , King.King))
		
		for j in range(1, 3):
			with self.subTest(i=i):
				self.assertTrue(isinstance(self.board.black.pieces[j] , Pawn.Pawn))

	def test_1_contains_square(self):
		valid_square_key = "a1"
		self.assertTrue(self.board.contains_square(valid_square_key))


	def test_2_contains_square(self):
		not_valid_square_key= "d4"
		self.assertTrue(not self.board.contains_square(not_valid_square_key))


	def tearDown(self):
		self.board = None

if __name__ == '__main__':
	unittest.main()



