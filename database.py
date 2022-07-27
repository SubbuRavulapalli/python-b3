# 1.Create a common function to get database connection
# def database():
#     import mysql.connector
#
#     conn = mysql.connector.connect(user='root',
#                                    password='Subbu@99666',
#                                    host='localhost',
#                                    database='python_project', port=3306)
#     cursor = conn.cursor()
#
#
#
#     print(conn)
#
#     conn.close()
#
# database()



# 2.Create a program to create customers table with all fields from python code and insert 4 records
# import mysql.connector
# conn = mysql.connector.connect(user='root',
#                                password='Subbu@99666',
#                                host='localhost',
#                                database='python_project',
#                                port=3306)
# cursor=conn.cursor()
# #cursor.execute("create table cust_details(cust_id integer(5) not null,fst_name varchar(20) not null,last_name varchar(20) not null,address varchar(30))")
# sql = "insert into cust_details(cust_id, fst_name, last_name,address) VALUES(%s, %s, %s, %s)"
# records = [(123, 'Subbu', 'ravulapalli', 'vinukonda'),
#            (112, 'kasi', 'yedumati', 'ongole'),
#            (113, 'nagaraj', 'mutyala', 'podili')]
#
# cursor.executemany(sql, records)
# conn.commit()
# print("Records Inserted Successfully...")
#
# cursor.execute("select * from employees")
# data = cursor.fetchall()
# print("data from db ", data)
# conn.close()
#
#
#
#






# 3.Select all the records from customers table
# import mysql.connector
# conn = mysql.connector.connect(user='root',
#                                password='Subbu@99666',
#                                host='localhost',
#                                database='python_project',
#                                port=3306)
# cursor = conn.cursor()
#
# cursor.execute('select * from cust_details;')
# data = cursor.fetchall()
# print('data from db',data)
# conn.close()


# 4.Update customer pincode for all the customers whose address is ongole
import mysql.connector
from DBConnection import *

conn=get_db_connection()
conn = mysql.connector.connect(user = 'root',
                               password='Subbu@99666',
                               host='localhost',
                               database='python_project',
                               port=3306)
cursor = conn.cursor()
cursor.execute('update cust_details set address="pincode" where cust_id=112 ')

data = cursor.fetchall()
print('data from db',data)
conn.close()