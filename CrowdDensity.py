from HeatMap import HeatMap
import HeatMapDensity
import threading
import database
import time

class CrowdDensity:
	@staticmethod
	def getCrowdArea(locationId, placeId):
		try:
			heatMapImage = HeatMapDensity.readHeatMap(locationId, placeId)
			density = HeatMapDensity.getCrowdArea(heatMapImage)
		except:
			print 'Error in calculating crowd area'
			print 'Check location and place ID'
			density = -1

		return density

	@staticmethod
	def getPlaceDensity(locationId, placeId):
		try:
			heatMapImage = HeatMapDensity.readHeatMap(locationId, placeId)
			density = HeatMapDensity.findHeatMapDensity(heatMapImage)
		except:
			print 'Error in calculating crowd density'
			print 'Check location and place ID'
			density = -1

		return density

def getLocationPlaces():
    f1 = open('db_config_data/config_place.txt','r')
    res = []
    for line in f1.readlines():
        fields = line.strip().split(';')
        locationId = fields[0]
        placeId = fields[1]
        res.append([locationId, placeId])
    return res

locationPlaces = getLocationPlaces()
oldDensities = {}

def updateDensityValues():
	def updateDensities():
			global locationPlaces
			global oldDensities
			threading.Timer(40.0, updateDensities).start()
			# update values
			for x in locationPlaces:
				locationId = x[0]
				placeId = x[1]
				area = CrowdDensity.getCrowdArea(locationId, placeId)
				density = CrowdDensity.getPlaceDensity(locationId, placeId)
				if density == -1:
					density = oldDensities[locationId][placeId][1]
				t = time.ctime()
				database.addCrowdTrend(locationId, placeId, t, density)
				oldDensities[locationId] = {}
				oldDensities[locationId][placeId] = [t, density]
			print 'Density values updated'
	updateDensities()

if __name__ == '__main__':
	#area = CrowdDensity.getCrowdArea(1, 1)
	#density = CrowdDensity.getPlaceDensity(1, 1)
	#print 'crowd density of place: %f' % (density)
	updateDensityValues()
