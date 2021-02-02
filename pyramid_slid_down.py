#Your task is to write a function longestSlideDown 
#that takes a pyramid representation as argument
# and returns its' largest 'slide down'. For example,

def longest_slide_down(pyramid):
	btm_layer = pyramid.pop()  		#removes last layer of Array, saves in counter
	print (btm_layer)
	while pyramid:
		nxt_layer = pyramid.pop()		# next layer up from bottom
		print(f"Next Layer: {nxt_layer}")
		btm_layer = [nxt_layer[i] + max(btm_layer[i], btm_layer[i+1]) for i in range(len(nxt_layer))]
		print(f" bottom Layer: {btm_layer}")
	print (btm_layer.pop())



longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) # => 23

