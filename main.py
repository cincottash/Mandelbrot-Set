import pygame
import random

pygame.init()

canvasWidth = 200
canvasHeight = 200
endlessLoop = 1

def main():

	screen = pygame.display.set_mode((canvasWidth, canvasHeight))

	while endlessLoop:
		for i in range(canvasWidth):
			for j in range(canvasHeight):
				screen.set_at((i, j), (100,100,100))
				pygame.display.update()

if __name__ == '__main__':
	main()