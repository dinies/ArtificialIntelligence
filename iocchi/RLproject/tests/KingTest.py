import unittest
from context import src
from src import Board
from src import King
from src import Square



class KingTest(unittest.TestCase):
    def setUp(self):
        self.initial_board = Board.Board("1k1/ppp/111/111/PPP/1K1")
        self.king1= self.initial_board.white.pieces[3]

        self.started_board = Board.Board("111/111/1k1/1K1/111/111")
        self.king2= self.started_board.white.pieces[0]


    def test_add_square(self):
        king = King.King("black")
        square= Square.Square("b", 2)
        king.add_square(square)
        self.assertEqual(king.square, square)

    @unittest.skip("TODO")
    def test_1_reachable_squares(self):
        square_list= self.king1.reachable_squares()
        true_list= [ Square.Square("a", 1),Square.Square("c", 1)]

  
    @unittest.skip("TODO")
    def test_2_reachable_squares(self):
        square_list= self.king2.reachable_squares()
        true_list= [ 
            Square.Square("a", 2),
            Square.Square("b", 2),
            Square.Square("c", 2),
            Square.Square("a", 3),
            Square.Square("c", 3),
            Square.Square("a", 4),
            Square.Square("c", 4)
            ]
     

    def test_initial_white_attacked_squares(self):
        square_list= self.king1.attacked_squares(self.initial_board)
        true_list= [ 
            Square.Square("b", 2),
            Square.Square("a", 2),
            Square.Square("a", 1),
            Square.Square("c", 2),
            Square.Square("c", 1),

            ]
        self.assertEqual(square_list, true_list)
                
    

    def test_started_white_squares(self):
        square_list= self.king2.attacked_squares(self.started_board)
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


    def test_str__(self):
        self.assertEqual(self.king1.__str__(), "K") 



    def tearDown(self):
        self.initial_board = None
        self.king1 = None
        self.started_board = None
        self.king2 = None


if __name__ == '__main__':
    unittest.main()

