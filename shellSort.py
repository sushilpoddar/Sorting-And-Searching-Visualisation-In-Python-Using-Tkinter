"""this is shell sort
	Algorithm	|				Time Complexity
				|	Best(omega notation)	|    Average(theta notation)	|	Worst(bigO notation)
Shell sort		|	Ω(n)(not confirm yet)	|	θ(n^2)						|	O(n^2)

"""
import time


def ShellSort(data, drawData, stopTime):
	gap = len(data) // 2
	while gap > 0:
		drawData(data, getColorList(data, gap))
		time.sleep(stopTime)
		for index in range(gap, len(data)):
			current_element = data[index]
			drawData(data, ['blue' if data[i] == current_element and i == index else 'red' for i in range(len(data))])
			time.sleep(stopTime)
			current_position = index

			while current_position >= gap and current_element <= data[current_position - gap]:
				drawData(data, ['yellow' if (current_element == data[i] and i == current_position) or (data[i] ==
					data[current_position-gap] and i == current_position - gap) else 'red' for i in range(len(data))])
				time.sleep(stopTime)
				data[current_position] = data[current_position - gap]
				drawData(data, ['green' if (data[i] == data[current_position] and i == current_position) else 'red'
				for i in range(len(data))])
				# time.sleep(stopTime)
				current_position -= gap

			data[current_position] = current_element
			drawData(data, ['green' if (data[current_position] == data[i] and i == current_position) else 'red' for i in
				range(len(data))])
			time.sleep(stopTime)
		gap //= 2

	# return data


def getColorList(data, gap):
	ColorList = []
	for color in range(len(data)):
		if color % gap == 0:
			ColorList.append('white')
		else:
			ColorList.append('red')

	return ColorList
