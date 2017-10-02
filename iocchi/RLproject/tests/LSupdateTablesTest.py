import unittest
from context import src
from src import LearningSim
from src import Database
from src import Action
from src import Square
from src import King
from src import Pawn
from src import State
import MySQLdb
import random
import pdb




class LSupdateTables(unittest.TestCase):
	def setUp(self):
		self.max_epoque_steps= 100
		self.tot_epoques=10
		self.db_learning_sim= Database.Database("chesstester","chessqtest")
		self.learning_sim= LearningSim.LearningSim("1k1/ppp/111/111/PPP/1K1",self.max_epoque_steps,"white",self.db_learning_sim,self.tot_epoques)
		self.flag_drop_tables=False
		self.test_db= MySQLdb.connect("localhost","chesstester","chesstester","chessqtest" )

	def test_update_tables(self):
		self.flag_drop_tables=True

		queries=[
		"CREATE TABLE QTABLE (STATE  VARCHAR(100) NOT NULL,ACTION  VARCHAR(10) NOT NULL,REWARD FLOAT(2),TURN VARCHAR(10),PRIMARY KEY(STATE,ACTION))",

		"CREATE TABLE RTABLE (ID INTEGER PRIMARY KEY AUTO_INCREMENT,STATE  VARCHAR(100) NOT NULL,ACTION  VARCHAR(10) NOT NULL,REWARD INT,TURN VARCHAR(10),EPOQUE INT,ITERATION INT )",

		"INSERT INTO RTABLE (state, action, reward, turn, epoque, iteration) VALUES (%s,%s, %s, %s, %s,%s)",

		"INSERT INTO QTABLE (state, action, reward, turn) VALUES (%s,%s, %s, %s)",

		"SELECT COUNT(*) FROM RTABLE WHERE state= %s AND action=%s AND reward=%s AND turn=%s AND epoque=%s AND iteration=%s",

		"SELECT reward FROM QTABLE WHERE state= %s AND action=%s AND turn=%s",

		"SELECT COUNT(*) FROM QTABLE",

		"SHOW TABLES LIKE %s",

		"DROP TABLE QTABLE",

		"DROP TABLE RTABLE"
		]
		
		Rvalues= [
		["1k1/ppp/111/111/PPP/1K1", "P.c2-c3", -100,"white",1,1],
		["1k1/ppp/111/11P/PP1/1K1", "k.b6-a6", 100,"black",1,1],
		["k11/ppp/11P/11P/PP1/1K1", "P.c3-c4", -100,"white",1,1],
		["k11/ppp/11P/111/PP1/1K1", "p.b5xc4", 100,"black",1,1]
		]

		Qvalues=[
		["1k1/ppp/111/111/PPP/1K1", "P.c2-c3", -100, "white"],
		["1k1/ppp/111/11P/PP1/1K1", "k.b6-a6", 100, "black"],
		["k11/ppp/11P/11P/PP1/1K1", "P.c3-c4", -100, "white"],
		["k11/ppp/11P/111/PP1/1K1", "p.b5xc4", 100, "black"]
		]
		cursor=self.test_db.cursor()



		cursor.execute(queries[7], ("qtable",))
		data= cursor.fetchone()
		if not data is None:
			cursor.execute(queries[8])
		
		cursor.execute(queries[7], ("rtable",))
		data= cursor.fetchone()
		if not data is None:
			cursor.execute(queries[9])

		cursor.execute(queries[0])
		cursor.execute(queries[1])

		for vec in Rvalues:
			try:
				cursor.execute(queries[2], (vec[0], vec[1], vec[2], vec[3], vec[4], vec[5]))
				self.test_db.commit()
			except:
				self.test_db.rollback()

		for vec in Qvalues:
			try:
				cursor.execute(queries[3], (vec[0], vec[1], vec[2],vec[3]))
				self.test_db.commit()
			except:
				self.test_db.rollback()

		self.test_db.close()

		P_c2= Pawn.Pawn("white")
		P_c2_pos=Square.Square("c",2)
		P_c2.add_square(P_c2_pos)

		k_b6= King.King("black")
		k_b6_pos= Square.Square("b",6)
		k_b6.add_square(k_b6_pos)

		P_c5= Pawn.Pawn("white")
		P_c5_pos= Square.Square("c",5)
		P_c5.add_square(P_c5_pos)

		epoque_example= [
			[ State.State("1k1/ppp/111/111/PPP/1K1"), Action.Action(P_c2,Square.Square("c",3)), "white" ],
			[ State.State("1k1/ppp/111/11P/PP1/1K1"), Action.Action(k_b6,Square.Square("a",6)), "black" ],
			[ State.State("k11/ppP/111/1p1/P11/1K1"), Action.Action(P_c5,Square.Square("c",6)), "white" ],
			[ State.State("k1P/pp1/111/1p1/P11/1K1"), None, "black" ]
		]
		self.learning_sim.update_tables(epoque_example,1,2)


		self.test_db= MySQLdb.connect("localhost","chesstester","chesstester","chessqtest" )
		cursor=self.test_db.cursor()

		
		Rvalues_check= [
		["1k1/ppp/111/111/PPP/1K1", "P.c2-c3",100,"white",2,1],
		["1k1/ppp/111/11P/PP1/1K1", "k.b6-a6",-100,"black",2,1],
		["k11/ppP/111/1p1/P11/1K1", "P.c5-c6",100,"white",2,1],
		]

		Qvalues_check=[
		["1k1/ppp/111/111/PPP/1K1", "P.c2-c3", 0.00, "white"],
		["1k1/ppp/111/11P/PP1/1K1", "k.b6-a6", 0.00, "black"],
		["k11/ppP/111/1p1/P11/1K1", "P.c5-c6", 100.00, "white"],
		
		]


		for vec in Rvalues_check:
			cursor.execute(queries[4], (vec[0], vec[1], vec[2], vec[3], vec[4],vec[5]))
			result=cursor.fetchone()
			self.assertEqual(1,result[0])
		for vec in Qvalues_check:
			cursor.execute(queries[5], (vec[0], vec[1],vec[3]))
			result=cursor.fetchone()
			self.assertEqual(vec[2],result[0])
			
		cursor.execute(queries[6])
		result=cursor.fetchone()
		self.assertEqual(5,result[0])

	def tearDown(self):
		try:
			self.test_db.close()
		except Exception:
			pass

		self.db_learning_sim.close_connection()
		self.test_db= MySQLdb.connect("localhost","chesstester","chesstester","chessqtest" )
		cursor= self.test_db.cursor()
		drop_Q_table="DROP TABLE QTABLE"
		drop_R_table="DROP TABLE RTABLE"
		cursor.execute(drop_Q_table)
		cursor.execute(drop_R_table)
		self.test_db.close()
       
if __name__ == '__main__':
	unittest.main()
