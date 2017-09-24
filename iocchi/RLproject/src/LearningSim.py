import State
class LearningSim(object):
	"""docstring for LearningSim"""
	def __init__(self, initial_board_state, max_epoque_steps, agent_chosen,db):
		s= State.State(initial_board_state)
		self.initial_state= s
		self.max_epoque_steps= max_epoque_steps
		self.agent_chosen= agent_chosen
		self.database= db
		#self.current_state= s
		# create database connection


	def montecarlo_epoque_exec(self,iteration):
		#loop
		epoque= self.generate_epoque(self.initial_state)
		self.update_tables(epoque)

		

	def update_tables(self,epoque):
		[last_state, last_action, last_turn] = epoque[len(epoque)-1]

		if not last_state.is_final_state() :
			reward_epoque= -1
		else:
			reward_epoque= last_state.get_reward(self.agent_chosen)


		#then for every state action pair in the epoque
		# if the turn was of white then update Q table with reward_epoque_scaled
		# else update Q table with - reward_epoque_scaled
		# logic : agent learn Q entries both from moves made by him but also
		# from the moves made from the opponent

		epoque_num= self.database.get_last_epoque_number()
		epoque_num+=1
		#execute montecarlo for every state in episode
		for  [ state , action , turn] in epoque :

			if turn== self.agent_chosen:
				reward= reward_epoque
			else:
				reward= -reward_epoque

		#database   insert in R table this tuple state,action, reward
		self.database.insert_reward_in_R( state.__str__(), action.__str__(), reward, epoque_num, iteration)
		#database   get avg of rewards for this pair state action
		past_avg_rewards= self.database.get_rewards_from_stateAction_pair_in_R(state.__str__(),action.__str__())

		#compute the avg with also the new reward

		new_average= self.new_avg(past_avg_rewards, reward)


		#database   update Q table with this avg
		self.database.update_avg_reward_in_Q(state.__str__(),action.__str__(),new_average)

		#update the Q_table in DB ( the policy follows strictly from the Q_table)
		#register the epoch number and iteration number in DB table
	   
	def generate_epoque(self, initial_state):
		#generate episode retriving Q_table entries for current_state and choose the next action following softmax policy with e-greedy
		step_number= 0
		state = initial_state
		turn= "white"
		state_action_tuples= []
		while step_number <= self.max_epoque_steps and not state.is_final_state():
			if turn == "white":
				possible_actions= state.possible_actions("white")
			else:
				possible_actions= state.possible_actions("black")

			#choose an action according to policy
			action=self.choose_action()## implement database query for Q_table in database
			#execute action. choosing with softmax and maybe with epsilon greedy
			next_state_str= state.execute_action( action )
			next_state= State.State(next_state_str)
			sa_tuple= [ state, action, turn]
			state_action_tuples.append( sa_tuple )

			state= next_state
			if turn == "white":
				turn= "black"
			else:
				turn= "white"
		if state.is_final_state():
			state_action_tuples.append( [state, None, turn ])

		return state_action_tuples
   
	def new_avg(self,old_avgs, new_rew):
		pass

	def choose_action(self,state, possible_actions):
		pass



 #  possible calls from there to state class
 #  current_state.possible_actions(agent_color)
 #	current_state.get_reward()
 #	current_state.execute_action(action)
 #

