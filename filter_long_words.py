def filter_long_words(sentence, n):
	long_words = []
	sentence_list = sentence.split()
	for word in sentence_list:
		if len(word) > n:
			long_words.append(word)

	return(long_words)






filter_long_words("The quick brown fox jumps over the lazy dog", 4)

