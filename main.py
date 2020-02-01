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
			red = 111
			green = 1
			blue = 234
			global total_counter
			total_counter = 0
			decay_multiplier = 1000 * total_counter
			for i in range(100):
				z = z*z + c
				if abs(z) > 2.0:
					global total_counter
					# print(int(255/((abs(z) % 3) + 1)))
					new_red,new_green,new_blue = red * decay_multiplier,int(1 - (green / decay_multiplier)),blue + decay_multiplier
					screen.set_at((u, v), (int((new_red % 255) % 255) + 1,int((new_green % 255) % 255) + 1,int((new_blue % 255) % 255) + 1)
					total_counter += 1
					break
				screen.set_at((u, v), (0,0,0))
	pygame.display.update()
	time.sleep(100)






if __name__ == '__main__':
	main()
