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
		attacked_squares= piece.attacked_squares(self.board)
		for square in attacked_squares:
			if square not in self.attacked_squares:
				self.attacked_squares.append(square)

	def compute_possible_actions(self):
		for piece in self.pieces :
			# compute all the possible movements

			possible_actions= piece.get_possible_actions(self.board)
			for action in possible_actions:
				self.possible_actions[ action.__str__() ]= action
			


		



	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.__dict__ == other.__dict__
		else:
			return False

	def __ne__(self, other):
		return not self.__eq__(other)

	def __hash__(self):
		return hash(self.__dict__.values())
