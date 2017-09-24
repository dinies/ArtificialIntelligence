import unittest
import MySQLdb
from context import src
from src import Database

class DatabaseTest(unittest.TestCase):
	def setUp(self):
		self.true_db = MySQLdb.connect("localhost","chesstester","chesstester","chessqtest" )
		self.db_under_test= Database.Database("chesstester", "chessqtest")

		queries=[
		"CREATE TABLE QTABLE (STATE  VARCHAR(100) NOT NULL,ACTION  VARCHAR(10) NOT NULL,REWARD FLOAT(2),PRIMARY KEY(STATE,ACTION))",

		"CREATE TABLE RTABLE (ID INTEGER PRIMARY KEY AUTO_INCREMENT,STATE  VARCHAR(100) NOT NULL,ACTION  VARCHAR(10) NOT NULL,REWARD INT,EPOQUE INT,ITERATION INT )",

		"INSERT INTO RTABLE (state, action, reward, epoque, iteration) VALUES (%s,%s, %s, %s, %s)",

		"INSERT INTO QTABLE (state, action, reward) VALUES (%s,%s, %s)"

		]

		Rvalues= [
		["1k1/ppp/111/111/PPP/1K1", "K.a2-a1", -5,1,2],
		["1k1/ppp/111/111/PPP/1K1", "K.a2-c1", 100,5,2],
		["1k1/ppp/111/111/PPP/1K1", "K.a2-a1", -100, 2, 4],
		["1k1/ppp/111/111/PPP/1K1", "K.a2-a1", -52, 5, 2],
		["1k1/ppp/111/111/PPP/1K1", "K.a2-c1", 100, 3, 1]
		]

		Qvalues=[
		["1k1/ppp/111/111/PPP/1K1", "K.a2-a1", sum([-5,-100,-52])/3],
		["1k1/ppp/111/111/PPP/1K1", "K.a2-c1", 100],
		]
		self.cursor=self.true_db.cursor()		
		self.cursor.execute(queries[0])
		self.cursor.execute(queries[1])

		for vec in Rvalues:
			try:
				self.cursor.execute(queries[2], (vec[0], vec[1], vec[2], vec[3], vec[4]))
				self.true_db.commit()
			except:
				self.true_db.rollback()

		for vec in Qvalues:
			try:
				self.cursor.execute(queries[3], (vec[0], vec[1], vec[2]))
				self.true_db.commit()
			except:
				self.true_db.rollback()


	def test_insert_reward_in_R(self):
		self.db_under_test.insert_reward_in_R("1k1/ppp/111/111/PPP/1K1","K.a2-a3",100,2,2)

		sql_select="SELECT * FROM RTABLE WHERE state= %s AND action=%s "

		state="1k1/ppp/111/111/PPP/1K1"
		action="K.a2-a3"

		self.cursor.execute(sql_select, (state,action))

		result=self.cursor.fetchone()
		self.assertEqual("1k1/ppp/111/111/PPP/1K1",result[1])
		self.assertEqual("K.a2-a3",result[2])
		self.assertEqual(100,result[3])
		self.assertEqual(2,result[4])
		self.assertEqual(2,result[5])

	def test_get_rewards_in_R(self):

		true_rewards= [-5,-100,-52]
		rewards= self.db_under_test.get_rewards_in_R("1k1/ppp/111/111/PPP/1K1","K.a2-a1")
		self.assertEqual(true_rewards, rewards)
	

	@unittest.skip("demonstrating skipping")
	def test_update_avg_reward_in_Q(self):

		state="1k1/ppp/111/111/PPP/1K1"
		action="K.a2-c1"

		self.db_under_test.update_avg_reward_in_Q(state,action,30.45)

		sql_select= "SELECT * FROM QTABLE WHERE state= %s AND action=%s "
		cursor = db.cursor()

		cursor.execute(sql_select, (state,action))

		result=cursor.fetchone()
		self.assertEqual(state,result[0])
		self.assertEqual(action,result[1])
		self.assertEqual(30.45,result[2])


	def test_get_best_action_from_Q(self):
		result= self.db_under_test.get_best_action_from_Q("1k1/ppp/111/111/PPP/1K1")

		self.assertEqual( result, "K.a2-c1" )


	def test_get_last_epoque_number(self):
		result= self.db_under_test.get_last_epoque_number()

		self.assertEqual(result, 5 )

	def test_get_last_iteration_number(self):
		result= self.db_under_test.get_last_iteration_number()

		self.assertEqual(result, 4 )

	def test_get_epoque_cumulative_reward_in_R(self):
		result= self.db_under_test.get_epoque_cumulative_reward_in_R(2)

		self.assertEqual(result, -100.00)


	def test_get_iteration_cumulative_reward_in_R(self):
		result= self.db_under_test.get_iteration_cumulative_reward_in_R(2)

		self.assertEqual(result, 14.33 )

	def test_get_cumulative_reward_in_Q(self):
		result= self.db_under_test.get_cumulative_reward_in_Q()

		self.assertEqual(result, 23.83 )


	def test_get_size_of_Q(self):
		result= self.db_under_test.get_size_of_Q()

		self.assertEqual(result, 2 )



	def tearDown(self):
		self.db_under_test.close_connection()
		drop_Q_table="DROP TABLE QTABLE"
		drop_R_table="DROP TABLE RTABLE"
		try:
			self.cursor.execute(drop_Q_table)
		except Exception as e:
			print(e)
			print("\nnon si cancella q table")

		try:
			self.cursor.execute(drop_R_table)
		except Exception as e:
			print(e)
			print("\n non si cancella r table")
		self.true_db.close()


if __name__ == '__main__':
	unittest.main()