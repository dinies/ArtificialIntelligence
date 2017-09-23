import MySQLdb

db = MySQLdb.connect("localhost","chesstester","chesstester","chessqtest")

create_q="CREATE TABLE PROVA (ID INTEGER PRIMARY KEY AUTO_INCREMENT,STATE VARCHAR(100) NOT NULL,ACTION VARCHAR(20) NOT NULL,REWARD INT)"

ins_q="INSERT INTO PROVA(STATE,ACTION,REWARD)VALUES(%s,%s,%s)"

cursor = db.cursor()
	
cursor.execute(create_q)
	
state_str="1k1/ppp/111/111/PPP/1K1"
action_str="K.a2-a3"

try:
	cursor.execute(ins_q, (state_str,action_str, str(3)))
	db.commit()
	print ("c'e l'ho fatta2")
except:
	db.rollback()
	print("nada2")

db.close()