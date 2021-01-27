# Complete the solution so that it splits the string into pairs
# of two characters. If the string contains an odd number of
# characters then it should replace the missing second character
# of the final pair with an underscore ('_').

def solution(s):
    result = []			
    if s:			
        n = 2
        result = [s[i:i+n] for i in range(0, len(s), n)]
        if len(result[-1]) < 2:
            result[-1] = result[-1] + '_'
        return result
    return result		# return an empty string if nothin in s



solution('abc') # should return ['ab', 'c_']
#solution('abcdef') # should return ['ab', 'cd', 'ef']
