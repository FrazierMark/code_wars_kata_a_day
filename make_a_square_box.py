def box(n):
	boxer = []
	top = '-' + (n-1)*'-'
	middle = '-' + (n-2)*' ' + '-'
	bottom = '-' + (n-1)*'-'
	boxer.append(top)
	for mid in range(n-2):
		boxer.append(middle)
	boxer.append(bottom)
	return boxer