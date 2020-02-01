from pylab import imshow,show,gray
from numpy import zeros,linspace
import pygame
import time
import random
import math

#math: Zn+1 = Zn + c
#c = a + bi
#c^2 = a^2 + 2abi - b^2
#Ex: Z0 = c
#Ex: Z1 = c^2 + c
#Ex: Z2 = (c^2 + c)^2 + c

pygame.init()
canvasWidth = 600
canvasHeight = 600


def main():
	screen = pygame.display.set_mode((canvasWidth, canvasHeight))
	n= 600

	M = zeros([n,n],int)
	xvalues = linspace(-2,1,n)
	yvalues = linspace(-2,1,n)

	for u,x in enumerate(xvalues):
		for v,y in enumerate(yvalues):

			z = 0 + 0j
			c = complex(x,y)

			red = 255
			green = 255
			blue = 255

			for i in range(0,100):
				prev_z = z
				z = z*z + c
				if abs(z) > 2.0:

					new_red =
					red =
					new_green =
					green =
					new_blue =
					blue =

					# print(z.real)
					print('{r} {g} {b}'.format(r=new_red,g=new_green,b=new_blue))

					screen.set_at((u, v),(red,green,blue))
					break

				screen.set_at((u, v), (0,0,0))


	pygame.display.update()
	time.sleep(100)






if __name__ == '__main__':
	main()
