import smartcar 
from twilio.rest import Client

def emergency_protocol(problem):
	# Fetch the set of vehicles associated with this access
	response = smartcar.get_vehicle_ids("2252fdd5-cb00-4e0c-8a3c-57ddb5b80d46")
	print(response)

	# Use the first vehicle
	vehicle = smartcar.Vehicle(response['vehicles'][0], "2252fdd5-cb00-4e0c-8a3c-57ddb5b80d46")

	# Fetch the vehicle's location
	location = vehicle.location()
	print(location)

	#lock the vehicle
	vehicle.lock()


	#texting functionality

	account_sid = 'AC48e29bfc8e2d0e9e7db0ed92cd8333ee'
	auth_token = '063956022336f601b581f2ab668bc9e6'
	client = Client(account_sid, auth_token)

	message = client.messages.create(
	                              body="Hello, you are receiving a crime tip from WatchDog.io. We are reporting a suspicious incident at Longitude: " + str(location['data']['longitude']) + ", \n Latitude: " + str(location['data']['latitude']) + " at " + str(location['age']),
	                              from_='+14159645713',
	                              media_url='https://media.wnyc.org/i/800/0/c/85/1/AP_880772131965.jpg',
	                              to='+15106314908'
	                          )

	print(message.sid)

problem = True
emergency_protocol(problem)