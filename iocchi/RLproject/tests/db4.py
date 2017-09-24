import MySQLdb


def trial(state_str,action_str):

	db = MySQLdb.connect("localhost","chesstester","chesstester","chessqtest")

	ins_q="SELECT REWARD FROM RTABLE WHERE state=%s AND action=%s"

	cursor = db.cursor()

	try:
		cursor.execute(ins_q, (state_str,action_str))
		db.commit()
		print ("c'e l'ho fatta44")
	except:
		db.rollback()
		print("nada44")


	data= cursor.fetchall()
	print(data)
	db.close()





trial("1k1/ppp/111/111/PPP/1K1", "K.a2-a1")