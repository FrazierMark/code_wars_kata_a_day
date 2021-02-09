def ips_between(start, end):
	list_start = start.split(".")
	list_end = end.split(".")
	start_convert = []
	end_convert = []

	for i in list_start:
		i = int(i)
		start_convert.append(i)

	for i in list_end:
		i = int(i)
		end_convert.append(i)

	start_convert[1] = start_convert[1] + (start_convert[0] * 256)
	start_convert[2] = start_convert[2] + (start_convert[1] * 256)
	start_a = start_convert[3] + (start_convert[2] * 256)


	end_convert[1] = end_convert[1] + (end_convert[0] * 256)
	end_convert[2] = end_convert[2] + (end_convert[1] * 256)
	end_a = end_convert[3] + (end_convert[2] * 256)

	addresses = end_a - start_a

	return addresses


	#return addresses






ips_between("10.0.0.0", "10.0.0.50") # 50)
# ips_between("20.0.0.10", "20.0.1.0") # 246)