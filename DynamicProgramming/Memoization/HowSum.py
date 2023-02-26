# Write a function `howSum(targetSum, numbers)` that takes in 
# a targetSum and an array of numbers as arguments.

# The function should return an array containing 
# any combination of elements that add up to exactly the targetSum. 
# If there is no combination that adds up to the targetSum, then return null.

# If there are multiple combinations possible, you may return any single one.

# Brute force
# m = targetSum, n = numbers.length
# time: O(n^m * m) -> *m because we used spread operator
# space: O(m)
def howSum(targetSum, numbers):
    if (targetSum == 0): return []
    if (targetSum < 0): return None
    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers)
        if (remainderResult != None):
            return [*remainderResult, num] # * sign is used for spread operator in Python
    return None

print(howSum(20, [4, 5, 7])) # result: [4, 4, 4, 4, 4]
print(howSum(7, [4, 2])) # result: None

# Memoized
# time: O(n * m^2)
# space: O(m^2) 
def howSum(targetSum, numbers, memo={}):
    if (targetSum in memo): return memo[targetSum]
    if (targetSum == 0): return []
    if (targetSum < 0): return None
    
    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers, memo)
        if (remainderResult != None):
            memo[targetSum] = [*remainderResult, num]
            return memo[targetSum]
    memo[targetSum] = None
    return None

print(howSum(300, [7, 14])) # result: None