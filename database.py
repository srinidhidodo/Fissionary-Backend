import sqlite3
conn= sqlite3.connect('database.db', detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread = False)

# Location Table Operations

def getAllLocations():
    c = conn.cursor()
    c.execute('''SELECT * FROM LOCATION''')
    r = c.fetchall()
    return r

def queryLocation(locationId):
    c = conn.cursor()
    w = (locationId,)
    c.execute('''SELECT * FROM LOCATION WHERE lid=?''',w)
    r = c.fetchall()
    return r

def createLocation(locationId, locationName, latitude, longitude):
    c = conn.cursor()
    w = (locationId, locationName, latitude, longitude,)
    c.execute('''INSERT INTO LOCATION VALUES(?,?,?,?)''',w)
    conn.commit()

def deleteLocation(locationId, locationName, latitude, longitude):
    c = conn.cursor()
    w = (locationId,)
    c.execute('''DELETE FROM LOCATION WHERE lid=?''',w)
    conn.commit()

def queryLocationById(locationId):
    c = conn.cursor()
    w = (locationId,)
    c.execute('''SELECT * FROM LOCATION WHERE lid=?''',w)
    r = c.fetchall()
    return r

def queryLocationByName(locationName):
    c = conn.cursor()
    w = (locationName,)
    c.execute('''SELECT * FROM LOCATION WHERE lname=?''',w)
    r = c.fetchall()
    return r

def queryLocationByLatLong(latitude, longitude):
    c = conn.cursor()
    w = (latitude, longitude,)
    c.execute('''SELECT * FROM LOCATION WHERE lat=? AND lon=?''',w)
    r = c.fetchall()
    return r


# Place Table Operations
def getAllPlaces():
    c = conn.cursor()
    c.execute('''SELECT * FROM PLACE''')
    r = c.fetchall()
    return r

def getPlaces(locationId):
    c = conn.cursor()
    w = (locationId,)
    c.execute('''SELECT * FROM PLACE WHERE pid in (SELECT pid FROM LOC_PLACE WHERE lid=?)''',w)
    r = c.fetchall()
    return r

def createPlace(placeId, placeName, latitude, longitude):
    c = conn.cursor()
    w = (placeId, placeName, latitude, longitude,)
    c.execute('''INSERT INTO PLACE VALUES(?,?,?,?)''',w)
    conn.commit()

def deletePlace(placeId, placeName, latitude, longitude):
    c = conn.cursor()
    w = (placeId,)
    c.execute('''DELETE FROM PLACE WHERE pid=?''',w)
    conn.commit()

def queryPlaceById(placeId):
    c = conn.cursor()
    w = (placeId,)
    c.execute('''SELECT * FROM PLACE WHERE pid=?''',w)
    r = c.fetchall()
    return r

def queryPlaceByName(placeName):
    c = conn.cursor()
    w = (placeName,)
    c.execute('''SELECT * FROM PLACE WHERE pname=?''',w)
    r = c.fetchall()
    return r

def queryPlaceByLatLong(latitude, longitude):
    c = conn.cursor()
    w = (latitude, longitude, )
    c.execute('''SELECT * FROM PLACE WHERE lat=? AND lon=?''',w)
    r = c.fetchall()
    return r

# LocationPlace Table Operations

def getThreshold(locationId,placeId):
    c = conn.cursor()
    w = (locationId,placeId,)
    c.execute('''SELECT * FROM LOC_PLACE WHERE lid=? AND pid=?''',w)
    r = c.fetchall()
    return r

def getPlace(locationId,placeId):
    c = conn.cursor()
    w = (locationId,placeId,)
    c.execute('''SELECT * FROM PLACE WHERE pid in (SELECT pid FROM LOC_PLACE WHERE lid=? AND pid=?)''',w)
    r = c.fetchall()
    return r

def getAllLocationPlaces():
    c = conn.cursor()
    c.execute('''SELECT * FROM LOC_PLACE''')
    r = c.fetchall()
    return r

def createLocationPlace(locationId, placeId, threshold):
    c = conn.cursor()
    w = (locationId, placeId, threshold,)
    c.execute('''INSERT INTO LOC_PLACE VALUES(?,?,?)''',w)
    conn.commit()

def deleteLocationPlace(locationId, placeId, threshold):
    c = conn.cursor()
    w = (locationId,placeId,)
    c.execute('''DELETE FROM LOC_PLACE WHERE lid=? AND pid=?''',w)
    conn.commit()

# CrowdTrends Table Operations

def getAllCrowdTrends():
    c = conn.cursor()
    c.execute('''SELECT * FROM CROWDTRENDS''')
    r = c.fetchall()
    return r

def createCrowdTrend(locationId, placeId, timeStamp, crowdDensity):
    c = conn.cursor()
    w = (locationId, placeId, timeStamp, crowdDensity)
    c.execute('''INSERT INTO CROWDTRENDS VALUES(?,?,?,?)''',w)
    conn.commit()

def deleteCrowdTrend(locationId, placeId, timeStamp, crowdDensity):
    c = conn.cursor()
    w = (locationId,placeId,timeStamp)
    c.execute('''DELETE FROM CROWDTRENDS WHERE lid=? AND pid=? AND time=?''',w)
    conn.commit()

def getCrowdTrends(locationId, placeId):
    c = conn.cursor()
    w = (locationId,placeId,)
    c.execute('''SELECT * FROM CROWDTRENDS WHERE lid=? AND pid=?''',w)
    r = c.fetchall()
    return r

def getCrowdTrendByTime(locationId, placeId, timeStamp):
    c = conn.cursor()
    w = (locationId,placeId,timeStamp,)
    c.execute('''SELECT * FROM CROWDTRENDS WHERE lid=? AND pid=? AND time=?''',w)
    r = c.fetchall()
    return r

def getPlaceDensity(locationId, placeId):
    c = conn.cursor()
    w = (locationId,placeId,)
    c.execute('''SELECT * FROM CROWDTRENDS WHERE lid=? AND pid=?''',w)
    r = c.fetchall()
    return r


def addCrowdTrend(locationId, placeId, timeStamp, crowdDensity):
    c = conn.cursor()
    w = (locationId, placeId, timeStamp, crowdDensity)
    c.execute('''INSERT INTO CROWDTRENDS VALUES(?,?,?,?)''',w)
    conn.commit()
