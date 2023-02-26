# Write a function `canSum(targetSum, numbers)` that takes in 
# a targetSum and an array of numbers as arguments.

# The function should return a Boolean indicating whether or 
# not it is possible to generate the targetSum using numbers from the array.

# Constraints: You may use an element of the array as many times as needed. 
# You may assume that all input numbers nonnegative.
# For example: canSum(7, [5, 3, 4, 7]) -> true, is true because least 
# one way we can generate the target value

# Brute Force O(n^2) solution
# m = targetSum, n = array length -> O(n^m) time, O(m) space
# Note: Remember that you can use any element many times you want
def canSum(targetSum, numbers) -> bool:
    # Covering up base case
    if (targetSum == 0): return True
    # If targetSum become negative, then return False
    if (targetSum < 0): return False
    # Iterate through numbers array
    for num in numbers:
        remainder = targetSum - num
        if (canSum(remainder, numbers) == True): return True
    return False
print(canSum(7, [5, 3, 4, 7]))

# Memoization technique, O(m*n) time, O(m) space
def canSum(targetSum, numbers, memo={}):
    if (targetSum in memo): return memo[targetSum]
    if (targetSum == 0): return True
    if (targetSum < 0): return False
    
    for num in numbers:
        remainder = targetSum - num
        if (canSum(remainder, numbers, memo) == True): 
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False
print(canSum(300, [7, 14]))