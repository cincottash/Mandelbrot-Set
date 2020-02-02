import time
import random
from initializeThreads import *

def main():

	start_time = time.time()

	for numThread in threadList:
		numThread.start()

	for numThread in threadList:
		numThread.join()
	
	print("--- Completed in %s seconds with threads %d running ---" % (time.time() - start_time, len(threadList)))

	while True:
		pygame.display.update()

if __name__ == '__main__':
	initializeThreads()
	main()

