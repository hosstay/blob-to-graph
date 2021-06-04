import mysql.connector
from mysql.connector import Error
from sys import exit
from binascii import hexlify, a2b_hex
import matplotlib.pyplot as plt

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

def convertBlobDataToIntArray(data):
  # hex encode blob data so it looks like proper hex
  hex_encoded_bytes_from_blob = hexlify(data)

  # convert hex byte string into string
  hexstring = ''.join(map(chr, hex_encoded_bytes_from_blob))

  # make an array of 4 byte hex strings from full hex string
  hexstring_byte_array = [hexstring[i: i + 8] for i in range(0, len(hexstring), 8)]

  int_array = []
  for y in hexstring_byte_array:
    y = convert4byteHexStrToSigned32BitInt(y)
    y = y / 1000
    int_array.append(y)

  return int_array

def convert4byteHexStrToSigned32BitInt(h):
  b = bytes(h, 'utf-8')
  ba = a2b_hex(b)
  return int.from_bytes(ba, byteorder='big', signed=True)

if __name__ == '__main__':
  conn = connect()

  result = run_query(conn, 'SELECT * FROM test ORDER BY trace_id;')

  while(True):
    for x in result:
      trace_data = x[1]
      trace_time = x[2]

      timestamp = 'Trace Time: ' + trace_time.strftime('%m/%d/%Y %H:%M:%S %p')

      int_array = convertBlobDataToIntArray(trace_data)

      index_array = list(range(1, len(int_array) + 1))

      plt.plot(index_array, int_array)
      plt.ylim(-130, -30)
      plt.xlabel('Index')
      plt.ylabel('Magnitude')
      plt.title('Magnitude Over Index')
      plt.text(150, -120, timestamp)
      plt.draw()
      plt.pause(1)
      plt.clf()

    print('End of firm loop, starting again')

  # never gets called because program is intentionally an infinite loop
  disconnect(conn)