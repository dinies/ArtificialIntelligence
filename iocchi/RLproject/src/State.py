import Board

class State(object):
	"""docstring for State"""
	def __init__(self, board_state):
		self.board= Board.Board(board_state)
		self.winner= None  #maybe useless

	def is_final_state(self, agent_color):
		#the game ends when a pawn reach the last row or one kings is put in checkmate or stalemate
		return true

	def possible_actions(self, agent_color = "white"):
		if agent_color == "white" :
			self.board.white.compute_possible_actions()
			return self.board.white.possible_actions
		else :
			self.board.black.compute_possible_actions()
			return self.board.black.possible_actions


