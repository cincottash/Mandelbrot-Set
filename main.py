from pylab import imshow,show,gray
from numpy import zeros,linspace
import pygame
import time
import random

#math: Zn+1 = Zn + c
#c = a + bi
#c^2 = a^2 + 2abi - b^2
#Ex: Z0 = c
#Ex: Z1 = c^2 + c
#Ex: Z2 = (c^2 + c)^2 + c

pygame.init()
canvasWidth = 400
canvasHeight = 400


def main():
	screen = pygame.display.set_mode((canvasWidth, canvasHeight))
	n= 400

	M = zeros([n,n],int)
	xvalues = linspace(-2,2,n)
	yvalues = linspace(-2,2,n)


	for u,x in enumerate(xvalues):
		for v,y in enumerate(yvalues):
			z = 0 + 0j
			c = complex(x,y)
			for i in range(100):
				z = z*z + c
				if abs(z) > 2.0:
					# print(int(255/((abs(z) % 3) + 1)))
					screen.set_at((u, v), ( , , ))
					break
				screen.set_at((u, v), (0,0,0))
	pygame.display.update()
	time.sleep(100)






if __name__ == '__main__':
	main()
