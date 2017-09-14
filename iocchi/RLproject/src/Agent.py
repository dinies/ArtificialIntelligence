class Agent(object):
	"""docstring for Agent"""
	def __init__(self,color,board):
		self.color= color
		self.board= board
		self.pieces= []
		self.possible_actions= {}
		self.occupied_squares= []
		self.reachable_squares= []
		self.attacked_squares= []

	


	def add_piece_to_agent(self, piece):
		self.pieces.append(piece)
		self.occupied_squares.append(piece.square)
		


	def compute_attacked_squares(self):
		for piece in self.pieces:
			att_squares= piece.get_attacked_squares(self.board)
			for square in att_squares:
				if square not in self.attacked_squares:
					self.attacked_squares.append(square)

	def compute_possible_actions(self):
		for piece in self.pieces :
			possible_actions= piece.get_possible_actions(self.board)
			for action in possible_actions:
				self.possible_actions[ action.__str__() ]= action
			
	def remove_captured_piece(self, piece):
		piece_square = piece.square
		self.pieces.remove(piece)
		self.occupied_squares.remove(piece_square)

		



	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.color == other.color and self.pieces.__eq__(other.pieces) and self.attacked_squares.__eq__(other.attacked_squares)
		else:
			return False

	def __ne__(self, other):
		return not self.__eq__(other)

	def __hash__(self):
		return hash(self.color) + hash( self.pieces) + hash( self.attacked_squares )
