from numpy import zeros,linspace
import pygame

pygame.init()
canvasWidth = 400
canvasHeight = 400
screen = pygame.display.set_mode((canvasWidth, canvasHeight))

def drawMandelbrotSet(start, step):
	n = canvasWidth

	#Make n equally spaced values between -2 and 2
	xValuesList = list(linspace(-2, 2, n))
	yValuesList = list(linspace(-2, 2, n))

	u=start
	for x in range(start, n, step):
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
					screen.set_at((u, v), (normalZ, normalZ, normalZ))
					break
				screen.set_at((u, v), (0,0,0))
		u+=step