from src import Piece
from src import Square
import string

class Action(object):
	
	def __init__(self, piece= None, target_square= None, capture = False, check = False, action_string= None ,board= None):
		if action_string == None and board == None:
			self.piece= piece
			self.target_square= target_square
			self.capture= capture
			self.check= check
		else:
			self.parse_action_string(action_string, board)


	def parse_action_string( self, action_string, board):
		letters= list(action_string)
		from_square_key = letters[2]+letters[3]
		to_square_key = letters[5]+letters[6]
		self.piece= board.squares[from_square_key].piece
		self.target_square= board.squares[to_square_key]
		self.capture= letters[4] == "x"
		self.check= len(letters) == 8


		

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
		if self.capture:
			sign_1= "x"
		else:
			sign_1= "-"

		if self.check :
			sign_2 = "+"
		else:
			sign_2 = ""


		return self.piece.__str__() +"."+ self.piece.square.__str__() + sign_1 + self.target_square.__str__() + sign_2
		