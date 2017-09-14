import Board

class State(object):
	"""docstring for State"""
	def __init__(self, board_state):
		self.board= Board.Board(board_state)
		self.winner= None  #maybe useless

	def is_final_state(self, agent_color):
		#check all the squares in the stating rows for enemy pawns
		#after that ask board if white or black are under checkmate or stalemate
		#the game ends when a pawn reach the last row or one kings is put in checkmate or stalemate
		return true
	def get_winner(self):


	def possible_actions(self, agent_color = "white"):
		if agent_color == "white" :
			self.board.white.compute_possible_actions()
			return self.board.white.possible_actions
		else :
			self.board.black.compute_possible_actions()
			return self.board.black.possible_actions


