from src import Piece
from src import Square
import string

class Action(object):
	
	def __init__(self, piece, target_square, capture = False, check = False):
		self.piece= piece
		self.target_square= target_square
		self.capture= capture
		self.check= check



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
		