import mysql.connector
def get_db_connection():
    con = mysql.connector.connect(user='root',password='Subbu@99666',host='localhost',database='python_project',port=3306)

    return con