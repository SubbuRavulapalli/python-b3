import csv

import mysql.connector
from DBConnection import *

try:

    con = get_db_connection()
    cursor=con.cursor()
    cursor.execute("select * from emp_info")
    data=cursor.fetchall()
    print('data from db',data)
    with open("out.csv","w",newline='') as csv_file:
        csv_writer=csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(data)

except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
    print('there is a problem with sql',e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()


