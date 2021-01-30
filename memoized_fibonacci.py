fib_dict = {}
def fibonacci(n):
    if n in fib_dict:
        return fib_dict[n]
    if n == 1 or n == 2:
        result = 1
    elif n > 2:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    fib_dict[n] = result
    return result

print(fibonacci(70)) # 190392490709135)

# Good explaination: https://towardsdatascience.com/memoization-in-python-57c0a738179a