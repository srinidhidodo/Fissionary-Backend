from analyzer import get_location_data, get_place_data, get_place_density
from flask import Flask, redirect, url_for, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/location-details/<int:locationId>', methods=['GET'])
def location_details(locationId):
    location_data = get_location_data(locationId)
    return jsonify({'location': location_data})

@app.route('/location-details/<int:locationId>/place-details/<int:placeId>', methods=['GET'])
def place_details(locationId, placeId):
    place_data = get_place_data(locationId, placeId)
    return jsonify({'place': place_data})

@app.route('/location-details/<int:locationId>/place-details/<int:placeId>/crowd-density/', methods=['GET'])
def crowd_density(locationId, placeId):
    density = get_place_density(locationId, placeId)
    return jsonify({'density': density})


if __name__ == '__main__':
	app.debug = True
	app.run(host="127.0.0.1", port=5000)