class Square(object):
	"""docstring for Square"""
	def __init__(self,  column, row):
		
		self.column = column
		self.row = row
		self.piece= None
	
	def add_piece_to_square(self,piece):
		self.piece= piece

	def remove_piece( self):
		self.piece= None

	def is_occupied(self):
		return  not self.piece == None



	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return  self.column.__eq__(other.column) and self.row == other.row 
		else:
			return False

	def __ne__(self, other):
		return not self.__eq__(other)

	def __hash__(self):
		return hash(self.column) + hash(self.row)

	def __str__(self):
		return self.column + str(self.row)
