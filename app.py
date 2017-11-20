from analyzer import getLocations, getLocation, getPlaces, getPlace, getPlaceDensity
from flask import Flask, redirect, url_for, request, render_template, jsonify, send_file, session
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import time
import CrowdSimulator

# initialize app and db
app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)
'''
import initdb
import dbinfo
import database
import db_cleartables
'''

# URL Mappings
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/admin')
def adminPage():
    return render_template('admin.html')

@app.route('/location/lid/<int:locationId>', methods=['GET'])
def locationPage(locationId):
    return render_template('location.html', locationId=locationId)

@app.route('/place/lid/<int:locationId>/pid/<int:placeId>', methods=['GET'])
def placePage(locationId, placeId):
    return render_template('place.html', locationId=locationId, placeId=placeId)

@app.route('/admin/initdb')
def initDatabase():
    initdb.initDatabaseFromConfig()
    return render_template('admin.html')

@app.route('/admin/cleardb')
def clearDatabase():
    db_cleartables.clear_data(session)
    return render_template('admin.html')


@app.route('/admin/dbdata')
def showDbInfo():
    #initdb.initDatabaseFromConfig()
    global db
    dbinfo.dbinfo(db)
    return render_template('admin.html')

@app.route('/locations', methods=['GET'])
def locationDetails():
    locationData = getLocations()
    return jsonify({'locations': locationData})

@app.route('/locations/<int:locationId>', methods=['GET'])
def locationDetail(locationId):
    locationData = getLocation(locationId)
    return jsonify({'location': locationData})

@app.route('/locations/<int:locationId>/places', methods=['GET'])
def placeDetails(locationId):
    placeData = getPlaces(locationId)
    return jsonify({'places': placeData})

@app.route('/locations/<int:locationId>/places/<int:placeId>', methods=['GET'])
def placeDetail(locationId, placeId):
    placeData = getPlace(locationId, placeId)
    return jsonify({'place': placeData})

@app.route('/locations/<int:locationId>/places/<int:placeId>/crowdDensity/', methods=['GET'])
def crowdDensity(locationId, placeId):
    density = getPlaceDensity(locationId, placeId)
    return jsonify({'density': density})

@app.route('/heatmap/location/<int:locationId>/place/<int:placeId>', methods=['GET'])
def getHeatMap(locationId, placeId):
    filename = 'heatmaps\l%d_p%d.png' % (locationId, placeId)
    return send_file(filename, mimetype='image/png')


if __name__ == '__main__':
    app.debug = True
    app.run(host="127.0.0.1", port=5000)