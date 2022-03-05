from pyCPN import PyCPN
from pyEncodeDecode import stringEncode, stringDecode

# Tested with Python v 3.7.2 and CPN Tools v 4.0.1
# For use with processCityServer.cpn example net

port = 9999
host = 'localhost'
conn = PyCPN()
conn.connect(host, port)

def doit():
	result = []
	for city in ['new york', 'philadelphia', 'baltimore']:
		conn.send(stringEncode(city))
		result.append(stringDecode(conn.receive()))
	conn.send(stringEncode('quit'))
	conn.disconnect()
	print(result)	

if __name__ == "__main__":
   doit()