import unittest
import MySQLdb
from context import src
from src import Database

class DatabaseTest(unittest.TestCase):
	def setUp(self):
		self.test_db = MySQLdb.connect("localhost","chesstester","chesstester","chessqtest" )

		queries=[
		"CREATE TABLE QTABLE (STATE  VARCHAR(100) NOT NULL,ACTION  VARCHAR(10) NOT NULL,REWARD INT,PRIMARY KEY(STATE,ACTION))",

		"CREATE TABLE RTABLE (ID INTEGER PRIMARY KEY AUTO_INCREMENT,STATE  VARCHAR(100) NOT NULL,ACTION  VARCHAR(10) NOT NULL,REWARD INT,EPOQUE INT,ITERATION INT )",

		"INSERT INTO RTABLE (state, action, reward, epoque, iteration) VALUES (%s,%s, %s, %s, %s)"
		]

		values= [
		["1k1/ppp/111/111/PPP/1K1", "K.a2-a1", -5,1,2],
		["1k1/ppp/111/111/PPP/1K1", "K.a2-c1", 100,1,2],
		["1k1/ppp/111/111/PPP/1K1", "K.a2-a1", -100, 1, 2],
		["1k1/ppp/111/111/PPP/1K1", "K.a2-a1", -52, 1, 2],
		["1k1/ppp/111/111/PPP/1K1", "K.a2-c1", 100, 1, 2]
		]

		cursor=self.test_db.cursor()		
		cursor.execute(queries[0])
		cursor.execute(queries[1])

		for vec in values:
			try:
				cursor.execute(queries[2], (vec[0], vec[1], vec[2], vec[3], vec[4]))
				self.test_db.commit()
			except:
				self.test_db.rollback()

	def test_insert_reward_in_R(self):
		db= Database.Database("chesstester", "chessqtest")
		db.insert_reward_in_R("1k1/ppp/111/111/PPP/1K1","K.a2-a3",100,2,2)

		sql_select="SELECT REWARD FROM RTABLE WHERE state= %s AND action=%s "

		state="1k1/ppp/111/111/PPP/1K1"
		action="K.a2-a3"

		cursor = self.test_db.cursor()

		cursor.execute(sql_select, (state,action))
		result=cursor.fetchone()
		self.assertEqual(100,result[0])

	@unittest.skip("demonstrating skipping")
	def test_get_rewards_from_stateAction_pair_in_R(self):
		db= Database.Database("chesstester", "chessqtest")
		db.insert_Qentry("1k1/ppp/111/111/PPP/1K1","K.a2-a3",100,12,13)

		sql_select=...
		cursor = db.cursor()

		cursor.execute(sql_select)

		data = cursor.fetchone()
	

	@unittest.skip("demonstrating skipping")
	def test_update_avg_reward_in_Q(self):
		db= Database.Database("chesstester", "chessqtest")
		db.insert_Qentry("1k1/ppp/111/111/PPP/1K1","K.a2-a3",100,12,13)

		sql_select=...
		cursor = db.cursor()

		cursor.execute(sql_select)

		data = cursor.fetchone()


	@unittest.skip("demonstrating skipping")
	def test_get_best_action_from_Q(self):
		db= Database.Database("chesstester", "chessqtest")
		db.insert_Qentry("1k1/ppp/111/111/PPP/1K1","K.a2-a3",100,12,13)

		sql_select=...
		cursor = db.cursor()

		cursor.execute(sql_select)

		data = cursor.fetchone()



	@unittest.skip("demonstrating skipping")
	def test_get_last_epoque_number(self):
		db= Database.Database("chesstester", "chessqtest")
		db.insert_Qentry("1k1/ppp/111/111/PPP/1K1","K.a2-a3",100,12,13)

		sql_select=...
		cursor = db.cursor()

		cursor.execute(sql_select)

		data = cursor.fetchone()
	
	@unittest.skip("demonstrating skipping")	
	def test_get_last_iteration_number(self):
		db= Database.Database("chesstester", "chessqtest")
		db.insert_Qentry("1k1/ppp/111/111/PPP/1K1","K.a2-a3",100,12,13)

		sql_select=...
		cursor = db.cursor()

		cursor.execute(sql_select)

		data = cursor.fetchone()


	@unittest.skip("demonstrating skipping")
	def test_get_cumulative_reward_in_R(self):
		db= Database.Database("chesstester", "chessqtest")
		db.insert_Qentry("1k1/ppp/111/111/PPP/1K1","K.a2-a3",100,12,13)

		sql_select=...
		cursor = db.cursor()

		cursor.execute(sql_select)

		data = cursor.fetchone()


	@unittest.skip("demonstrating skipping")
	def test_get_size_in_state_of_Q(self):
		db= Database.Database("chesstester", "chessqtest")
		db.insert_Qentry("1k1/ppp/111/111/PPP/1K1","K.a2-a3",100,12,13)

		sql_select=...
		cursor = db.cursor()

		cursor.execute(sql_select)

		data = cursor.fetchone()



	def tearDown(self):
		queries=[
		"DROP TABLE QTABLE"
		]
		cursor=self.test_db.cursor()
		for q in queries:
			cursor.execute(q)
		self.test_db.close()


if __name__ == '__main__':
	unittest.main()