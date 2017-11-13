from analyzer import getLocations, getLocation, getPlaces, getPlace, getPlaceDensity
from flask import Flask, redirect, url_for, request, render_template, jsonify, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')

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
    filename = 'images\l%d_p%d.png' % (locationId, placeId)
    return send_file(filename, mimetype='image/png')

if __name__ == '__main__':
	app.debug = True
	app.run(host="127.0.0.1", port=5000)