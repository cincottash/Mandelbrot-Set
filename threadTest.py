import threading
import time

threadList = []
intList = []

def main():

	t0 = threading.Thread(target = test, args = (0,4))
	t1 = threading.Thread(target = test, args = (1,4))
	t2 = threading.Thread(target = test, args = (2,4))
	t3 = threading.Thread(target = test, args = (3,4))

	threadList.append(t0)
	threadList.append(t1)
	threadList.append(t2)
	threadList.append(t3)

def test(start, step):
	for i in range(start, 1000, step):
		intList.append(i)

if __name__ == '__main__':
	main()

	start_time = time.time()

	for thread in threadList:
		thread.start()

	for thread in threadList:
		thread.join()

	print("--- Completed in %s seconds with %d threads running ---" % (time.time() - start_time, len(threadList)))
