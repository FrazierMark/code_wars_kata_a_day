#There is an array with some numbers. All numbers are equal except for one. Try to find it!
import numpy as np

def find_uniq(arr):
	arr = np.sort(arr)
	for previous, current in zip(arr, arr[1:]):
		if previous != current and current == current + 1:
			return previous
		else:
			return arr[-1]



#def find_uniq(arr):
#   arr.sort()
#   return arr[0] if arr[0] != arr[1] else arr[-1]

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
#find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55