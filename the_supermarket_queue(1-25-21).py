#There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

#customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
#n: a positive integer, the number of checkout tills.

#The function should return an integer, the total time required.

def queue_time(customers, n):
	register = []			#list of registers tallied at 0
	for i in range(n):
		register.append(0)
	for i in customers:			# adding customer time to the lowest.. 
		register.sort()		#..register tally
		register[0] += i
	return max(register)	# time to checkout everyone is biggest tally



queue_time([2], 5)			  # 2
queue_time([2,2,3,3,4,4], 2) # 9
queue_time([1,2,3,4,5], 1)   # answer 15 
queue_time([1,2,3,4,5], 100) # answer 5


#Also, this is a little more concise by Numrut...
def queue_time(customers, n):
    queues = [0] * n
    for i in customers:
        queues.sort()
        queues[0] += i
    return max(queues)

# Additional info found on the topic
# Bin Packing Problem
# https://en.wikipedia.org/wiki/Bin_packing_problem...

#  "...involving placing each item into the first bin in which
# it will fit. It requires Θ(n log n) time, where n is the
# number of items to be packed. The algorithm can be made much
# more effective by first sorting the list of items into
# decreasing order (sometimes known as the first-fit decreasing algorithm)
#, although this still does not guarantee an optimal solution, and for
# longer lists may increase the running time of the algorithm.
# It is known, however, that there always exists at least one ordering
# of items that allows first-fit to produce an optimal solution.[3]"