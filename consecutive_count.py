

def get_consective_items(items, key): 
    current = 0
    longest = 0
    if isinstance(items, int):
        items, key = str(items), str(key)
    for item in items:
        if item == key:
            current += 1
            if current > longest:
                longest = current
        else:
            current = 0
    return longest


# best answer
def get_consective_items(items, key): 
	items, key = str(items), str(key)
	count = 0
	temp = key[:]
	while temp in items:
		temp += key
		count += 1
	print(count)



get_consective_items(90000, 0) # 4)
#get_consective_items('ascasdaiiiasdacasdiiiiicasdasdiiiiiiiiiiisdasdasdiii', 'i') # 11)