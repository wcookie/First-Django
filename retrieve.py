
import psycopg2
import sys


con = None

try:
     
    con = psycopg2.connect("dbname='newdb' user='wyatt'") 
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM Test")

    rows = cur.fetchall()

    for row in rows:
        print (row)
    

except psycopg2.DatabaseError as e:
    print ('Error %s' % e)    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()

