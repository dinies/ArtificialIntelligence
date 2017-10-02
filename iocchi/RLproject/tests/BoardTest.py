import unittest
from context import src
from src import Board
from src import King
from src import Pawn
from src import Square
from src import State



class BoardTest(unittest.TestCase):
	def setUp(self):
		self.board = Board.Board("1k1/ppp/111/111/PPP/1K1")
		self.check_board = Board.Board("111/111/1k1/111/p11/1K1")
		self.checkmate_board= Board.Board("k11/1PP/K11/111/111/111")
		self.simple_capture_board= Board.Board("k11/111/1p1/P11/111/1K1")
		self.stalemate_board= Board.Board("k11/P11/1K1/111/111/111")
		self.last_row_reached_board= Board.Board("k11/111/111/111/111/p1K")
		
	def test_board_constructor(self):
		self.assertEqual(self.board.rows_number, 6)
		self.assertEqual(self.board.columns_number, 3)
		self.assertEqual(len(self.board.squares), 18)
		self.assertEqual(len(self.board.white.pieces),4)
		self.assertEqual(len(self.board.black.pieces),4)
		
		self.assertEqual(len(self.board.white.attacked_squares), 8)
		self.assertEqual(len(self.board.black.attacked_squares), 8)
		self.assertEqual(len(self.board.white.occupied_squares), 4)
		self.assertEqual(len(self.board.black.occupied_squares), 4)

		for i in range(0, 2):
			with self.subTest(i=i):
				self.assertTrue(isinstance(self.board.white.pieces[i] , Pawn.Pawn))
		self.assertTrue(isinstance(self.board.white.pieces[3] , King.King))

		self.assertTrue(isinstance(self.board.black.pieces[0] , King.King))
		
		for j in range(1, 3):
			with self.subTest(i=i):
				self.assertTrue(isinstance(self.board.black.pieces[j] , Pawn.Pawn))


	def test_check_board_constructor(self):
		self.assertEqual(self.check_board.rows_number, 6)
		self.assertEqual(self.board.columns_number, 3)
		self.assertEqual(len(self.check_board.squares), 18)
		self.assertEqual(len(self.check_board.white.pieces),1)
		self.assertEqual(len(self.check_board.black.pieces),2)
	
		self.assertEqual(len(self.check_board.white.attacked_squares), 5)
		self.assertEqual(len(self.check_board.black.attacked_squares), 9)
		self.assertEqual(len(self.check_board.white.occupied_squares), 1)
		self.assertEqual(len(self.check_board.black.occupied_squares), 2)

		self.assertTrue(isinstance(self.check_board.white.pieces[0] , King.King))
		self.assertTrue(isinstance(self.check_board.black.pieces[0] , King.King))
		self.assertTrue(isinstance(self.check_board.black.pieces[1] , Pawn.Pawn))


	def test_1_contains_square(self):
		valid_square_key = "a1"
		self.assertTrue(self.board.contains_square(valid_square_key))


	def test_2_contains_square(self):
		not_valid_square_key= "d4"
		self.assertTrue(not self.board.contains_square(not_valid_square_key))

	def test_is_free_square(self):
		self.assertTrue(self.board.is_free_square( "a1" ))
		self.assertTrue(self.board.is_free_square( "b4" ))
		self.assertFalse(self.board.is_free_square( "b1" ))
		self.assertFalse(self.board.is_free_square( "c5" ))

    
	def test_is_under_check(self):
		self.assertTrue(self.check_board.is_under_check("white"))
		self.assertFalse(self.check_board.is_under_check("black"))

	def test_make_move(self):
		self.board.make_move("b2", "b3")
		self.assertEqual(self.board.__str__(), "1k1/ppp/111/1P1/P1P/1K1" )

	def test_make_white_capture_move(self):
		self.simple_capture_board.make_move("a3", "b4")
		self.assertEqual(self.simple_capture_board.__str__(), "k11/111/1P1/111/111/1K1")

	def test_make_black_capture_move(self):
		self.simple_capture_board.make_move("b4", "a3")
		self.assertEqual(self.simple_capture_board.__str__(), "k11/111/111/p11/111/1K1")

	def test_is_under_checkmate(self):
		state= State.State(self.checkmate_board.__str__())
		self.assertTrue(self.checkmate_board.is_under_checkmate("black",state))
		self.assertFalse(self.checkmate_board.is_under_checkmate("white",state))

	def test_is_under_stalemate(self):
		state= State.State(self.checkmate_board.__str__())
		self.assertTrue(self.stalemate_board.is_under_stalemate("black",state))
		self.assertFalse(self.stalemate_board.is_under_stalemate("white",state))

	def test_last_row_reached_with_pawn(self):
		self.assertTrue(self.last_row_reached_board.last_row_reached_with_pawn("black"))
		self.assertFalse(self.last_row_reached_board.last_row_reached_with_pawn("white"))
		self.assertFalse(self.simple_capture_board.last_row_reached_with_pawn("white"))
		self.assertFalse(self.stalemate_board.last_row_reached_with_pawn("white"))
		self.assertFalse(self.checkmate_board.last_row_reached_with_pawn("black"))


	def test_str__(self):
		self.assertEqual(self.board.__str__(), "1k1/ppp/111/111/PPP/1K1")
		self.assertEqual(self.check_board.__str__(), "111/111/1k1/111/p11/1K1")
		self.assertEqual(self.checkmate_board.__str__(), "k11/1PP/K11/111/111/111")


	def tearDown(self):
		self.board = None
		self.check_board = None
		self.checkmate_board= None
		self.simple_capture_board= None
		self.stalemate_board= None
		self.last_row_reached_board= None

       
if __name__ == '__main__':
	unittest.main()



