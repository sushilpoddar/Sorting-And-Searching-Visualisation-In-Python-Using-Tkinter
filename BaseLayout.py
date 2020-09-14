"""
this is base layout of python sorting visualisation...
here is time complexity of those sorting algorithm...

	Algorithm	|				Time Complexity
				|	Best(omega notation)	|    Average(theta notation)	|	Worst(bigO notation)

Selection Sort	|	Ω(n^2)					|	θ(n^2)						|	O(n^2)
Bubble Sort		|	Ω(n)					|	θ(n^2)						|	O(n^2)
Insertion Sort	|	Ω(n)					|	θ(n^2)						|	O(n^2)
Heap Sort		|	Ω(n log(n))				|	θ(n log(n))					|	O(n log(n))
Quick Sort		|	Ω(n log(n))				|	θ(n log(n))					|	O(n^2)
Merge Sort		|	Ω(n log(n))				|	θ(n log(n))					|	O(n log(n))
Bucket Sort		|	Ω(n+k)					|	θ(n+k)						|	O(n^2)
Radix Sort		|	Ω(nk)					|	θ(nk)						|	O(nk)
Shell sort		|	Ω(n log(n))				|	θ(n^2)						|	O(n^2)

Radix sort –
	Best, average and worst case time complexity: nk where k is the maximum number of digits in elements of array.

Count sort –
	Best, average and worst case time complexity: n+k where k is the size of count array.

Bucket sort –
	Best and average time complexity: n+k where k is the number of buckets.
	Worst case time complexity: n^2 if all elements belong to same bucket.
"""
from tkinter import *
from tkinter import ttk
import random
from bubbleSort import Bubble_sort
from quickSort import Quick_sort
from mergeSort import Merge_sort
from selectionSort import SelectionSort
from tkinter import messagebox
from insertionSort import InsertionSort
from shellSort import ShellSort
from binarySearch import BinarySearch
from linearSearch import LinearSearch

root = Tk()
root.title('Sorting Algorithm Visualisation')
root.geometry("1350x1000+0+0")
root.maxsize(1400, 1150)
root.config(bg='black')

# global variables
selected_alg = StringVar()
selected_search_alg = StringVar()
# ValueToFind = StringVar()
valueFind = IntVar()
data = []


# global function
def drawData(data, colorList):
	canvas.delete("all")
	c_height = 480
	c_width = 900
	x_width = c_width / (len(data) + 1)
	offset = 10
	spacing = 10
	normalizedData = [i / max(data) for i in data]
	for i, height in enumerate(normalizedData):
		# top left
		x0 = i * x_width + offset + spacing
		y0 = c_height - height * 440
		# bottom right
		x1 = (i + 1) * x_width + offset
		y1 = c_height

		canvas.create_rectangle(x0, y0, x1, y1, fill=colorList[i])
		# this write value of element on the top...visible only other than black colour
		canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]), fill='white')

	root.update_idletasks()


def Generate():
	global data

	minVal = int(minEntry.get())
	maxVal = int(maxEntry.get())
	size = int(sizeEntry.get())

	data = []
	for _ in range(size):
		data.append(random.randrange(minVal, maxVal + 1))

	# ['red', 'red' ,....,red]
	drawData(data, ['red' for x in range(len(data))])


def StartAlgorithm():
	global data
	# global value
	if not data: return

	# it will run quick sort
	if algoMenu.get() == 'Quick Sort':
		Quick_sort(data, 0, len(data) - 1, drawData, speedScale.get())

	# it will run bubble sort
	elif algoMenu.get() == 'Bubble Sort':
		Bubble_sort(data, drawData, speedScale.get())

	# it will run merge sort
	elif algoMenu.get() == 'Merge Sort':
		Merge_sort(data, drawData, speedScale.get())

	# it will run selection sort
	elif algoMenu.get() == 'Selection Sort':
		SelectionSort(data, drawData, speedScale.get())

	# it will run insertion sort
	elif algoMenu.get() == 'Insertion Sort':
		InsertionSort(data, drawData, speedScale.get())

	# it will run shell sort
	elif algoMenu.get() == 'Shell Sort':
		ShellSort(data, drawData, speedScale.get())

	# it will run visualise Binary Search work and Linear search
	elif salgoMenu.get() == 'Binary Search' or salgoMenu.get() == 'Linear Search':
		if salgoMenu.get() == 'Binary Search':
			Merge_sort(data, drawData, speedScale.get())
			FoundOrNot = BinarySearch(data, valueFind.get(), drawData, speedScale.get())
		else:
			FoundOrNot = LinearSearch(data, valueFind.get(), drawData, speedScale.get())

		if FoundOrNot[0] is False:
			messagebox.showinfo("Info", "Data is Not Found!!!", parent=root)
		else:
			messagebox.showinfo("Info", f"Data is Found at the index {FoundOrNot[1]}", parent=root)

	# show error if click on start button without selecting any algorithm.
	if algoMenu.get() == '-Select Sorting Algorithm-' and salgoMenu.get() == '-Select Searching Algorithm-':
		messagebox.showerror("Error", "Please select a algorithm!!!", parent=root)
		drawData(data, ['red' for x in range(len(data))])

	# final list after sorting will be in purple colour
	elif algoMenu.get() == '-Select Sorting Algorithm-' and salgoMenu.get() != '-Select Searching Algorithm-':
		drawData(data, ['purple' for i in range(len(data))])

	elif algoMenu.get() != '-Select Sorting Algorithm-' and salgoMenu.get() == '-Select Searching Algorithm-':
		drawData(data, ['purple' for i in range(len(data))])


