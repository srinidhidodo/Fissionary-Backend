import random
from HeatMap import HeatMap

# simulate crowd by generating coordinates representing people
class CrowdSimulator:
	groundValue = 10
	highValueRange = (80,100)

	# height and width of the place (same as that of image captured by cameras)
	# changerate - rate at which ppl move out of the place
	def __init__(self, sizeX=1024, sizeY=1024, changeRate=10):
		self.sizeX = sizeX
		self.sizeY = sizeY
		self.changeRate = changeRate
		self.crowd = []
		self.initializeCrowd()

	def getCellProbability(self, x, y):
		weight = 1
		centerX = self.sizeX/2.0
		if (x,y-1) in self.crowd:
			weight+=1
		if (x+1,y-1) in self.crowd:
			weight+=1
		if (x-1,y-1) in self.crowd:
			weight+=1
		d = abs(centerX-x)+y
		if d!=0:
			probability = random.randint(1,10)*weight/(d)
		else:
			probability = 1
		#probability = random.random()
		return probability

	# assume entrance is at the top
	def initializeCrowd(self):
		for x in range(self.sizeX):
			for y in range(self.sizeY):
				probability = self.getCellProbability(x,y)
				if probability > 0.5:
					self.crowd.append((x,y))

	def getNextCrowdSimulation(self):
		pass

	def generateHeatMap(self, heatmap, imageName):
		heatmap.generateHeatMap(self.crowd, imageName)


if __name__ == "__main__":    
	crowd = CrowdSimulator(100,100)
	#print crowd.getNextCrowdSimulation()
	heatmap = HeatMap()
	crowd.generateHeatMap(heatmap, 'sample.png')