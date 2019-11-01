# def fibonaci(n):
#     if n==0 or n==1:
#         return n
#     return fibonaci(n-1)+fibonaci(n-2)
#
# print(fibonaci(3))
#


def fib(n):
    memo = {}
    if n < 0:
        # Edge case: negative index
        raise ValueError('Index was negative. No such thing as a '
                         'negative index in a series.')
    elif n in [0, 1]:
        # Base case: 0 or 1
        return n

    # See if we've already calculated this
    if n in memo:
        return memo[n]

    result = fib(n - 1) + fib(n - 2)
    # Memoize
    memo[n] = result
    return result
print(fib(5))