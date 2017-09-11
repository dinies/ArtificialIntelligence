import unittest
from context import src
from src import Board
from src import King
from src import Square
from src import Action



class KingTest(unittest.TestCase):
    def setUp(self):
        self.initial_board = Board.Board("1k1/ppp/111/111/PPP/1K1")
        self.initial_king= self.initial_board.white.pieces[3]

        self.started_board = Board.Board("111/111/1k1/1K1/111/111")
        self.started_king= self.started_board.white.pieces[0]

        self.check_board = Board.Board("111/111/1k1/111/p11/1K1")
        self.check_white_king = self.check_board.white.pieces[0]
        self.check_black_king = self.check_board.black.pieces[0]

        self.king_capture_board= Board.Board("P1P/PkP/111/111/1p1/pKp")
        self.white_king_capture= self.king_capture_board.white.pieces[4]
        self.black_king_capture= self.king_capture_board.black.pieces[0]




    def test_add_square(self):
        king = King.King("black")
        square= Square.Square("b", 2)
        king.add_square(square)
        self.assertEqual(king.square, square)

    def test_initial_get_reachable_squares(self):
        square_list= self.initial_king.get_reachable_squares(self.initial_board)
        true_list= [ Square.Square("a", 1),Square.Square("c", 1)]

  
    def test_started_get_reachable_squares(self):
        square_list= self.started_king.get_reachable_squares(self.started_board)
        true_list= [ 
            Square.Square("a", 2),
            Square.Square("b", 2),
            Square.Square("c", 2),
            Square.Square("a", 3),
            Square.Square("c", 3),
            Square.Square("a", 4),
            Square.Square("c", 4)
            ]
     

    def test_white_king_capture_possible_actions(self):
        self.assertTrue(isinstance(self.white_king_capture, King.King))
        piece= King.King("white")
        s = Square.Square("b", 1)
        piece.add_square(s)

        target_square_1 = Square.Square("a", 2)
        action_1= Action.Action(piece,target_square_1)

        target_square_2 = Square.Square("c", 2)
        action_2= Action.Action(piece,target_square_2)

        target_square_3 = Square.Square("b", 2)
        action_3= Action.Action(piece,target_square_3, capture=True)

        actions_list=self.white_king_capture.get_possible_actions(self.king_capture_board)
        self.assertEqual(actions_list, [action_1, action_2, action_3])



    def test_black_king_capture_possible_actions(self):
        self.assertTrue(isinstance(self.black_king_capture, King.King))
        piece= King.King("black")
        s = Square.Square("b", 5)
        piece.add_square(s)

        target_square_1 = Square.Square("b", 4)
        action_1= Action.Action(piece,target_square_1)

        target_square_2 = Square.Square("a", 4)
        action_2= Action.Action(piece,target_square_2)

        target_square_3 = Square.Square("c", 4)
        action_3= Action.Action(piece,target_square_3)
        
        target_square_4 = Square.Square("a", 6)
        action_4= Action.Action(piece,target_square_4, capture= True)

        target_square_5 = Square.Square("a", 5)
        action_5= Action.Action(piece,target_square_5, capture= True)

        target_square_6 = Square.Square("c", 6)
        action_6= Action.Action(piece,target_square_6, capture= True)

        target_square_7 = Square.Square("c", 5)
        action_7= Action.Action(piece,target_square_7, capture= True)

        true_actions= [
            action_1,
            action_2,
            action_3,
            action_4,
            action_5,
            action_6,
            action_7
            ]

        actions_list=self.black_king_capture.get_possible_actions(self.king_capture_board)
        self.assertEqual(actions_list, true_actions)


    def test_initial_white_get_attacked_squares(self):
        square_list= self.initial_king.get_attacked_squares(self.initial_board)
        true_list= [ 
            Square.Square("b", 2),
            Square.Square("a", 2),
            Square.Square("a", 1),
            Square.Square("c", 2),
            Square.Square("c", 1),

            ]
        self.assertEqual(square_list, true_list)
                
    

    def test_started_white_get_attacked_squares(self):
        square_list= self.started_king.get_attacked_squares(self.started_board)
        true_list= [ 
            Square.Square("b", 4),
            Square.Square("b", 2),
            Square.Square("a", 4),
            Square.Square("a", 3),
            Square.Square("a", 2),
            Square.Square("c", 4),
            Square.Square("c", 3),
            Square.Square("c", 2)
            ]

        self.assertEqual(square_list, true_list)


    def test_check_white_king_get_attacked_squares(self):
        square_list= self.check_white_king.get_attacked_squares(self.check_board)
        true_list= [ 
            Square.Square("b", 2),
            Square.Square("a", 2),
            Square.Square("a", 1),
            Square.Square("c", 2),
            Square.Square("c", 1)
            ]

        self.assertEqual(square_list, true_list)



    def test_check_black_king_get_attacked_squares(self):
        square_list= self.check_black_king.get_attacked_squares(self.check_board)
        true_list= [ 
            Square.Square("b", 5),
            Square.Square("b", 3),
            Square.Square("a", 5),
            Square.Square("a", 4),
            Square.Square("a", 3),
            Square.Square("c", 5),
            Square.Square("c", 4),
            Square.Square("c", 3)
            ]

        self.assertEqual(square_list, true_list)


    def test_str__(self):
        self.assertEqual(self.initial_king.__str__(), "K") 



    def tearDown(self):
        self.initial_board = None
        self.initial_king = None
        self.started_board = None
        self.started_king = None
        self.check_board = None
        self.check_white_king = None
        self.check_black_king = None


if __name__ == '__main__':
    unittest.main()

