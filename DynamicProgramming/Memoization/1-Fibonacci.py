# Write a function `fib(n)` that takes in a number ads an argument.
# The function should return the nth number of the Fibonacci sequence.

def fib(n) -> int: 
    if (n <= 2): return 1
    return fib(n - 1) + fib(n - 2)

print(fib(7)) # result: 13

# This is O(2^n) which is not a desirable complexity. 
# If we give high n number, it will take long time to complete, for example:
# print(fib(50))

# To solve this, we can use "memoization" technique of dynamic programming
# Memoization is a programming technique that accelerates performance by caching 
# the return values of expensive function calls. 
# A “memoized” function will immediately output a pre-computed value 
# if it’s given inputs that it’s seen before.
def fib(n, memo = {}) -> int:
    if (n in memo): return memo[n]
    if (n <= 2): return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

print(fib(50)) # result: 12586269025