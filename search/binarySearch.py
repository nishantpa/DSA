# << Swami Shreeji >>
# 20 Dec 2017
# Binary Search

import sys

# Test cases
case1 = [1, 3, 5, 7, 9]

def binarySearch(case, target):
	low = 0
	high = len(case) - 1

	while low <= high:
		mid = (low + high) / 2
		guess = case[mid]
		if guess == target:
			print mid
			return mid
		if guess > target:
			high = mid - 1
		else:
			low = mid + 1
	return None

binarySearch(case1, 1)