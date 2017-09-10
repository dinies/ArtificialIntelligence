import State
class LearningSim(object):
	"""docstring for LearningSim"""
	def __init__(self, initial_board_state):
		self.current_state= State.State(initial_board_state)
		# create database connection


	def run_epoch(self):
		#loop
				#generate episode retriving Q_table entries for current_state and choose the next action following softmax policy with e-greedy
				#execute montecarlo for every state in episode
				#update the Q_table in DB ( the policy follows strictly from the Q_table)
				#register the epoch number and iteration number in DB table



 #  possible calls from there to state class
 #  current_state.possible_actions()
 #	current_state.get_reward()
 #	current_state.execute_action(action)
 #

