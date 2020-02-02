from pylab import imshow,show,gray
from numpy import zeros,linspace
import pygame
pygame.init()
canvasWidth = 400
canvasHeight = 400
screen = pygame.display.set_mode((canvasWidth, canvasHeight))
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