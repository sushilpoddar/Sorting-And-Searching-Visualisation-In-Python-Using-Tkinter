import time


def LinearSearch(data, findValue, drawData, stopTime):
	for index in range(len(data)):
		drawData(data, ['yellow' if i == index else 'red' for i in range(len(data))])
		time.sleep(stopTime)
		if data[index] == findValue:
			colorList = ['green' if data[i] == findValue else 'red' for i in range(len(data))]
			drawData(data, colorList)
			time.sleep(stopTime)
			return [True, colorList.index('green')]

	return [False]
