import MySQLdb


def trial(state_str, action_str,reward,epoque,iteration):

	db = MySQLdb.connect("localhost","chesstester","chesstester","chessqtest")

	create_q="CREATE TABLE RTABLE (ID INTEGER PRIMARY KEY AUTO_INCREMENT,STATE  VARCHAR(100) NOT NULL,ACTION  VARCHAR(10) NOT NULL,REWARD FLOAT(2) ,EPOQUE INT,ITERATION INT )"

	ins_q="INSERT INTO RTABLE(STATE,ACTION,REWARD,EPOQUE,ITERATION)VALUES(%s,%s,%s,%s,%s)"

	cursor = db.cursor()
	
	cursor.execute(create_q)
	
	try:
		cursor.execute(ins_q, (state_str,action_str, reward, epoque, iteration))
		db.commit()
		print ("c'e l'ho fatta2")
	except:
		db.rollback()
		print("nada2")

	db.close()




trial("1k1/ppp/111/111/PPP/1K1", "K.a2-a3", 100,2,4)