import MySQLdb



class Database(object):

	def __init__(self,user, db_name):
		self.db = MySQLdb.connect("localhost",user,user, db_name )
		



	def insert_reward_in_R(self, state_str , action_str, reward, epoque_num , iteration_num):
		cursor = self.db.cursor()
		query= "INSERT INTO RTABLE(STATE,ACTION,REWARD,EPOQUE,ITERATION)VALUES(%s,%s,%s,%s,%s)"

		try:
			cursor.execute(query, (state_str,action_str, reward, epoque_num, iteration_num))
			self.db.commit()
		except:
			self.db.rollback()

	def get_rewards_from_stateAction_pair_in_R(self):
		pass


	def update_avg_reward_in_Q(self, state_str, action_str, new_avg_rew):
		pass


	def get_best_action_from_Q(self):
		pass

	def get_last_epoque_number(self):
		pass

	def get_last_iteration_number(self):
		pass

	def get_cumulative_reward_in_R(self):
		pass

	def get_size_in_state_of_Q(self):
		pass


'''

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print ("Database version : %s " % data)

db.close()

'''