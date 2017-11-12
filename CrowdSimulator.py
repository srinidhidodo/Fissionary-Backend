import random
from HeatMap import HeatMap

# simulate crowd by generating coordinates representing people
class CrowdSimulator:
	# height and width of the place (same as that of image captured by cameras)
	# changerate - rate at which ppl move out of the place
	def __init__(self, heatmap, sizeX=1024, sizeY=1024, changeRate=10):
		self.sizeX = sizeX
		self.sizeY = sizeY
		self.changeRate = changeRate
		self.heatmap = heatmap
		self.imageNum = 1
		self.generateCrowd()

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
	def generateCrowd(self, threshold=0.5):
		self.crowd = []
		for x in range(self.sizeX):
			for y in range(self.sizeY):
				probability = self.getCellProbability(x,y)
				if probability > threshold:
					self.crowd.append((x,y))

	def getCrowdSimulator(self, saveImage=False, imageName="sampleHeatMap"):
		while True:
			if saveImage:
				img = self.heatmap.generateHeatMapImage(self.crowd, imageName)
			else:
				img = self.heatmap.generateHeatMap(self.crowd)
			yield img
			self.imageNum += 1
			threshold = random.uniform(0.4, 0.6)
			self.generateCrowd(threshold)



if __name__ == "__main__":    
	heatmap = HeatMap()
	crowd = CrowdSimulator(heatmap, 100,100)
	simulator = crowd.getCrowdSimulator(True)
	for i in range(1):
		simulator.next()
		
	
	'''
	heatmap = HeatMap()
	crowd = CrowdSimulator(heatmap, 100,100)
	#print crowd.getNextCrowdSimulation()
	hmap = crowd.generateHeatMap(heatmap)
	print hmap
	'''



