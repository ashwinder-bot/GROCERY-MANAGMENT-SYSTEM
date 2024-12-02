import mysql.connector 

__cnx = None



def get_sql_connection():
    global __cnx
    if __cnx is None:

     cnx=mysql.connector.connect(user='root', password='Ashi2007@#',
                            host='127.0.0.1',
                            database='gs')
     return cnx