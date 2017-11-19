from app import db

class Location(db.Model):
    __tablename__ = 'location'
    locationId = db.Column(db.Integer, primary_key=True)
    locationName = db.Column(db.Text, index=True, nullable=False)
    latitude = db.Column(db.Float, index=True, nullable=False)
    longitude = db.Column(db.Float, index=True, nullable=False)

    def __init__(self, locationId, locationName, latitude, longitude):
        self.locationId = locationId
        self.locationName = locationName
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return '<Location %r>' % (self.locationName)


class Place(db.Model):
    __tablename__ = 'place'
    placeId = db.Column(db.Integer, primary_key=True)
    placeName = db.Column(db.Text, index=True, unique=True)
    latitude = db.Column(db.Float, index=True, nullable=False)
    longitude = db.Column(db.Float, index=True, nullable=False)

    def __init__(self, placeId, placeName, latitude, longitude):
        self.placeId = placeId
        self.placeName = placeName
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return '<Place %r>' % (self.placeName)


# mapping of places and location (maps places to a location)
class LocationPlace(db.Model):
    __tablename__ = 'location_place'
    locationId = db.Column(db.Integer, db.ForeignKey('location.locationId'), primary_key=True)
    placeId = db.Column(db.Integer, db.ForeignKey('place.placeId'), primary_key=True)
    threshold = db.Column(db.Float, nullable=True)
    db.UniqueConstraint('locationId', 'placeId', name='loc_pl_uniq')

    def __init__(self, locationId, placeId, threshold):
        self.locationId = locationId
        self.placeId = placeId
        self.threshold = threshold

    def __repr__(self):
         return '<LocationPlace: location %d ; place %d>' % (self.locationId, self.placeId)

# stores density values along with time stamps for each location of a place
class CrowdTrend(db.Model):
    __tablename__ = 'crowd_trend'
    crowdTrendsId = db.Column(db.Integer, primary_key=True)
    locationId = db.Column(db.Integer, db.ForeignKey('location.locationId'), nullable=False)
    placeId = db.Column(db.Integer, db.ForeignKey('place.placeId'), nullable=False)
    timeStamp = db.Column(db.Text, nullable=False)
    crowdDensity = db.Column(db.Float, nullable=False)

    def __init__(self, locationId, placeId, timeStamp, crowdDensity):
        self.locationId = locationId
        self.placeId = placeId
        self.timeStamp = timeStamp
        self.crowdDensity = crowdDensity

    def __repr__(self):
        return '<CrowdTrends %d ; location %d ; place %d>' % (self.crowdTrendsId, self.locationId, self.placeId)