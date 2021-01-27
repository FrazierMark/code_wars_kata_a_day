def longest(s1, s2):
    result = s1 + s2
    print (result)
    set(result)
    print (result)
    results = []
    for i in result:
    	results.append(i)
    results = list(dict.fromkeys(results))
    results = sorted(results)
    results = ''.join(results)


# Same as

longest("aretheyhere", "yestheyarehere")