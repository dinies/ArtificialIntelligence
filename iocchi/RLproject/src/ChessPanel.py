import LearningSim as ls
class ChessPanel(object):
	"""docstring for ChessPanel"""
	def __init__(self, arg):
		self.arg = arg
		self.initial_board_state= "1k1/ppp/3/3/PPP/1K1"
		
	def run_learning(self):
		self.simulator= ls.LearningSim(self.initial_board_state)
		self.simulator.run_epoch()

