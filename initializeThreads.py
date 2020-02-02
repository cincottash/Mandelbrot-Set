import threading
from drawMandelbrotSet import *

threadList = []

def initializeThreads():

	t0 = threading.Thread(target=drawMandelbrotSet, args= (0,4))
	t1 = threading.Thread(target=drawMandelbrotSet, args= (1,4))
	t2 = threading.Thread(target=drawMandelbrotSet, args= (2,4))
	t3 = threading.Thread(target=drawMandelbrotSet, args= (3,4))

	threadList.append(t0)
	threadList.append(t1)
	threadList.append(t2)
	threadList.append(t3)
