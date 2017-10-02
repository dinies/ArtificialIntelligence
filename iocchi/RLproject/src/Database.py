import MySQLdb
import pdb

class Database(object):

	def __init__(self,user, db_name):
		self.db = MySQLdb.connect("localhost",user,user, db_name )




	def insert_reward_in_R(self, state_str , action_str, reward, turn, epoque_num , iteration_num):
		query= "INSERT INTO RTABLE(STATE,ACTION,REWARD,TURN,EPOQUE,ITERATION)VALUES(%s,%s,%s,%s,%s,%s)"
		cursor = self.db.cursor()

		try:
			cursor.execute(query, (state_str,action_str, reward,turn, epoque_num, iteration_num))
			self.db.commit()
		except:
			self.db.rollback()

	def get_rewards_in_R(self, state_str, action_str):
		cursor = self.db.cursor()
		existence_query= "SELECT COUNT(*) FROM RTABLE WHERE state=%s AND action=%s"
		cursor.execute( existence_query, (state_str,action_str))
		data= cursor.fetchone()
		if data[0] >0 :
			get_query= "SELECT REWARD FROM RTABLE WHERE state=%s AND action=%s"
			cursor.execute( get_query, (state_str,action_str))
			data= cursor.fetchall()
			rewards= [ r[0] for r in data ]
			return rewards
		else:
			return None

		

	def update_avg_reward_in_Q(self, state_str, action_str, new_avg_rew,turn):
		cursor = self.db.cursor()
		existence_query= "SELECT COUNT(*) FROM QTABLE WHERE state=%s AND action=%s"
		cursor.execute( existence_query, (state_str,action_str))
		data= cursor.fetchone()
		if data[0] == 1 :
			query="UPDATE QTABLE SET REWARD=%s WHERE state=%s AND action=%s"
			params= (new_avg_rew, state_str, action_str)
		else:
			query="INSERT INTO QTABLE(STATE,ACTION,REWARD , TURN)VALUES(%s,%s,%s,%s)"
			params= (state_str, action_str, str(new_avg_rew),turn)
		try:
			cursor.execute( query, params)
			self.db.commit()
		except:
			self.db.rollback()

	def get_best_action_from_Q(self, state_str,turn):
		q= "SELECT ACTION FROM QTABLE WHERE STATE=%s AND TURN=%s AND REWARD IN ( SELECT MAX(REWARD) FROM QTABLE WHERE STATE=%s AND TURN=%s)"
		cursor = self.db.cursor()
		cursor.execute(q, (state_str,turn,state_str,turn))
		data= cursor.fetchone()
		if data is None:
			return None
		return data[0]

	def check_Q_entry_existence(self,state_str,turn):
		query= "SELECT COUNT(*) FROM QTABLE WHERE STATE=%s AND TURN=%s"
		cursor = self.db.cursor()
		cursor.execute(query, (state_str,turn))
		data= cursor.fetchone()
		if data[0] == 0:
			return False
		else:
			return True
		

	# def get_last_epoque_number(self,iteration_num):
	# 	query= "SELECT MAX(EPOQUE) FROM RTABLE WHERE ITERATION=%s"
	# 	cursor = self.db.cursor()
	# 	cursor.execute(query, (str(iteration_num)))
	# 	data= cursor.fetchone()
	# 	return data[0]


	def get_last_iteration_number(self):
		query= "SELECT MAX(ITERATION) FROM RTABLE"
		cursor = self.db.cursor()
		cursor.execute(query)
		data= cursor.fetchone()
		if data[0] is None:
			return 0
		else:
			return data[0]

	def get_avg_reward_in_R(self,turn, epoque_num,iteration_num):
		cursor = self.db.cursor()
		existence_query= "SELECT COUNT(*) FROM RTABLE WHERE TURN=%s AND EPOQUE=%s AND ITERATION=%s"
		cursor.execute( existence_query, (turn,str(epoque_num),str(iteration_num)))
		data= cursor.fetchone()
		if data[0] >0 :
			get_query="SELECT AVG(REWARD) FROM RTABLE WHERE TURN=%s AND EPOQUE=%s AND ITERATION=%s"
			cursor.execute( get_query, (turn,str(epoque_num),str(iteration_num)))
			data= cursor.fetchone()
			return round(data[0],2)
		else:
			return None
		
	def get_avg_reward_in_Q(self,turn):

		cursor = self.db.cursor()
		existence_query= "SELECT COUNT(*) FROM QTABLE WHERE TURN=%s"
		cursor.execute( existence_query, (turn,))
		data= cursor.fetchone()
		if data[0] >0 :
			get_query="SELECT AVG(REWARD) FROM QTABLE WHERE TURN=%s"
			cursor.execute( get_query, (turn,))
			data= cursor.fetchone()
			return round(data[0],2)
		else:
			return None


	def get_size_of_Q(self):
		query= "SELECT COUNT(*) FROM QTABLE"
		cursor = self.db.cursor()
		cursor.execute(query)
		data= cursor.fetchone()
		return data[0]

	def save_performances_in_P(self,iteration_num,epoque_num,white_avg_R_rew,white_avg_Q_rew,black_avg_R_rew,black_avg_Q_rew,Q_size):
		query= "INSERT INTO PTABLE(ITERATION,EPOQUE,WAVGR,WAVGQ,BAVGR, BAVGQ, QSIZE)VALUES(%s,%s,%s,%s,%s,%s,%s)"
		cursor = self.db.cursor()
		try:
			cursor.execute(query, (iteration_num,epoque_num, white_avg_R_rew,white_avg_Q_rew,black_avg_R_rew,black_avg_Q_rew,Q_size))
			self.db.commit()
		except:
			self.db.rollback()


	def flush_db(self):
		cursor=self.db.cursor()
		drop_Q_table="DROP TABLE QTABLE"
		drop_R_table="DROP TABLE RTABLE"
		drop_P_table="DROP TABLE PTABLE"

		try:
			cursor.execute(drop_Q_table)
		except Exception as e:
			print(e)
			print("\nnon si cancella q table")

		try:
			cursor.execute(drop_R_table)
		except Exception as e:
			print(e)
			print("\n non si cancella r table")

		try:
			cursor.execute(drop_P_table)
		except Exception as e:
			print(e)
			print("\n non si cancella p table")

		create_R="CREATE TABLE RTABLE (ID INTEGER PRIMARY KEY AUTO_INCREMENT,STATE  VARCHAR(100) NOT NULL,ACTION  VARCHAR(10) NOT NULL,REWARD INT,TURN VARCHAR(10),EPOQUE INT,ITERATION INT );"
		create_Q="CREATE TABLE QTABLE (STATE  VARCHAR(100) NOT NULL,ACTION  VARCHAR(10) NOT NULL,REWARD FLOAT(2),TURN VARCHAR(10),PRIMARY KEY(STATE,ACTION));"
		create_P="CREATE TABLE PTABLE (ITERATION INT NOT NULL,EPOQUE INT NOT NULL, WAVGR FLOAT(2), WAVGQ FLOAT(2), BAVGR FLOAT(2), BAVGQ FLOAT(2), QSIZE INT, PRIMARY KEY(ITERATION, EPOQUE));"

		cursor.execute(create_R)
		cursor.execute(create_Q)
		cursor.execute(create_P)



	def close_connection(self):
		self.db.close()
