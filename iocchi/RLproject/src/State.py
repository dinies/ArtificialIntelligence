from src import Board

class State(object):
	"""docstring for State"""
	def __init__(self, board_state):
		self.board= Board.Board(board_state)
		self.winner= None  #maybe useless

	def is_final_state(self):
		
		finished= False
		if self.board.last_row_reached_with_pawn("white") or self.board.last_row_reached_with_pawn("black"):
			finished= True
		if self.board.is_under_checkmate("white") or self.board.is_under_checkmate("black"):
			finished= True
		if self.board.is_under_stalemate("white") or self.board.is_under_stalemate("black"):
			finished= True
		return finished
	def get_winner(self):
		pass

	def possible_actions(self, agent_color = "white"):
		if agent_color == "white" :
			self.board.white.compute_possible_actions()
			return self.board.white.possible_actions
		else :
			self.board.black.compute_possible_actions()
			return self.board.black.possible_actions


	def get_reward(self, agent_color):
		if self.board.is_under_stalemate("black") or self.board.is_under_stalemate("white"):
			return -5
		else:
			if self.board.last_row_reached_with_pawn("white") or self.board.is_under_checkmate("black"):
				if agent_color== "white":
					return 100
				else:
					return -100
			if self.board.last_row_reached_with_pawn("black") or self.board.is_under_checkmate("white"):
				if agent_color== "white":
					return -100
				else:
					return 100

	


	def execute_action(self, action):
		
		board_state= self.board.__str__()
		next_board= Board.Board(board_state)
		from_square_key= action.piece.square.__str__()
		to_square_key= action.target_square.__str__()
		next_board.make_move(from_square_key,to_square_key)

		return next_board.__str__()

		
	def __str__(self):
		return self.board.__str__()

	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.__str__() == other.__str__()
		else:
			return False

	def __ne__(self, other):
		return not self.__eq__(other)

	def __hash__(self):
		return hash(self.__str__())

