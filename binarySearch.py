import time


def BinarySearch(data, findValue, drawData, stopTime):
	low = 0
	high = len(data)-1
	drawData(data, ['blue' if i == low or i == high else 'red' for i in range(len(data))])
	time.sleep(stopTime)
	while low <= high:
		mid = (low + high) // 2
		drawData(data, ['yellow' if i == mid else 'red' for i in range(len(data))])
		time.sleep(stopTime)
		if findValue > data[mid]:
			low = mid + 1
			pass
		elif findValue < data[mid]:
			high = mid - 1
			pass
		else:
			colorList = ['green' if data[i] == findValue else 'red' for i in range(len(data))]
			drawData(data, colorList)
			time.sleep(stopTime)
			return [True, colorList.index('green')]

	return [False]
