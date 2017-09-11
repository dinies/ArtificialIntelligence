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
		self.columns_number=0
		self.check_columns_number(board_state)
		self.rows_number = 0
		self.check_rows_number(board_state)
		self.parse_board_state(board_state)
		self.white.compute_attacked_squares()
		self.black.compute_attacked_squares()
		
	def check_columns_number(self, board_state_string):
		rows= board_state_string.split('/')
		self.columns_number= len(rows[0])

	def check_rows_number(self, board_state_string):
		rows= board_state_string.split('/')
		self.rows_number= len(rows)


	def parse_board_state(self, board_state_string):
		rows= board_state_string.split('/')
		row_index=len(rows)
		for row in rows:
			self.parse_row(row, row_index)
			row_index-=1


	def parse_row(self, row_string, row_index):
		column_index=0
		column_keys=  string.ascii_lowercase[:len(list(row_string))]
		for c in row_string:
			if self.parse_int(c) == -1:
				square= Square.Square(column_keys[column_index], row_index)
				dict_key= column_keys[column_index] + str(row_index)
				self.squares[ dict_key ]= square
				piece= self.create_piece(c,square)
				square.add_piece_to_square(piece)
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

	def is_free_square(self, square_key):
		square = self.squares[square_key]
		return square.piece == None


	def is_under_check(self, agent_color):
		if agent_color == "white":
			for piece in self.white.pieces:
				if isinstance(piece, King.King):
					agent_king= piece
			agent_king_square= agent_king.square
			enemy_attacked_squares= self.black.attacked_squares
		else:
			for piece in self.black.pieces:
				if isinstance(piece, King.King):
					agent_king= piece
			agent_king_square= agent_king.square
			enemy_attacked_squares= self.white.attacked_squares	
		return agent_king_square in enemy_attacked_squares


	def make_move(self, square_from_key, square_to_key):
		square_from = self.squares[square_from_key]
		moving_piece= square_from.piece
		square_from.piece= None
		square_to= self.squares[square_to_key]

		if not self.is_free_square(square_to_key):
			captured_piece= square_to.piece
			captured_piece.remove_from_board(self)
		square_to.add_piece_to_square(moving_piece)
		moving_piece.square = square_to
		self.white.compute_attacked_squares()
		self.black.compute_attacked_squares()



	def is_under_checkmate(self, agent_color):
		if agent_color == "white":
			for piece in self.white.pieces:
				if isinstance(piece, King.King):
					agent_king= piece
			return self.is_under_check("white") and len( agent_king.get_possible_actions(self) ) == 0
		else:
			for piece in self.black.pieces:
				if isinstance(piece, King.King):
					agent_king= piece
			return self.is_under_check("black") and len( agent_king.get_possible_actions(self) ) == 0
		
	
	def is_under_stalemate(self, agent_color):
		if agent_color == "white":
			for piece in self.white.pieces:
				if isinstance(piece, King.King):
					agent_king= piece
			return not self.is_under_check("white") and len( agent_king.get_possible_actions(self) ) == 0
		else:
			for piece in self.black.pieces:
				if isinstance(piece, King.King):
					agent_king= piece
			return not self.is_under_check("black") and len( agent_king.get_possible_actions(self) ) == 0
		


	def parse_int(self,s):
		try:
			return int(s)
		except ValueError:
			return -1


	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.__dict__ == other.__dict__
		else:
			return False

	def __ne__(self, other):
		return not self.__eq__(other)

	def __hash__(self):
		return hash(self.__dict__.values())


	def __str__(self):
		inv_parsing_list= list(self.squares.keys())
		board_state_string= ""
		col_count= 0
		row_count= 1
		while len(inv_parsing_list) > 0 :
			s_key= inv_parsing_list.pop(0)
			col_count += 1
			square = self.squares[s_key]
			if square.is_occupied() :
				char= square.piece.__str__()
			else:
				char= str(1)
			board_state_string = board_state_string + char
			if col_count >= 3 :
				col_count =0
				row_count +=1
				if row_count <= self.rows_number :
					board_state_string= board_state_string + "/"


		return board_state_string




