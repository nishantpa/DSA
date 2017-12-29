# Swami Shreeji 
# 28 Dec 2017
# Selection Sort

def findSmallest(arr):
	smallest = arr[0]
	smallestIndex = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallestIndex = i
	return smallestIndex

def selectionSort(arr):
	sortedArr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr)
		sortedArr.append( arr.pop(smallest) )
	return sortedArr

print selectionSort([5, 2, 3, 6, 9])