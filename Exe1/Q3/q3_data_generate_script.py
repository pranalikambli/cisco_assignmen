import sqlite3
import random
import string

conn = sqlite3.connect('../Q1-2/router_App/db.sqlite3')
print ("Opened database successfully")
try:
   no_of_data=int(input("Enter the Value of n:"))
   stringLength=8
   letters = string.ascii_lowercase

   for row in range(no_of_data):
      sapid = ''.join(random.choice(letters) for i in range(stringLength))
      host_name = ''.join(random.choice(letters) for i in range(stringLength))
      hostname = 'www.' + host_name + '.com'
      loopback = ('127.0.0.' +str(row))
      mac = [0x00, 0x16, 0x3e,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff)]
      mac_add = ':'.join(map(lambda x: "%02x" % x, mac))
      sql = ("INSERT INTO router_info(sapid, hostname, loopback, mac_address, is_active) VALUES('{0}','{1}','{2}','{3}','{4}')").format(str(sapid), str(hostname), str(loopback), str(mac_add), 1)
      cur = conn.cursor()
      cur.execute(sql)
      conn.commit()
   print ("Operation done successfully")
except ValueError:
   print("This is not a whole number.")
finally:
   conn.close()


