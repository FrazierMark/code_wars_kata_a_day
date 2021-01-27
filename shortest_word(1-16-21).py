def find_short(s):
	""" Find the shortest word in a sentence/string."""
    l = min(len(word) for word in s.split())
    return l