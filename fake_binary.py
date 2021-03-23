def fake_bin(x):
	converted_string = []
	string_x = str(x)
	for digit in string_x:
		if int(digit) < 5:
			converted_string.append(str(0))
		elif int(digit) >= 5:
			converted_string.append(str(1))
	return("".join(converted_string))

fake_bin(45385593107843568)
