import cv2
import numpy as np

def findCrowdedArea(image):
	#Boundaries for color red
	boundaries = [([17, 15, 100], [50, 56, 200])]
	for (lower, upper) in boundaries:
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
		# find the colors within the specified boundaries and apply the mask
		mask = cv2.inRange(image, lower, upper)
		output = cv2.bitwise_and(image, image, mask = mask)
	
	imgray = cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)
	im2,contours, hier = cv2.findContours(imgray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	backtorgb=cv2.cvtColor(imgray,cv2.COLOR_GRAY2RGB)

	area=[]
	for cnt in contours:
		area.append(cv2.contourArea(cnt))
	l=sorted(area,reverse=True)
	print("HELLO:",l)
	i=1
	sumred=0
	for cnt in contours:
		cv2.drawContours(backtorgb,[cnt], 0, (0,0,255), 2)
		if(cv2.contourArea(cnt)!=l[0] and cv2.contourArea(cnt)!=0):
			print("Contour number: ",i," Contour Area: ",cv2.contourArea(cnt)," \n")
			sumred+=cv2.contourArea(cnt)
			i+=1


	cv2.imshow('images',np.hstack([image,backtorgb]))
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	return sumred

if __name__ == "__main__":  
	image=cv2.imread('heatmap2.jpg')
	image = np.uint8(image)
	total=findCrowdedArea(image)
	print("The total area of red components are: ",total)	
