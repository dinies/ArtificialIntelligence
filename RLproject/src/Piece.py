from abc import ABC, abstractmethod

class Piece(ABC):

	def __init__(self, color):
		self.color= color
		self.square= None



	def add_square(self, square):
		self.square = square
	
	def remove_from_board(self,board):
		if self.color== "white":
			board.white.remove_captured_piece(self)
		else:
			board.black.remove_captured_piece(self)
			
		self.square.remove_piece()
		self.square= None

	@abstractmethod
	def get_reachable_squares(self):
		pass

	@abstractmethod
	def get_possible_actions(self,board):
		pass

	@abstractmethod
	def get_attacked_squares(self,board):
		pass



	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.__dict__ == other.__dict__
		else:
			return False

	def __ne__(self, other):
		return not self.__eq__(other)

	def __hash__(self):
		return hash(self.__dict__.values())

	@abstractmethod
	def __str__(self):
		pass