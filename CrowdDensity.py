from HeatMap import HeatMap
import HeatMapDensity


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

if __name__ == '__main__':
	area = CrowdDensity.getCrowdArea(1, 1)
	density = CrowdDensity.getPlaceDensity(1, 1)
	print 'crowd density of place: %f' % (density)

