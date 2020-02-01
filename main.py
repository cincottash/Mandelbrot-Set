import pygame

pygame.init()

canvasWidth = 1920
canvasHeight = 1080

background = pygame.image.load("assets/background.jpg")

canvas = pygame.display.set_mode((canvasWidth,canvasHeight))
#pygame.display.set_caption('Space')

endlessLoop = 1

def main():

	while endlessLoop:
		#reset the background
		canvas.blit(background, (0,0))
			

		#"Commit" the changes
		pygame.display.update()



if __name__ == '__main__':
	main()