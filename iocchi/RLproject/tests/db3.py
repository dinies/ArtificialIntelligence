import MySQLdb


def trial(state_str):

	db = MySQLdb.connect("localhost","chesstester","chesstester","chessqtest")
	#q= "SELECT ACTION, MAX(REWARD) FROM QTABLE WHERE STATE=%s)"
	q= "SELECT ACTION FROM QTABLE WHERE STATE=%s AND REWARD IN ( SELECT MAX(REWARD) FROM QTABLE WHERE STATE=%s)"
	cursor = db.cursor()

	cursor.execute(q,(state_str,state_str))

	data= cursor.fetchone()
	print(data)

	db.close()



trial("1k1/ppp/111/111/PPP/1K1")