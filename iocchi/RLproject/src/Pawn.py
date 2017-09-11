from src import Piece
import string
from src import Action
from src import Board

class Pawn(Piece.Piece):
	"""docstring for Pawn"""
	def __init__(self, color):
		super().__init__(color)
		

	def get_reachable_squares(self,board):
		reac_squares= []
		column = self.square.column
		row = self.square.row
		if self.color == "white" :
			row_index= row + 1
			
		else: 
			row_index= row - 1

		s_key= column + str(row_index)
		if board.is_free_square(s_key):
			reac_squares.append( board.squares[s_key] )
		return reac_squares

	def get_possible_actions(self,board):
		action_list=[]

		#search for reachable squares   ___ if they are empty (and indeed they are) then this is valid action
		reachable_squares = self.get_reachable_squares(board)

		#search for attacked squares  ____ if they are occupied by an enemy piece they can capture
		attacked_squares = self.get_attacked_squares(board)
		capture_squares= []
		for  s in attacked_squares:
			if self.color == "white" :
				if  not board.is_free_square(s.__str__()) and  s in board.black.occupied_squares:
					capture_squares.append(s)
			else:
				if not board.is_free_square(s.__str__()) and s in board.white.occupied_squares:
					capture_squares.append(s)
		for s in reachable_squares:

			board_state= board.__str__()
			next_board= Board.Board(board_state)
			actual_square_key= self.square.__str__()
			next_board.make_move(actual_square_key, s.__str__())
			
			if self.color == "white":
				if next_board.is_under_check("black"):
					action= Action.Action( self, s , check= True)
				else:
					action= Action.Action( self, s )
			else:
				if next_board.is_under_check("white"):
					action= Action.Action( self, s , check= True)
				else:
					action= Action.Action( self, s )
			action_list.append(action)
		for s in capture_squares:

			board_state= board.__str__()
			next_board= Board.Board(board_state)
			actual_square_key= self.square.__str__()
			next_board.make_move(actual_square_key, s.__str__())
			

			if self.color == "white":
				if next_board.is_under_check("black"):
					action= Action.Action( self, s , capture= True, check= True)
				else:
					action= Action.Action( self, s , capture= True )
			else:
				if next_board.is_under_check("white"):
					action= Action.Action( self, s , capture= True , check= True)
				else:
					action= Action.Action( self, s , capture= True)
			action_list.append(action)

		return action_list

	def get_attacked_squares(self, board):
		att_squares= []
		column_keys=  string.ascii_lowercase[:board.columns_number]
		column = self.square.column
		row = self.square.row
		col_index= column_keys.index(column)

		if self.color == "white":
			row_index= row + 1 
			if col_index != 0 :
				upper_left_s_key= column_keys[col_index - 1] + str(row_index)
				if board.contains_square(upper_left_s_key):
					att_squares.append(board.squares.get(upper_left_s_key))
			if col_index != len(column_keys) -1 :
				upper_right_s_key= column_keys[col_index + 1] + str(row_index)
				if board.contains_square(upper_right_s_key):
					att_squares.append(board.squares.get(upper_right_s_key))

		else:
			row_index= row - 1
			if col_index != 0 :
				lower_left_s_key= column_keys[col_index - 1] + str(row_index)
				if board.contains_square(lower_left_s_key):
					att_squares.append(board.squares.get(lower_left_s_key))
			if col_index != len(column_keys) - 1 :
				lower_right_s_key= column_keys[col_index + 1] + str(row_index)
				if board.contains_square(lower_right_s_key):
					att_squares.append(board.squares.get(lower_right_s_key))
		return  att_squares




	def __str__(self):
		if self.color == "white":
			return "P"
		else:
			return "p"









	 