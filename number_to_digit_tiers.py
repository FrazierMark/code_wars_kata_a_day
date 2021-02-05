def create_array_of_tiers(n):
	tiers = []
	num_string = str(n)
	tiers.append(num_string)

	while num_string:
		num_string = num_string[:-1]
		if num_string:
			tiers.append(num_string)
	tiers.reverse()
	return tiers

create_array_of_tiers(2017) # ["2", "20", "201", "2017"])