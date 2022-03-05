from pyCPN import PyCPN
from pyEncodeDecode import stringEncode, stringDecode

# Tested with Python v 3.7.2 and CPN Tools v 4.0.1
# Server for use with processCityClient.cpn model example

port = 9999
conn = PyCPN()
conn.accept(port)

def doit():
	while True:
		city = stringDecode(conn.receive())
		if city == 'quit':
			conn.disconnect()
			break
		else:
			conn.send(stringEncode(city.upper()))	

if __name__ == "__main__":
   doit()