def Search():
	# global value
	if valueFind.get() is None:
		return
	elif valueFind.get() > max(data):
		messagebox.showinfo("Info", "Data is out of range!!!", parent=root)
	elif valueFind.get() < min(data):
		messagebox.showinfo("Info", "Data is out of range!!!", parent=root)
	else:
		StartAlgorithm()


# frame / base lauout
UI_frame = Frame(root, width=600, height=200, bg='white')
UI_frame.grid(row=0, column=0, padx=8, pady=5)

canvas = Canvas(root, width=900, height=480, bg='black')
canvas.grid(row=1, column=0, pady=5)

# TODO: make a frame for displaying current processing algorithm in right side.
AlgoFrame = Frame(root, width=410, height=450, bg='yellow')
AlgoFrame.grid(row=1, column=1)
# label = Label(AlgoFrame, text="Visualisation Of Sorting Algorithm", font=("verdana", 15, "bold")).grid(padx=0, pady=0)
# TODO: make algorithm highlight at same time of that algorithm process in the back ground.

# User Interface Area
# Row[0]
Label(UI_frame, text=" Visualisation Of S.A.S Algorithm", font=("verdana", 14, "bold"), fg='red', bd=2, relief=GROOVE,
	bg='white').grid(row=0, column=0, padx=5, pady=5, sticky=W)

algoMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, font=("verdana", 10, "bold"),
	values=['-Select Sorting Algorithm-', 'Bubble Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort', 'Selection Sort',
	'Shell Sort'], state='readonly')
algoMenu.grid(row=0, column=1, padx=5, pady=5)
algoMenu.current(0)

speedScale = Scale(UI_frame, from_=0.01, to=5.0, length=200, digits=2, resolution=0.1, orient=HORIZONTAL,
	label="Select Speed [s]", font=("verdana", 8, "bold"))
speedScale.grid(row=0, column=2, padx=5, pady=5)

Button(UI_frame, text="Start", command=StartAlgorithm, bg='green', padx=15).grid(row=0, column=3, padx=15, pady=5)

# Row[1]
sizeEntry = Scale(UI_frame, from_=3, to=60, resolution=1, length=200, orient=HORIZONTAL, font=("verdana", 8, "bold"),
	label="Set Data Size :", bg='grey')
sizeEntry.grid(row=1, column=0, padx=15, pady=5, sticky=E)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, length=150, orient=HORIZONTAL, font=("verdana", 8, "bold"),
	label="Set Min Value :", bg='grey')
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, length=180, orient=HORIZONTAL, font=("verdana", 8, "bold"),
	label="Set Max Value :", bg='grey')
maxEntry.grid(row=1, column=2, padx=5, pady=5, sticky=W)

Button(UI_frame, text="Generate", command=Generate, bg='blue', padx=15).grid(row=1, column=3, padx=5, pady=5)

# row[1]
salgoMenu = ttk.Combobox(UI_frame, textvariable=selected_search_alg, font=("verdana", 10, "bold"),
	values=['-Select Searching Algorithm-', 'Binary Search', 'Linear Search'], state='readonly')
salgoMenu.grid(row=2, column=0, padx=5, pady=5, sticky=E)
salgoMenu.current(0)
value = Entry(UI_frame, font=("times new roman", 15), textvariable=valueFind, bg="white", fg="black", relief=GROOVE,
	bd=4)
value.insert(0, 'Enter value to find..ex:')
value.grid(row=2, column=1, padx=5, pady=5, sticky=E)
Button(UI_frame, text="Search", command=Search, bg='pink', padx=15).grid(row=2, column=2, padx=5, pady=5, sticky=W)

root.mainloop()
