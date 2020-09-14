"""	this is insertion sort algorithm for sorting..
    Algorithm	|				Time Complexity
                |	Best(omega notation)	|    Average(theta notation)	|	Worst(bigO notation)
Bubble Sort		|	Ω(n)					|	θ(n^2)						|	O(n^2)

    Bubble sort –
    Average and worst case time complexity:		n^2
    Best case time complexity: 		n when array is already sorted.
    Worst case:		when the array is reverse sorted.
"""
import time


def Bubble_sort(data, drawData, stopTime):
    for _ in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                drawData(data, ['green' if x == j or x == j + 1 else 'red' for x in range(len(data))])
                time.sleep(stopTime)
    drawData(data, ['green' for x in range(len(data))])
