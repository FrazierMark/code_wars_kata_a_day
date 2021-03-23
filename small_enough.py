def small_enough(array, limit):
	for digit in array:
		if digit > limit:
			return False
	return True