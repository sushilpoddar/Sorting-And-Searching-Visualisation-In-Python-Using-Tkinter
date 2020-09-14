"""
	Algorithm	|				Time Complexity
				|	Best(omega notation)	|    Average(theta notation)	|	Worst(bigO notation)

Merge Sort		|	Ω(n log(n))				|	θ(n log(n))					|	O(n log(n))

	Merge sort –
	Best, average and worst case time complexity: nlogn which is independent of distribution of data.
"""
import time


def Merge_sort(data, drawData, stopTime):
	merge_sort_algo(data, 0, len(data) - 1, drawData, stopTime)


def merge_sort_algo(data, left, right, drawData, stopTime):
	if left < right:
		middle = (left + right) // 2
		merge_sort_algo(data, left, middle, drawData, stopTime)
		merge_sort_algo(data, middle + 1, right, drawData, stopTime)
		merge(data, left, middle, right, drawData, stopTime)


def merge(data, left, middle, right, drawData, stopTime):
	drawData(data, getColorList(len(data), left, middle, right))
	time.sleep(stopTime)

	leftPart = data[left:middle + 1]
	rightPart = data[middle + 1: right + 1]

	leftIdx = rightIdx = 0

	for dataIdx in range(left, right + 1):
		if leftIdx < len(leftPart) and rightIdx < len(rightPart):
			if leftPart[leftIdx] <= rightPart[rightIdx]:
				data[dataIdx] = leftPart[leftIdx]
				leftIdx += 1
			else:
				data[dataIdx] = rightPart[rightIdx]
				rightIdx += 1

		elif leftIdx < len(leftPart):
			data[dataIdx] = leftPart[leftIdx]
			leftIdx += 1
		else:
			data[dataIdx] = rightPart[rightIdx]
			rightIdx += 1

	drawData(data, ["green" if left <= x <= right else "white" for x in range(len(data))])
	time.sleep(stopTime)


def getColorList(leght, left, middle, right):
	colorList = []

	for i in range(leght):
		if left <= i <= right:
			if left <= i <= middle:
				colorList.append("yellow")
			else:
				colorList.append("blue")
		else:
			colorList.append("white")

	return colorList
