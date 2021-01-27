#A Narcissistic Number is a positive number which is
# the sum of its own digits, each raised to the power
# of the number of digits in a given base. In this Kata,
# we will restrict ourselves to decimal (base 10).


def narcissistic(value):
	str_value = str(value)
	print(f"str_value: {str_value}")
	base = len(str_value)
	values = []
	for i in str_value:
		values.append(int(i)**base)
	print(f"base: {base}")
	print(f" values: {values}")
	total = sum(values)
	print(total)
	if total == value:
		print(f"true") 
	else:
		print(f"false")


#narcissistic(7) # True,
#narcissistic(371) # True,
#narcissistic(122) # False,
narcissistic(4887) # False,
