# test data
data = {
	'locations': [
		{
			'locationId': 1,
			'locationName': 'loc1',
			'places': [
				{
					'placeId': 1,
					'placeName': 'place1',
					'placeSize': 100,
					'threshold': 50,
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
					'placeDensity': {
						'time': '20:00',
						'density': 100
					}
				}
			]
		}
	]
}

def get_location_data(locationId):
	locations = data['locations']
	for location in locations:
		if location['locationId'] == locationId:
			return location

def get_place_data(locationId, placeId):
	location = get_location_data(locationId)
	places = location['places']
	for place in places:
		if place['placeId'] == placeId:
			return place

def get_place_density(locationId, placeId):
	place = get_place_data(locationId, placeId)
	return place['placeDensity']


def get_tasks():
    return jsonify({'tasks': tasks})