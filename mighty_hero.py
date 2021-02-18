from math import factorial

def count_of_heads(initial, n, swings):
	f = 1
	while swings:
		initial = (initial - 1) + (factorial(f) *n)
		swings -=1
		f +=1
	return initial




#count_of_heads(2, 1, 1) #, 2)
#count_of_heads(5, 10, 3)#, 92)
#count_of_heads(5, 10, 2)#, 33)
#count_of_heads(51, 6, 31)#, 50983496835888389711611599965641898)
count_of_heads(30, 12, 31)#, 101966993671776779423223199931283755)
#count_of_heads(10, 8, 3)#, 79)
#count_of_heads(1, 1, 3)#, 7)
#count_of_heads(100, 143, 8)#, 6611411)
