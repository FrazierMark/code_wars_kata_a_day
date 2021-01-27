#Find the missing letter
#Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

def find_missing_letter(chars):
	for previous, current in zip(chars, chars[1:]):
			if ord(current) - ord(previous) != 1:
				missing = chr(ord(current) - 1)
				print (missing)


 

# Best answer by Blind4Basics
#def find_missing_letter(chars):
 #   n = 0
  #  while ord(chars[n]) == ord(chars[n+1]) - 1:
  #     n += 1
   # return chr(1+ord(chars[n]))



#find_missing_letter(['a','b','c','d','f'])
find_missing_letter(['O','Q','R','S'])
