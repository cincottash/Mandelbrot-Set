from pylab import imshow,show,gray
from numpy import zeros,linspace
import pygame
import time
import random
import threading
#math: Zn+1 = Zn + c
#c = a + bi
#c^2 = a^2 + 2abi - b^2
#Ex: Z0 = c
#Ex: Z1 = c^2 + c
#Ex: Z2 = (c^2 + c)^2 + c

pygame.init()
canvasWidth = 400
canvasHeight = 400

screen = pygame.display.set_mode((canvasWidth, canvasHeight))
def drawManelbrotSet():
	
	n = 400

	M = zeros([n,n],int)
	xvalues = linspace(-2,2,n)
	yvalues = linspace(-2,2,n)

	#u, v
	#u=0
	#v=u
	for u,x in enumerate(xvalues):
		#u+=1
		#v=0
		for v,y in enumerate(yvalues):
			#v+=1
			z = 0 + 0j
			c = complex(x,y)
			for i in range(100):
				z = z*z + c
				if abs(z) > 2.0:
					#normalizes z between 0 and 1
					normalZ = int(-255*((abs(z)/4)-1.5))
					#print(normalZ)
					screen.set_at((u, v), (normalZ, 100, 150))
					break
				screen.set_at((u, v), (0,0,0))
	while True:
		pygame.display.update()

def main():
		x = threading.Thread(target=drawManelbrotSet)
		x.start()
		#pygame.display.update()

if __name__ == '__main__':
	main()

