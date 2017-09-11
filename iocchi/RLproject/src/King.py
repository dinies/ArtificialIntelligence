from src import Piece
from src import Action
import string


class King(Piece.Piece):
	"""docstring for King"""
	def __init__(self, color):
		super().__init__(color)
		

	def get_reachable_squares(self, board):
		reac_squares= []
		square_keys= self.get_around_squares_keys(board)
		for s_key in square_keys:
			if  board.contains_square(s_key) and board.is_free_square(s_key):
				reac_squares.append( board.squares[s_key] )
		return reac_squares

	def get_possible_actions(self,board):
		action_list= []
	
		#serch all reachable squares
			#which is also not attacked from enemy pieces is good
		reachable_squares= self.get_reachable_squares(board)
		not_attacked_reac_squares= []
		for s in reachable_squares:
			if self.color == "white":
				if not s in board.black.attacked_squares:
					not_attacked_reac_squares.append(s)
			else:
				if not s in board.white.attacked_squares:
					not_attacked_reac_squares.append(s)

		#search all the captures = attacked squares in which there is an enemy piece
			# from these find only squares that are not attacked by enemy pieces
		attacked_squares = self.get_attacked_squares(board)
		capture_squares= []
		for  s in attacked_squares:
			if self.color == "white" :
				if  not board.is_free_square(s.__str__()) and  s in board.black.occupied_squares and not s in board.black.attacked_squares:
					capture_squares.append(s)
			else:
				if not board.is_free_square(s.__str__()) and s in board.white.occupied_squares and not s in board.white.attacked_squares:
					capture_squares.append(s)


		for s in not_attacked_reac_squares:
			action= Action.Action( self, s )
			action_list.append(action)


		for s in capture_squares:
			action= Action.Action( self, s , capture= True )
			action_list.append(action)

		return action_list




	def get_around_squares_keys(self, board):
		square_keys= []
		column_keys=  string.ascii_lowercase[:board.columns_number]

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

		return square_keys

	def get_attacked_squares(self,board):
		att_squares= []
		
		square_keys = self.get_around_squares_keys(board)
		for s_key in square_keys:
			if board.contains_square(s_key):
				att_squares.append(board.squares.get(s_key))
		return att_squares
		
	def __str__(self):
		if self.color == "white":
			return "K"
		else:
			return "k"
