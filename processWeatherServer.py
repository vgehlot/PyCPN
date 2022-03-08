import requests
from pyCPN import PyCPN
from pyEncodeDecode import stringEncode, stringDecode

# Tested with Python v 3.7.2 and CPN Tools v 4.0.1
# Server for use with processWeatherClient.cpn model example

port = 9999
conn = PyCPN()
conn.accept(port)
def doit():
	while True:
		gridXY = stringDecode(conn.receive())
		if gridXY == 'quit':
			conn.disconnect()
			break
		else:
			response = requests.get("https://api.weather.gov/gridpoints/LWX/"+gridXY+"/forecast") #96,70 for Washington Monument in Washington, D.C
			jresponse = response.json()
			temp = jresponse["properties"]["periods"][0]["temperature"]
			conn.send(stringEncode(str(temp)))
			print(temp)	

if __name__ == "__main__":
   doit()

