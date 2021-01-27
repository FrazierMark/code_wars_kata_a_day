# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.



def find_it(seq):
    for i in seq:		# iterate through array
    	count = 0		
    	for j in seq:	# iterate through, if i = j increase count
    		if i == j:
    			count += 1
    	if count % 2 !=0:	# if count returns odd num, return that num
    		return i
    return None
                             