import database
from app import db

# for initial setup of tables in db
def initDatabaseFromConfig():
    # location table
    f1 = open('db_config_data/config_loc.txt','r')
    for line in f1.readlines():
        fields = line.strip().split(';')
        #print fields
        database.createLocation(*fields)

    # place and location_place table
    f1 = open('db_config_data/config_place.txt','r')
    for line in f1.readlines():
        fields = line.strip().split(';')
        locationId = fields[0]
        placeId = fields[1]
        placeName = fields[2]
        latitude = fields[3]
        longitude = fields[4]
        threshold = fields[5]
        #print locationId, placeId, placeName, latitude, longitude, threshold
        database.createPlace(placeId, placeName, latitude, longitude)
        database.createLocationPlace(locationId, placeId, threshold)


if __name__ == '__main__':
    initDatabaseFromConfig()


