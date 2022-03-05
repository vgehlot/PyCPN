from pyCPN import PyCPN
from pyEncodeDecode import stringEncode, stringDecode

# Tested with Python v 3.7.2 and CPN Tools v 4.0.1
# For use with HelloNameCPNComm.cpn example net

port = 9999
host = 'localhost'
conn = PyCPN()
conn.connect(host, port)

def doit():
	while True:
		resp = input("Type your name or type quit: ")
		conn.send(stringEncode(resp))
		if resp == 'quit':
			conn.disconnect()
			break
		else:
			msg = stringDecode(conn.receive())
			print(msg)		

if __name__ == "__main__":
   doit()