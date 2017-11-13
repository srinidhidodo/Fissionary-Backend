# test data
data = {
	'locations': [
		{
			'locationId': 1,
			'locationName': 'loc1',
			'latitude': '12.22',
			'longitude': '20.22',
			'places': [
				{
					'placeId': 1,
					'placeName': 'place1',
					'placeSize': 100,
					'threshold': 50,
					'latitude': '34.22',
					'longitude': '40.22',
					'placeDensity': {
						'time': '12:00',
						'density': 10
					}
				},
				{
					'placeId': 2,
					'placeName': 'place2',
					'placeSize': 200,
					'threshold': 10,
					'latitude': '11.22',
					'longitude': '80.22',
					'placeDensity': {
						'time': '20:00',
						'density': 100
					}
				}
			]
		}
	]
}

def getLocations():
	locations = data['locations']
	res = []
	for location in locations:
		res.append({'locationId':location['locationId'], 'locationName':location['locationName']})
	return res

def getLocation(locationId):
	locations = data['locations']
	for location in locations:
		if location['locationId'] == locationId:
			return location

def getPlaces(locationId):
	location = getLocation(locationId)
	places = location['places']
	return places

def getPlace(locationId, placeId):
	location = getLocation(locationId)
	places = location['places']
	for place in places:
		if place['placeId'] == placeId:
			return place

def getPlaceDensity(locationId, placeId):
	place = getPlace(locationId, placeId)
	return place['placeDensity']
