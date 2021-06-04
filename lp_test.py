import mysql.connector
from mysql.connector import Error
from sys import exit
from binascii import hexlify, a2b_hex

def connect():
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

  except Error as e:
    print(e)

  finally:
    return conn

def disconnect(conn):
  if conn is not None and conn.is_connected():
    conn.close()
    print('Closed mySQL database')

def run_query(conn, query):
  try:
    cursor = conn.cursor()
    cursor.execute(query)
 
    return cursor.fetchall()

  except Error as e:
    print(e)
    cursor.close()
    exit()

def convert4byteHexStrToSigned32BitInt(h):
  b = bytes(h, 'utf-8')
  ba = a2b_hex(b)
  return int.from_bytes(ba, byteorder='big', signed=True)

if __name__ == '__main__':
  conn = connect()

  result = run_query(conn, 'SELECT * FROM test ORDER BY trace_id;')

  hex_encoded_bytes_from_blob = hexlify(result[0][1])
  hexstring = ''.join(map(chr, hex_encoded_bytes_from_blob))
  
  hexstring_byte_array = [hexstring[i: i + 8] for i in range(0, len(hexstring), 8)]

  int_array = []
  for y in hexstring_byte_array:
    y = convert4byteHexStrToSigned32BitInt(y)
    y = y / 1000
    int_array.append(y)

  print(int_array)

  disconnect(conn)