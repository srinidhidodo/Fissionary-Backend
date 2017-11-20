import database

# test data - for testing purpose
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
	res = []
	locations = database.getAllLocations()
	for location in locations:
		res.append({'locationId':int(location[0]), 'locationName':location[1]})
	return res

def getLocation(locationId):
	location = database.queryLocation(locationId)[0]
	res = {'latitude':location[2], 'longitude':location[3], 'locationName':location[1], 'locationId':int(location[0])}
	places = getPlaces_(locationId)
	pl = []
	for place in places:
		density = getPlaceDensity_(locationId, place[0])
		density = density[-1]
		density = {'density': density[3], 'time': density[2]}
		threshold = database.getThreshold(locationId, place[0])[0][2]
		pl.append({'latitude':place[2], 'longitude':place[3], 'placeId':int(place[0]), 'placeName':place[1], 'threshold':threshold, 'placeDensity': density})
	res['places'] = pl
	return res

def getPlaces_(locationId):
	return database.getPlaces(locationId)

def getPlace_(locationId, placeId):
	return database.getPlace(locationId,placeId)

def getPlaceDensity_(locationId, placeId):
	return database.getPlaceDensity(locationId, placeId)

def getPlaces(locationId):
	location = getLocation(locationId)
	places = location['places']
	return places

def getPlace(locationId, placeId):
	location = getLocation(locationId)
	places = location['places']
	for place in places:
		if int(place['placeId']) == int(placeId):
			return place

def getPlaceDensity(locationId, placeId):
	place = getPlace(locationId, placeId)
	return place['placeDensity']
