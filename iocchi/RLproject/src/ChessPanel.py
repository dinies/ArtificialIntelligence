from context import src
from src import LearningSim as ls
from src import Database
import pdb
class ChessPanel(object):
	"""docstring for ChessPanel"""
	def __init__(self, initial_board_state="1k1/ppp/111/111/PPP/1K1"):
		self.initial_board_state= initial_board_state
		self.max_epoque_steps= 400
		self.agent_chosen= "white"
		self.db=Database.Database("chessagent","chessqboard")

		
	def run_learning(self,tot_epoque_num=100):

		iteration_num= self.db.get_last_iteration_number()
		iteration_num+=1
		epoque_num=0
		for _ in range(tot_epoque_num):
			self.simulator= ls.LearningSim(self.initial_board_state ,self.max_epoque_steps,self.agent_chosen,self.db,tot_epoque_num)
			print("epoque_num"+str(epoque_num+1))
			self.simulator.montecarlo_epoque_exec(iteration_num,epoque_num+1)
			self.save_statistics(iteration_num,epoque_num+1)
			epoque_num+=1

	def save_statistics(self,iteration_num,epoque_num):
		white_avg_R_rew = self.db.get_avg_reward_in_R("white",epoque_num,iteration_num)
		white_avg_Q_rew = self.db.get_avg_reward_in_Q("white")
		black_avg_R_rew = self.db.get_avg_reward_in_R("black",epoque_num,iteration_num)
		black_avg_Q_rew = self.db.get_avg_reward_in_Q("black")
		
		Q_size= self.db.get_size_of_Q()
		self.db.save_performances_in_P(iteration_num,epoque_num,white_avg_R_rew,white_avg_Q_rew,black_avg_R_rew,black_avg_Q_rew,Q_size)

	def run_some_greedy_games(self,games_num):
		iteration_num= self.db.get_last_iteration_number()
		iteration_num+=1
		for _ in range(games_num):
			self.simulator= ls.LearningSim(self.initial_board_state ,self.max_epoque_steps,self.agent_chosen,self.db,1,totally_greedy_flag=True)
			self.simulator.montecarlo_epoque_exec(iteration_num,games_num)
			self.save_statistics(iteration_num,games_num)
			games_num+=1


	def reduced_board_case(self):
		self.initial_board_state="k11/111/KPP"
		self.db.flush_db()
		self.run_learning()
		self.run_some_greedy_games(10)
		self.db.close_connection()



if __name__ == '__main__':
	c=ChessPanel()
	c.reduced_board_case()


