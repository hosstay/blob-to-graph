import mysql.connector
from mysql.connector import Error
from sys import exit

if __name__ == '__main__':
  conn = None
  try:
    conn = mysql.connector.connect(
      host='localhost',
      database='lp_test',
      user='root',
      password='password'
    )

    if conn.is_connected():
      print('Connected to MySQL database')

      try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM test ORDER BY trace_id;')
    
        print(cursor.fetchall())

      except Error as e:
        print(e)
        cursor.close()
        exit()

  except Error as e:
    print(e)

  finally:
    if conn is not None and conn.is_connected():
      conn.close()
      print('Closed mySQL database')