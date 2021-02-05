# The maximum sum subarray problem consists in finding
# the maximum sum of a contiguous subsequence in an array
# or list of integers:

#Kadane's Algorithm<<<<

# good ex. https://www.educative.io/edpresso/the-maximum-sub-array-sum-problem
# https://www.youtube.com/watch?v=jnoVtCKECmQ&t=58s

def max_sequence(arr):
    n = len(arr)
    if not arr:
        return 0
    current_maximum = maximum_so_far = arr[0]    
          
    for i in range(1,n): 
        current_maximum = max(arr[i], current_maximum + arr[i]) 
        maximum_so_far = max(maximum_so_far,current_maximum)
        
    if maximum_so_far <= 0:					# If the max_sequence is negative, return 0
        return 0
    return maximum_so_far 