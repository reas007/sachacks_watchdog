import smartcar 

def emergency_protocol(problem):
	# Fetch the set of vehicles associated with this access
	response = smartcar.get_vehicle_ids("3faba1e4-3cbe-4f39-988d-896b80a0db6a")
	print(response)

	# Use the first vehicle
	vehicle = smartcar.Vehicle(response['vehicles'][0], "3faba1e4-3cbe-4f39-988d-896b80a0db6a")

	# Fetch the vehicle's location
	location = vehicle.location()
	print(location)

	#lock the vehicle
	vehicle.lock()

problem = True
emergency_protocol(problem)