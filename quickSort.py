"""
	Algorithm	|				Time Complexity
				|	Best(omega notation)	|    Average(theta notation)	|	Worst(bigO notation)

Quick Sort		|	Ω(n log(n))				|	θ(n log(n))					|	O(n^2)

	Quick sort –
	It is a divide and conquer approach with recurrence relation:
	T(n) = T(k) + T(n-k-1) + cn
	Worst case: when the array is sorted or reverse sorted, the partition algorithm divides the array in two subarrays
	with 0 and n-1 elements. Therefore,

	T(n) = T(0) + T(n-1) + cn
	Solving this we get, T(n) = O(n^2)
	Best case and Average case: On an average, the partition algorithm divides the array in two subarrays with equal size.
	Therefore,

	T(n) = 2T(n/2) + cn
	Solving this we get, T(n) = O(nlogn)
"""
import time


def partition(data, head, tail, drawData, stopTime):
	border = head
	pivot = data[tail]

	drawData(data, getColorArray(len(data), head, tail, border, border))
	time.sleep(stopTime)

	for j in range(head, tail):
		if data[j] < pivot:
			drawData(data, getColorArray(len(data), head, tail, border, j, True))
			time.sleep(stopTime)

			data[border], data[j] = data[j], data[border]
			border += 1

		drawData(data, getColorArray(len(data), head, tail, border, j))
		time.sleep(stopTime)

	# swap pivot with border value
	drawData(data, getColorArray(len(data), head, tail, border, tail, True))
	time.sleep(stopTime)

	data[border], data[tail] = data[tail], data[border]

	return border


def Quick_sort(data, head, tail, drawData, stopTime):
	if head < tail:
		partitionIdx = partition(data, head, tail, drawData, stopTime)

		# LEFT PARTITION
		Quick_sort(data, head, partitionIdx - 1, drawData, stopTime)

		# RIGHT PARTITION
		Quick_sort(data, partitionIdx + 1, tail, drawData, stopTime)


def getColorArray(dataLen, head, tail, border, currIdx, isSwaping=False):
	colorArray = []
	for i in range(dataLen):
		if head <= i <= tail:
			colorArray.append('gray')
		else:
			colorArray.append('white')

		if i == tail:
			colorArray[i] = 'blue'
		elif i == border:
			colorArray[i] = 'red'
		elif i == currIdx:
			colorArray[i] = 'yellow'

		if isSwaping:
			if i == border or i == currIdx:
				colorArray[i] = 'green'

	return colorArray
