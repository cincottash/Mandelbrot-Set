from pylab import imshow,show,gray
from numpy import zeros,linspace
import pygame
import time
import random
import threading
import time

def drawMandelbrotSet(start, step):
	xValuesList = []
	yValuesList = []
	n = 400

	M = zeros([n,n],int)
	xvalues = linspace(-2,2,n)
	yvalues = linspace(-2,2,n)

	#Values are eaiser to work with if they are in a list
	for i in xvalues:
		xValuesList.append(i)

	for i in yvalues:
		yValuesList.append(i)

	u=start
	#TODO: Make thread 1 do half the for loop and thread 2 do the other half
	for x in range(start, n, step):
		u+=step
		v=0
		for y in range(n):
			v+=1
			z = 0 + 0j
			c = complex(xValuesList[x], yValuesList[y])
			for i in range(100):
				z = z*z + c
				if abs(z) > 2.0:
					#normalizes z between 0 and 255
					normalZ = int(-255*((abs(z)/4)-1.5))
					screen.set_at((u, v), (normalZ, normalZ-0, normalZ-0))
					break
				screen.set_at((u, v), (0,0,0))
	#while True:
		#pygame.display.update()

pygame.init()
canvasWidth = 400
canvasHeight = 400
screen = pygame.display.set_mode((canvasWidth, canvasHeight))

threadList = []
t0 = threading.Thread(target=drawMandelbrotSet, args= (0,1))
# t1 = threading.Thread(target=drawManelbrotSet, args= (1,4))
# t2 = threading.Thread(target=drawManelbrotSet, args= (2,4))
# t3 = threading.Thread(target=drawManelbrotSet, args= (3,4))

threadList.append(t0)
# threadList.append(t1)
# threadList.append(t2)
# threadList.append(t3)



def main():

	start_time = time.time()

	for numThread in threadList:
		numThread.start()

	for numThread in threadList:
		numThread.join()
	
	print("--- %s seconds ---" % (time.time() - start_time))

	while True:
		pygame.display.update()


if __name__ == '__main__':
	main()

