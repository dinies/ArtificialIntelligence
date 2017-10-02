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




class LearningSimTest(unittest.TestCase):
	def setUp(self):
		self.max_epoque_steps= 100
		self.tot_epoques=10
		self.db_learning_sim= Database.Database("chesstester","chessqtest")
		self.learning_sim= LearningSim.LearningSim("1k1/ppp/111/111/PPP/1K1",self.max_epoque_steps,"white",self.db_learning_sim,self.tot_epoques)
		self.test_db= MySQLdb.connect("localhost","chesstester","chesstester","chessqtest" )

		queries=[ 
		"CREATE TABLE QTABLE (STATE  VARCHAR(100) NOT NULL,ACTION  VARCHAR(10) NOT NULL,REWARD FLOAT(2),TURN VARCHAR(10),PRIMARY KEY(STATE,ACTION))",
		"CREATE TABLE RTABLE (ID INTEGER PRIMARY KEY AUTO_INCREMENT,STATE  VARCHAR(100) NOT NULL,ACTION  VARCHAR(10) NOT NULL,REWARD INT,TURN VARCHAR(10),EPOQUE INT,ITERATION INT )"
		]
		cursor=self.test_db.cursor()		
		cursor.execute(queries[0])
		cursor.execute(queries[1])

		self.test_db.close()


	def test_generate_epoque(self):

		random.seed(3)
		epoque= self.learning_sim.generate_epoque(1,2)

		current_final_state=epoque[len(epoque)-1][0]
		self.assertTrue(isinstance(epoque[len(epoque)-1][0] , State.State))
		self.assertTrue( current_final_state.is_losing_state_for_agent("white") or current_final_state.is_losing_state_for_agent("black") or len(epoque)>= self.max_epoque_steps)

		[state, action, turn] = random.sample(epoque,1)[0]
		self.assertTrue(isinstance(state , State.State))
		self.assertTrue(isinstance(action , Action.Action))

	def test_generate_epoque_check_alternate_moves(self):

		random.seed(90)
		epoque= self.learning_sim.generate_epoque(1,2)

		turn_flag= "white"
		for [state,action,turn] in epoque:
			self.assertTrue(turn == turn_flag)
			if turn_flag=="white":
				turn_flag="black"
			else:
				turn_flag="white"
		
	def test_new_avg(self):
		x= [ 2,4,8,10]
		y= [1 , -1, -100 ,100, 0]
		z= []
		w= -5

		self.assertEqual(self.learning_sim.new_avg(x,w), 3.80)
		self.assertEqual(self.learning_sim.new_avg(y,w), -0.83)
		self.assertEqual(self.learning_sim.new_avg(z,w), -5.00)
		self.assertEqual(self.learning_sim.new_avg([100],-100), 0.00)

	def test_choose_action(self):
		white_king= King.King("white")
		K_pos = Square.Square("b", 1)
		white_king.add_square(K_pos)
		left_w_pawn= Pawn.Pawn("white")
		P_pos= Square.Square("a", 2)
		left_w_pawn.add_square(P_pos)


		target_square1 = Square.Square("a", 3)
		target_square2 = Square.Square("a", 1)
		target_square3 = Square.Square("c", 1)

		action1= Action.Action(left_w_pawn,target_square1)
		action2= Action.Action(white_king,target_square2)
		action3= Action.Action(white_king,target_square3)

		possible_actions= {
		"P.a2-a3": action1,
		"K.b1-a1": action2,
		"K.b1-a3": action3
		}

		a= self.learning_sim.choose_action(self.learning_sim.initial_state, possible_actions, 2, "black")
		self.assertTrue( a in possible_actions.values())
		self.assertTrue(isinstance(a , Action.Action))



	def tearDown(self):
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



