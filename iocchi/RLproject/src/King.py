from src import Piece
import string


class King(Piece.Piece):
	"""docstring for King"""
	def __init__(self, color):
		super().__init__(color)
		

	def reachable_squares(self):
		return []


	def get_possible_actions(self,board):
		pass


	def attacked_squares(self,board):
		att_squares= []
		square_keys= []
		column_keys=  string.ascii_lowercase[:board.rows_number]

		column = self.square.column
		row = self.square.row
		col_index= column_keys.index(column)
		
		square_keys.append( column + str(row + 1) )
		square_keys.append( column + str(row - 1) )
		
		#no_left_edge
		if col_index!= 0:
			square_keys.append( column_keys[col_index - 1] + str(row + 1))
			square_keys.append( column_keys[col_index - 1] + str(row ))
			square_keys.append( column_keys[col_index - 1] + str(row - 1))
		#no_right_edge
		if col_index!= len(column_keys) - 1 :
			square_keys.append( column_keys[col_index + 1] + str(row + 1))
			square_keys.append( column_keys[col_index + 1] + str(row ))
			square_keys.append( column_keys[col_index + 1] + str(row - 1))

		for s_key in square_keys:
			if board.contains_square(s_key):
				att_squares.append(board.squares.get(s_key))
		return att_squares
		
	def __str__(self):
		if self.color == "white":
			return "K"
		else:
			return "k"
