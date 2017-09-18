import State
class LearningSim(object):
	"""docstring for LearningSim"""
	def __init__(self, initial_board_state, max_epoque_steps):
		s= State.State(initial_board_state)
		self.initial_state= s
		self.max_epoque_steps= max_epoque_steps
        self.agent_chosen= "white"
		#self.current_state= s
		# create database connection


	def every_visit_montecarlo_execution(self):
		#loop
				#generate episode retriving Q_table entries for current_state and choose the next action following softmax policy with e-greedy
				epoque= self.generate_epoque(self.initial_state)

                reward_epoque= epoque[len(epoque)-1][0].get_reward(self.agent_chosen)

                #then for every state action pair in the epoque
                # if the turn was of white then update Q table with reward_epoque_scaled
                # else update Q table with - reward_epoque_scaled
                # logic : agent learn Q entries both from moves made by him but also
                # from the moves made from the opponent


				#execute montecarlo for every state in episode
				for  [ state , action , next_state , turn] in epoque :
					# reward= next_state.get_reward( turn ) no
					#database   insert in R table this tuple state,action, reward
					#database   get avg of rewards for this pair state action
					#database   update Q table with this avg


				#update the Q_table in DB ( the policy follows strictly from the Q_table)
				#register the epoch number and iteration number in DB table

    def generate_epoque(self, initial_state):
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
    		action=## implement database query for Q_table in database
    		#execute action
    		next_state_str= state.execute_action( action )
    		next_state= State.State(next_state_str)
    		sas_tuple= [ state, action, next_state, turn]
    		state_action_tuples.append( sas_tuple )

    		state= next_state
            if turn == "white":
                turn= "black"
            else:
                turn= "white"
    	
    	state_action_pairs.append( [state, None, None, turn])
    	return state_action_tuples
   



 #  possible calls from there to state class
 #  current_state.possible_actions(agent_color)
 #	current_state.get_reward()
 #	current_state.execute_action(action)
 #

