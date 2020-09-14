"""	this is insertion sort algorithm for sorting...
	Algorithm	|				Time Complexity
				|	Best(omega notation)	|    Average(theta notation)	|	Worst(bigO notation)
Insertion Sort	|	Ω(n)					|	θ(n^2)						|	O(n^2)

	Insertion sort –
	Average and worst case time complexity:		n^2
	Best case time complexity: 		n when array is already sorted.
	Worst case:		when the array is reverse sorted.
"""
import time


def InsertionSort(data, drawData, stopTime):
	for index in range(1, len(data)):
		current_element = data[index]
		drawData(data, ['blue' if data[i] == current_element and i == index else 'red' for i in range(len(data))])
		time.sleep(stopTime)
		current_position = index
		while current_element < data[current_position - 1] and current_position > 0:
			drawData(data, ['yellow' if (data[current_position] == data[i] and i == current_position) else 'red' for i in range(len(data))])
			time.sleep(stopTime)
			data[current_position] = data[current_position - 1]
			drawData(data, ['green' if data[i] == data[current_position] and i == current_position else 'red' for i in range(len(data))])
			time.sleep(stopTime)
			current_position -= 1

		data[current_position] = current_element
		drawData(data, ['green' if data[current_position] == data[i] and i == current_position else 'red' for i in range(len(data))])
		time.sleep(stopTime)

	# return data
