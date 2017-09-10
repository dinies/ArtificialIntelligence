from src import Piece
import string

class Pawn(Piece.Piece):
	"""docstring for Pawn"""
	def __init__(self, color):
		super().__init__(color)
		

	def reachable_squares(self):
		return []

	def get_possible_actions(self,board):
		#search for reachable squares   ___ if they are empty then this is valid action


		#search for attacked squares  ____ if they are occupied by an enemy piece different from the king then they can capture
		
		#ask the board if the enemy king is put under check or chekmate
		# create action accordingly and add to action_list to return
		pass
		
	def attacked_squares(self, board):
		att_squares= []
		column_keys=  string.ascii_lowercase[:board.rows_number]
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









	 