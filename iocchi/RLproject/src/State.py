from src import Board
import pdb

class State(object):
	"""docstring for State"""
	def __init__(self, board_state):
		self.board= Board.Board(board_state)
		self.winner= None  #maybe useless

	def is_losing_state_for_agent(self,agent_color):
		if agent_color=="white":
			opponent_color= "black"
		else:
			opponent_color="white"
		return  self.board.last_row_reached_with_pawn(opponent_color) or self.board.is_under_checkmate(agent_color,self) or self.board.is_under_stalemate(agent_color,self)
	

	def get_winner(self):
		pass

	def possible_actions(self, agent_color):
		if agent_color == "white" :
			self.board.white.compute_possible_actions()
			return self.discard_not_admissible_actions( self.board.white.possible_actions , "white")
		else :
			self.board.black.compute_possible_actions()
			return self.discard_not_admissible_actions( self.board.black.possible_actions , "black")


	def get_reward(self, agent_color):
		if self.board.is_under_stalemate("black",self) or self.board.is_under_stalemate("white",self):
			return -5
		else:
			if self.board.last_row_reached_with_pawn("white") or self.board.is_under_checkmate("black",self):
				if agent_color== "white":
					return 100
				else:
					return -100
			if self.board.last_row_reached_with_pawn("black") or self.board.is_under_checkmate("white",self):
				if agent_color== "white":
					return -100
				else:
					return 100

	
	def discard_not_admissible_actions(self, possible_actions, agent_color):
		admissible_actions= {}

		for key in possible_actions.keys():
			action= possible_actions[key]
			next_board_state_str= self.execute_action( action )
			next_board=Board.Board(next_board_state_str)
			if not next_board.is_under_check(agent_color): 
				admissible_actions[key]= action
		return admissible_actions

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

