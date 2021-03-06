import heatmap
import random
from PIL import Image

class HeatMap: 
	# dotsize - size of each dot on the map
	def __init__(self, imageHeight=1024, imageWidth=1024, dotSize=150):
		self.hm = heatmap.Heatmap()
		self.imageHeight = imageHeight
		self.imageWidth = imageWidth
		self.dotSize = dotSize

	def generateHeatMap(self, crowdPoints):
		img = self.hm.heatmap(crowdPoints, dotsize=self.dotSize, opacity=255, size=(self.imageWidth, self.imageHeight), scheme='classic', area=None)
		return img

	def generateHeatMapImage(self, crowdPoints, imageName="sampleHeatMap"):
		img = self.generateHeatMap(crowdPoints)
		img.save('heatmaps/' + imageName + '.png')
		print 'Updated Heatmap Image'
		return img


if __name__ == "__main__":    
	pts = []
	'''for x in range(400):
	pts.append((random.random(), random.random() ))
	print pts'''
	print "Processing %d points..." % len(pts)
	pts=[]
	for i in range(150):
		pts.append((0,0))
	for i in range(100):
		pts.append((100+i,100+i))
	for i in range(150):
		pts.append((0,0))
	hm = heatmap.Heatmap()
	img = hm.heatmap(pts, dotsize=150, opacity=128, size=(1024, 1024), scheme='classic', area=None)
	img.save("classic.png")