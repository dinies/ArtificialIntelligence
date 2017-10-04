from context import src
from src import LearningSim as ls
from src import Database
from src import State
import pdb
class ChessPanel(object):
	"""docstring for ChessPanel"""
	def __init__(self, initial_board_state="1k1/ppp/111/111/PPP/1K1", agent_chosen="white"):
		self.initial_board_state= initial_board_state
		self.max_epoque_steps= 400
		self.agent_chosen= agent_chosen
		self.db=Database.Database("chessagent","chessqboard")

		
	def run_learning(self,tot_epoque_num=300):

		iteration_num= self.db.get_last_iteration_number()
		iteration_num+=1
		epoque_num=1
		for _ in range(tot_epoque_num):
			self.simulator= ls.LearningSim(self.initial_board_state ,self.max_epoque_steps,self.agent_chosen,self.db,tot_epoque_num)
			print("epoque_num  "+str(epoque_num))
			winner= self.simulator.montecarlo_epoque_exec(iteration_num,epoque_num)
			self.save_statistics(iteration_num,epoque_num,winner)
			epoque_num+=1

	def save_statistics(self,iteration_num,epoque_num,winner):
		white_avg_R_rew = self.db.get_avg_reward_in_R("white",epoque_num,iteration_num)
		white_avg_Q_rew = self.db.get_avg_reward_in_Q("white")
		black_avg_R_rew = self.db.get_avg_reward_in_R("black",epoque_num,iteration_num)
		black_avg_Q_rew = self.db.get_avg_reward_in_Q("black")
		
		Q_size= self.db.get_size_of_Q()

		self.db.save_performances_in_P(iteration_num,epoque_num,white_avg_R_rew,white_avg_Q_rew,black_avg_R_rew,black_avg_Q_rew,Q_size,winner)

	def run_some_greedy_games(self,games_num):
		iteration_num= self.db.get_last_iteration_number()
		iteration_num+=1
		counter=1
		for _ in range(games_num):
			self.simulator= ls.LearningSim(self.initial_board_state ,self.max_epoque_steps,self.agent_chosen,self.db,1,totally_greedy_flag=True)
			print("greedy_game  "+str(counter))
			winner= self.simulator.montecarlo_epoque_exec(iteration_num,counter)
			self.save_statistics(iteration_num,counter,winner)
			counter+=1

	# working
	def reduced_massive_advantage_board_case(self):
		self.initial_board_state="k11/111/KPP"
		self.db.flush_db()
		self.run_learning()
		self.run_some_greedy_games(10)
		self.db.close_connection()


	# working
	def reduced_slight_advantage_board_case(self):
		self.initial_board_state="k1p/111/111/KPP"
		self.db.flush_db()
		self.run_learning()
		self.run_some_greedy_games(30)
		self.db.close_connection()


	def reduced_parity_board_case(self):
		self.initial_board_state="1k1/ppp/111/111/PPP/1K1"
		self.db.flush_db()
		self.run_learning(tot_epoque_num= 5000)
		self.run_some_greedy_games(500)
		self.db.close_connection()

	def display_game(self, epoque_num, iteration_num):
		states_list=self.db.get_states_of_game(epoque_num, iteration_num)
		for state_string in states_list:
			state= State.State(state_string)
			state.board.display()



if __name__ == '__main__':
	w=ChessPanel()
	w.reduced_slight_advantage_board_case()
	# w.reduced_massive_advantage_board_case()
	# w.display_game(30,2)
	# w.reduced_parity_board_case()
	# b=ChessPanel(agent_chosen="black")
	# w.run_some_greedy_games(50)

