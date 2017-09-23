import LearningSim as ls
class ChessPanel(object):
	"""docstring for ChessPanel"""
	def __init__(self, arg):
		self.arg = arg
		self.initial_board_state= "1k1/ppp/111/111/PPP/1K1"
		self.max_epoque_steps= 400
		self.agent_chosen= "white"
		self.db=Database.Database("chessqboard")

		
	def run_learning(self):

		self.simulator= ls.LearningSim(self.initial_board_state ,self.max_epoque_steps,self.agent_chosen,self.db)
		iteration_num= self.db.get_last_iteration_number()
		iteration_num+=1
		for _ in range(2):
			self.simulator.montecarlo_epoque_exec(iteration_num)
		self.db.close()

