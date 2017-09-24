import MySQLdb


class Database(object):

	def __init__(self,user, db_name):
		self.db = MySQLdb.connect("localhost",user,user, db_name )




	def insert_reward_in_R(self, state_str , action_str, reward, epoque_num , iteration_num):
		query= "INSERT INTO RTABLE(STATE,ACTION,REWARD,EPOQUE,ITERATION)VALUES(%s,%s,%s,%s,%s)"
		cursor = self.db.cursor()

		try:
			cursor.execute(query, (state_str,action_str, reward, epoque_num, iteration_num))
			self.db.commit()
		except:
			self.db.rollback()

	def get_rewards_in_R(self, state_str, action_str):
		cursor = self.db.cursor()
		query= "SELECT REWARD FROM RTABLE WHERE state=%s AND action=%s"
		cursor.execute( query, (state_str,action_str))
	
		data= cursor.fetchall()
		rewards= [ r[0] for r in data ]
		return rewards

	def update_avg_reward_in_Q(self, state_str, action_str, new_avg_rew):
		pass


	def get_best_action_from_Q(self, state_str):
		q= "SELECT ACTION FROM QTABLE WHERE STATE=%s AND REWARD IN ( SELECT MAX(REWARD) FROM QTABLE WHERE STATE=%s)"
		cursor = self.db.cursor()
		cursor.execute(q, (state_str,state_str))
		data= cursor.fetchone()
		return data[0]
		

	def get_last_epoque_number(self):
		query= "SELECT MAX(EPOQUE) FROM RTABLE"
		cursor = self.db.cursor()
		cursor.execute(query)
		data= cursor.fetchone()
		return data[0]


	def get_last_iteration_number(self):
		query= "SELECT MAX(ITERATION) FROM RTABLE"
		cursor = self.db.cursor()
		cursor.execute(query)
		data= cursor.fetchone()
		return data[0]

	def get_epoque_cumulative_reward_in_R(self, epoque_num):
		query= "SELECT AVG(REWARD) FROM RTABLE WHERE EPOQUE=%s"
		cursor = self.db.cursor()
		cursor.execute(query, (str(epoque_num)))
		data= cursor.fetchone()
		return round(data[0],2)
		


	def get_iteration_cumulative_reward_in_R(self,iteration_num):
		query= "SELECT AVG(REWARD) FROM RTABLE WHERE ITERATION=%s"
		cursor = self.db.cursor()
		cursor.execute(query, (str(iteration_num)))
		data= cursor.fetchone()
		return round(float(data[0]),2)

	def get_cumulative_reward_in_Q(self):
		query= "SELECT AVG(REWARD) FROM QTABLE"
		cursor = self.db.cursor()
		cursor.execute(query)
		data= cursor.fetchone()
		return round(data[0],2)

	def get_size_of_Q(self):
		query= "SELECT COUNT(*) FROM QTABLE"
		cursor = self.db.cursor()
		cursor.execute(query)
		data= cursor.fetchone()
		return data[0]

	def close_connection(self):
		self.db.close()

'''

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print ("Database version : %s " % data)

db.close()

'''