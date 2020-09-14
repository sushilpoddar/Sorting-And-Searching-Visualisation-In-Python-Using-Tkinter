"""this is selection sort for sorting a list..
	Algorithm	|				Time Complexity
				|	Best(omega notation)	|    Average(theta notation)	|	Worst(bigO notation)

Selection Sort	|	Ω(n^2)					|	θ(n^2)						|	O(n^2)

	Selection sort –
	Best, average and worst case time complexity: n^2 which is independent of distribution of data.
"""
import time


def SelectionSort(data, drawData, stopTime):
	for i in range(len(data)):
		minimum = data[i]
		drawData(data, ['blue' if (data[k] == minimum and k == i) else 'red' for k in range(len(data))])
		time.sleep(stopTime)
		for j in range(i+1, len(data)):
			if minimum > data[j]:
				minimum = data[j]
				tmp = j
				drawData(data, ['blue' if (minimum == data[x] and i == x) else 'red' for x in range(len(data))])
				time.sleep(stopTime)

			drawData(data, ['yellow' if data[j] == data[k] and k == j else 'red' for k in range(len(data))])
			time.sleep(stopTime)
		if minimum != data[i]:
			drawData(data, ['green' if (data[k] == minimum and k == tmp) or (data[i] == data[k] and k == i) else
				'red' for k in range(len(data))])
			time.sleep(stopTime)
			data[i], data[tmp] = minimum, data[i]
			# time.sleep(timeTick)
			drawData(data, ['green' if (data[k] == minimum and k == i) or (data[tmp] == data[k] and tmp == k) else
							'red' for k	in range(len(data))])
			time.sleep(stopTime)

		drawData(data, ['white' if k <= i else 'red' for k in range(len(data))])
		time.sleep(stopTime)

	# drawData(data, ['green' for x in range(len(data))])
	# time.sleep(timeTick)

	# return data

	# by using min built in function

	# list2 = []
	# while len(list1) != 0:
	# 	tmp = min(list1)
	# 	list2.append(tmp)
	# 	list1.remove(tmp)
	#
	# return list2
