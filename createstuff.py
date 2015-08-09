import psycopg2
import sys


con = None

try:
     
    con = psycopg2.connect("dbname='newdb' user='wyatt'")   
    
    cur = con.cursor()
  
    cur.execute("CREATE TABLE Test(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)")
    cur.execute("INSERT INTO Test VALUES(1,'Audi',52642)")
    cur.execute("INSERT INTO Test VALUES(2,'Mercedes',57127)")
    cur.execute("INSERT INTO Test VALUES(3,'Skoda',9000)")
    cur.execute("INSERT INTO Test VALUES(4,'Volvo',29000)")
    cur.execute("INSERT INTO Test VALUES(5,'Bentley',350000)")
    cur.execute("INSERT INTO Test VALUES(6,'Citroen',21000)")
    cur.execute("INSERT INTO Test VALUES(7,'Hummer',41400)")
    cur.execute("INSERT INTO Test VALUES(8,'Volkswagen',21600)")
    
    con.commit()
    

except psycopg2.DatabaseError as e:
    
    if con:
        con.rollback()
    
    print( 'Error %s' % e)    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()
