
# my answer
def iq_test(numbers):
	list_nums = numbers.split(" ")
	even_dict = {}
	odd_dict = {}
	for i, v in enumerate(list_nums):
		if int(v)%2 == 0:
			even_dict[i+1] = v 
		else:
			odd_dict[i+1] = v
	if len(even_dict) > len(odd_dict):
		return next(iter(odd_dict))
	else:
		return	next(iter(even_dict))



#best answer by dumavit
def iq_test(n):
    n = [int(i)%2 for i in n.split()]
    if n.count(0)>1:
        return n.index(1)+1
    else:
        return n.index(0)+1



iq_test("2 4 7 8 10") # 3)
iq_test("1 2 2") # 1)