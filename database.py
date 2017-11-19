from models import Location, Place, LocationPlace, CrowdTrend
from sqlalchemy import and_, or_, not_
from app import db

# Location Table Operations

def getAllLocations():
    locations = Location.query.all()
    return locations

def createLocation(locationId, locationName, latitude, longitude):
    location = Location(locationId, locationName, latitude, longitude)
    db.session.add(location)
    db.session.commit()

def deleteLocation(locationId, locationName, latitude, longitude):
    location = Location(locationId, locationName, latitude, longitude)
    db.session.delete(location)
    db.session.commit()

def queryLocationById(locationId):
    locations = Location.query.filter_by(locationId = locationId).all()
    return locations

def queryLocationByName(locationName):
    locations = Location.query.filter_by(locationName = locationName).all()
    return locations

def queryLocationByLatLong(latitude, longitude):
    locations = meta.Session.query(Location).filter(
        and_(
            Location.latitude(latitude),
            Location.longitude(longitude)
        )
    )
    return locations


# Place Table Operations

def getAllPlaces():
    places = Place.query.all()
    return places

def createPlace(placeId, placeName, latitude, longitude):
    place = Place(placeId, placeName, latitude, longitude)
    db.session.add(place)
    db.session.commit()

def deletePlace(placeId, placeName, latitude, longitude):
    place = Place(placeId, placeName, latitude, longitude)
    db.session.delete(place)
    db.session.commit()

def queryPlaceById(placeId):
    places = Place.query.filter_by(placeId = placeId).all()
    return places

def queryPlaceByName(placeName):
    places = Place.query.filter_by(placeName = placeName).all()
    return places

def queryPlaceByLatLong(latitude, longitude):
    places = meta.Session.query(Place).filter(
        and_(
            Place.latitude(latitude),
            Place.longitude(longitude)
        )
    )
    return places


# LocationPlace Table Operations

def getAllLocationPlaces():
    locationPlaces = LocationPlace.query.all()
    return locationPlaces

def createLocationPlace(locationId, placeId, threshold):
    locationPlace = LocationPlace(locationId, placeId, threshold)
    db.session.add(locationPlace)
    db.session.commit()

def deleteLocationPlace(locationId, placeId, threshold):
    locationPlace = LocationPlace(locationId, placeId, threshold)
    db.session.delete(locationPlace)
    db.session.commit()


# CrowdTrends Table Operations

def getAllCrowdTrends():
    crowdTrends = CrowdTrend.query.all()
    return crowdTrends

def createCrowdTrend(locationId, placeId, timeStamp, crowdDensity):
    crowdTrend = CrowdTrend(locationId, placeId, timeStamp, crowdDensity)
    db.session.add(crowdTrend)
    db.session.commit()

def deleteCrowdTrend(locationId, placeId, timeStamp, crowdDensity):
    crowdTrend = CrowdTrend(locationId, placeId, timeStamp, crowdDensity)
    db.session.delete(crowdTrend)
    db.session.commit()

def getCrowdTrends(locationId, placeId):
    crowdTrends = meta.Session.query(CrowdTrend).filter(
        and_(
            CrowdTrend.locationId(locationId),
            CrowdTrend.placeId(placeId)
        )
    )
    return crowdTrends

def getCrowdTrendByTime(locationId, placeId, timeStamp):
    crowdTrends = meta.Session.query(CrowdTrend).filter(
        and_(
            CrowdTrend.locationId(locationId),
            CrowdTrend.placeId(placeId),
            CrowdTrend.timeStamp(timeStamp)
        )
    )
    return crowdTrends