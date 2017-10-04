from src import State
from src import Action
import random

class LearningSim(object):
	"""docstring for LearningSim"""
	def __init__(self, initial_board_state, max_epoque_steps, agent_chosen,db,tot_of_epoques, totally_greedy_flag=False):
		s= State.State(initial_board_state)
		self.initial_state= s
		self.max_epoque_steps= max_epoque_steps
		self.agent_chosen= agent_chosen
		self.database= db
		self.tot_of_epoques=tot_of_epoques
		self.totally_greedy_flag= totally_greedy_flag


	def montecarlo_epoque_exec(self,iteration_num,epoque_num):
		epoque= self.generate_epoque(iteration_num,epoque_num)
		return self.update_tables(epoque,iteration_num,epoque_num)

		

	def update_tables(self,epoque,iteration_num,epoque_num):
		[last_state, last_action, last_turn] = epoque[len(epoque)-1]
		winner= last_state.get_winner()
		(white_rew, black_rew)= last_state.get_reward()
		epoque.pop(len(epoque)-1)



		length_epoque= len(epoque)
		index= 0

		#then for every state action pair in the epoque
		# if the turn was of white then update Q table with reward_epoque_scaled
		# else update Q table with - reward_epoque_scaled
		# logic : agent learn Q entries both from moves made by him but also
		# from the moves made from the opponent

		#execute montecarlo for every state in episode
		for  [ state , action , turn] in epoque :
			index+=1
			discount_coeff= 0.2+ (index/length_epoque) * 0.8
			if turn== "white":
				reward= white_rew * discount_coeff
			else:
				reward= black_rew * discount_coeff
			
			#database   get avg of rewards for this pair state action
			past_avg_rewards= self.database.get_rewards_in_R(state.__str__(),action.__str__())

			if past_avg_rewards==None:
				new_average= reward
			else:
				new_average= self.new_avg(past_avg_rewards, reward)
			#database   insert in R table this tuple state,action, reward
			self.database.insert_reward_in_R( state.__str__(), action.__str__(), reward, turn,  epoque_num, iteration_num)

			#database   update Q table with this avg
			self.database.update_avg_reward_in_Q(state.__str__(),action.__str__(),new_average, turn)

		#update the Q_table in DB ( the policy follows strictly from the Q_table)
		#register the epoch number and iteration number in DB table
		return winner
	   
	def generate_epoque(self,iteration_num,epoque_num):
		#generate episode retriving Q_table entries for current_state and choose the next action following softmax policy with e-greedy
		step_number= 0
		state = self.initial_state
		turn= "white"
		state_action_tuples= []
		while step_number <= self.max_epoque_steps and not state.is_final_state_for_agent(turn):
			if turn == "white":
				possible_actions= state.possible_actions("white")
			else:
				possible_actions= state.possible_actions("black")

			#choose an action according to policy
			action=self.choose_action(state,possible_actions,epoque_num,turn)## implement database query for Q_table in database
			#execute action. choosing with softmax and maybe with epsilon greedy
			next_state_str= state.execute_action( action )
			next_state= State.State(next_state_str)
			sa_tuple= [ state, action, turn]
			state_action_tuples.append( sa_tuple )

			state= next_state
			step_number+=1
			if turn == "white":
				turn= "black"
			else:
				turn= "white"
		if state.is_final_state_for_agent(turn):
			state_action_tuples.append( [state, None, turn ])

		return state_action_tuples
   
	def new_avg(self,old_avgs, new_rew):
		num_of_samples= len(old_avgs) +1
		return round(  (sum(old_avgs)+ new_rew)/num_of_samples , 2 )

	def choose_action(self,state, possible_actions, epoque_num, turn):
		if turn == self.agent_chosen :
			#epsilon greedy
			epsilon =  1.05 - (epoque_num/self.tot_of_epoques)
			if epsilon < random.random() or self.totally_greedy_flag :
				
				#exploitation
				if self.database.check_Q_entry_existence(state.__str__(), turn):
					best_actions_str_list= self.database.get_best_actions_from_Q(state.__str__(),turn)
					[chosen_action_str]= random.sample(best_actions_str_list,1)
					chosen_action= Action.Action(action_string= chosen_action_str, board=state.board)
					return chosen_action
		#exploration
		#uniformly random choice
		x=random.sample(list(possible_actions.values()),1)
		return x[0]


