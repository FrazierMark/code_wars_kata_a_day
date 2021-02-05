#Your task is to write a function longestSlideDown 
#that takes a pyramid representation as argument
# and returns its' largest 'slide down'. For example,

def longest_slide_down(pyramid):
	btm_layer = pyramid.pop()  		#removes last layer of Array, saves in counter
	while pyramid:
		nxt_layer = pyramid.pop()		# next layer up from bottom
		btm_layer = [nxt_layer[i] + max(btm_layer[i], btm_layer[i+1]) for i in range(len(nxt_layer))]
		# takes the larger of 2 ints at lower layer, and adds it to the int above.
		# this continues, adding the lower layer to the upper layer until the top
	return btm_layer.pop()



longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) # => 23

