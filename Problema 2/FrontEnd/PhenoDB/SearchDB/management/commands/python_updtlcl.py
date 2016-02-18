import psycopg2

def connect():
	try:
	    conn = psycopg2.connect(
	    	database="Pheno",
	    	host="ec2-107-22-175-206.compute-1.amazonaws.com",
	    	port="5432",
	    	dbname="dfu5v18hea0jro",
	    	user="puxsikmrnjnnml",
	    	password="fpqWwIT73lFClOn23I1MMYpjP3")
	    cur = conn.cursor()
	    return conn,cur
	except:
	    print "I am unable to connect to the database"
	    return None, None

def update(cur):
	cur.execute("""select * FROM pheno_db""")
	rows = cur.fetchall()
	print "\nNew Database:\n"
	for row in rows:
		print [col for col in row]

def main():
	print "\nUpdating PhenoDB..."
	state,cur = connect()
	if state == None:
		return
	update(cur)	

if __name__ == "__main__":
    main()