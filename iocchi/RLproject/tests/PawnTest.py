import unittest
from context import src
from src import Board
from src import Pawn
from src import Square
from src import Action



class PawnTest(unittest.TestCase):
    def setUp(self):
        self.initial_board = Board.Board("1k1/ppp/111/111/PPP/1K1")
        self.initial_white_pawn= self.initial_board.white.pieces[1]
        self.initial_black_pawn = self.initial_board.black.pieces[1]
        self.capture_check_board = Board.Board("111/111/1k1/1p1/P11/1K1")
        self.capture_check_white_pawn = self.capture_check_board.white.pieces[0]
        self.capture_check_black_pawn = self.capture_check_board.black.pieces[1]
        self.checkmate_board= Board.Board("k11/11P/KP1/111/111/111")
        self.checkmate_white_pawn = self.checkmate_board.white.pieces[2]

    def test_add_square(self):
        pawn = Pawn.Pawn("white")
        square= Square.Square("b", 2)
        pawn.add_square(square)
        self.assertEqual(pawn.square, square)

    def test_initial_white_reachable_squares(self):
        square_list= self.initial_white_pawn.reachable_squares()
        true_list= [ Square.Square("b", 3)]
        self.assertEqual(square_list, true_list)

    def test_initial_black_reachable_squares(self):
        square_list= self.initial_black_pawn.reachable_squares()
        true_list= [ Square.Square("a", 4)]
        self.assertEqual(square_list, true_list)

    def test_initial_get_white_possible_actions(self):
        self.assertTrue(isinstance(self.initial_white_pawn, Pawn.Pawn))
        piece= Pawn.Pawn("white")
        s = Square.Square("b", 2)
        piece.add_square(s)
        target_square = Square.Square("b", 3)
        action= Action.Action(piece,target_square)
        actions_list=self.initial_white_pawn.get_possible_actions(self.initial_board)
        self.assertEqual(actions_list, [action])

    def test_initial_get_black_possible_actions(self):
        self.assertTrue(isinstance(self.initial_black_pawn, Pawn.Pawn))
        piece= Pawn.Pawn("black")
        s = Square.Square("a", 5)
        piece.add_square(s)
        target_square = Square.Square("a", 4)
        action= Action.Action(piece,target_square)
        actions_list= self.initial_black_pawn.get_possible_actions(self.initial_board)
        self.assertEqual(actions_list, [action])



    def test_capture_check_get_white_possible_actions(self):
        self.assertTrue(isinstance(self.capture_check_white_pawn, Pawn.Pawn))
        piece= Pawn.Pawn("white")
        s = Square.Square("a", 2)
        piece.add_square(s)
        target_square_1 = Square.Square("b", 3)
        target_square_2 = Square.Square("a", 3)
        action1= Action.Action(piece,target_square_1, capture= True)
        action2= Action.Action(piece,target_square_2, check= True)
        actions_list= self.capture_check_white_pawn.get_possible_actions(self.capture_check_board)
        self.assertEqual(actions_list, [action2 , action1])


    def test_capture_check_get_black_possible_actions(self):
        self.assertTrue(isinstance(self.capture_check_black_pawn, Pawn.Pawn))
        piece= Pawn.Pawn("black")
        s = Square.Square("b", 3)
        piece.add_square(s)
        target_square_1 = Square.Square("a", 2)
        target_square_2 = Square.Square("b", 2)
        action1= Action.Action(piece,target_square_1,capture= True, check= True)
        action2= Action.Action(piece,target_square_2)
        actions_list = self.capture_check_black_pawn.get_possible_actions(self.capture_check_board)
        self.assertEqual(actions_list, [action2, action1])


    def test_checkmate_get_white_possible_actions(self):
        self.assertTrue(isinstance(self.checkmate_white_pawn, Pawn.Pawn))
        piece= Pawn.Pawn("white")
        s = Square.Square("b", 4)
        piece.add_square(s)
        target_square = Square.Square("b", 5)
        action= Action.Action(piece,target_square, check= True, checkmate= True)
        actions_list = self.checkmate_white_pawn.get_possible_actions(self.checkmate_board)
        self.assertEqual(actions_list, [action])



    def test_initial_white_attacked_squares_central(self):
        self.assertTrue(isinstance(self.initial_white_pawn, Pawn.Pawn))
        square_list= self.initial_white_pawn.attacked_squares(self.initial_board)
        true_list= [ Square.Square("a", 3), Square.Square("c", 3)]
        self.assertEqual(square_list, true_list)

    def test_initial_black_attacked_squares_on_edge(self):
        self.assertTrue(isinstance(self.initial_black_pawn, Pawn.Pawn))
        square_list= self.initial_black_pawn.attacked_squares(self.initial_board)
        true_list= [ Square.Square("b", 4)]
        self.assertEqual(square_list, true_list)

    def test_str__(self):
        self.assertEqual(self.initial_white_pawn.__str__(), "P") 

    def tearDown(self):
        self.initial_board = None
        self.white_pawn = None

if __name__ == '__main__':
    unittest.main()



