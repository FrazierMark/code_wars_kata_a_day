def tickets(people):
	twenty_fives = fifties = 0

	for tickets in people:
		if tickets == 25:
			twenty_fives += 1
		elif tickets == 50:
			fifties += 1
			twenty_fives -= 1
		elif tickets == 100 and fifties > 0:
			twenty_fives -= 1
			fifties -= 1
		elif tickets == 100 and fifties == 0:
			twenty_fives -= 3
		if twenty_fives < 0 or fifties < 0:
			return "NO"
	return "YES"
