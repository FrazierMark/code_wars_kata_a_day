import numpy as np


def binary_array_to_number(arr):
	arr = np.array(arr).tolist()
	arr = ''.join(str(x) for x in arr)
	arr = int(arr, 2)
	return arr




binary_array_to_number([0,0,0,1])