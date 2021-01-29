#A Narcissistic Number is a positive number which is
# the sum of its own digits, each raised to the power
# of the number of digits in a given base. In this Kata,
# we will restrict ourselves to decimal (base 10).

def narcissistic(value):
	str_value = str(value)
	base = len(str_value)
	values = []
	for i in str_value:
		values.append(int(i)**base)
	total = sum(values)
	return total == value


#narcissistic(7) # True,
#narcissistic(371) # True,
#narcissistic(122) # False,
narcissistic(4887) # False,
