# Write a function called sumIntervals/sum_intervals() that
# accepts an array of intervals, and returns the sum of all
# the interval lengths. Overlapping intervals should only be
# counted once.


def sum_of_intervals(intervals):
	range_dict = {}
	len_counter = 0
	for array in intervals:
		for n in range(array[0], array[-1]):
			if n in range_dict:
				continue
			else:
				range_dict[n] = n
	print(len(range_dict))		




# sum_of_intervals([(1, 5)])  #4)
# sum_of_intervals([(1, 5), (6, 10)])  # 8
# sum_of_intervals([(1, 5), (1, 5)])    #4)
sum_of_intervals([(1, 4), (7, 10), (3, 5)]) # 7)