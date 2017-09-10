from src import Square
from src import Piece
from src import Agent
from src import Pawn
from src import King

import string

class Board(object):
	"""docstring for Board"""
	def __init__(self, board_state):

		self.squares= {}
		self.pieces= []
		self.white = Agent.Agent("white", self)
		self.black = Agent.Agent("black", self)
		self.rows_number=0
		self.check_rows_number(board_state)
		self.parse_board_state(board_state)
		
	def check_rows_number(self, board_state_string):
		rows= board_state_string.split('/')
		self.rows_number= len(rows[0])


	def parse_board_state(self, board_state_string):
		rows= board_state_string.split('/')
		row_index=len(rows)
		for row in rows:
			self.parse_row(row, row_index)
			row_index-=1


	def parse_row(self, row_string, row_index):
		"""example of row   1k1   ppp    111   111    PPP  1K1 """
		column_index=0
		column_keys=  string.ascii_lowercase[:len(list(row_string))]
		for c in row_string:
			if self.parse_int(c) == -1:
				square= Square.Square(column_keys[column_index], row_index)
				piece= self.create_piece(c,square)
				square.add_piece_to_square(piece)
				dict_key= column_keys[column_index] + str(row_index)
				self.squares[ dict_key ]= square
				column_index+=1

			else:
				s= Square.Square(column_keys[column_index],row_index)
				dict_key= column_keys[column_index] + str(row_index)
				self.squares[ dict_key ]= s
				column_index +=1

	def contains_square(self, square_key):
		return square_key in self.squares.keys()


				
	def create_piece(self, char, square):
		if char.isupper() :
			arg= "white"
			char= char.lower() 
		else:
			arg= "black"

		
		if char == "p" :
			piece= Pawn.Pawn(arg)
		else:
			piece= King.King(arg)

		piece.add_square(square)

		if arg == "white":
			self.white.add_piece_to_agent(piece)
		else:
			self.black.add_piece_to_agent(piece)
		return piece

	def parse_int(self,s):
		try:
			return int(s)
		except ValueError:
			return -1






