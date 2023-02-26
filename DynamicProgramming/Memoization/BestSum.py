# Write a function `bestSum(targetSum, numbers)` that takes in a 
# targetSum and an array of numbers as arguments.

# The function should return an array containing the shortest 
# combination of numbers that add up to exactly the targetSum.

# If there is a tie for the shortest combination, you may return any one of the shortest.

# Brute force,
# m = targetSum
# n = numbers.length
# time: O(n^m * m)
# space: O(m^2)
def bestSum(targetSum, numbers):
    if (targetSum == 0): return []
    if (targetSum < 0): return None
    shortestCombination = None
    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers)
        if (remainderCombination != None):
            combination = [*remainderCombination, num]
            if (shortestCombination == None or len(combination) < len(shortestCombination)):
                shortestCombination = combination
            
    return shortestCombination

print(bestSum(7, [5, 3, 4, 2])) # result: [2, 5]

# Memoized,
# m = targetSum
# n = numbers.length
# time: O(n*m)
# space: O(m^2)
def bestSum(targetSum, numbers, memo={}):
    if (targetSum in memo): return memo[targetSum]
    if (targetSum == 0): return []
    if (targetSum < 0): return None
    shortestCombination = None
    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers, memo)
        if (remainderCombination != None):
            combination = [*remainderCombination, num]
            if (shortestCombination == None or len(combination) < len(shortestCombination)):
               shortestCombination = combination
    memo[targetSum] = shortestCombination
    return shortestCombination
    
print(bestSum(100, [1, 2, 5, 25])) # result: [25, 25, 25, 25]