# Write a function `countConstruct(target, WordBank)` that accepts a target string
# and an array of strings.

# The function should return the number of ways that the `target` 
# can be constructed by concatenating elements of the `wordBank` array.

# You may reuse elements of `wordBank` as many times as needed.

# Brute force, exponential complexity
# m = target.length
# n = wordBank.length
# time = (n^m * m)
# space = O(m^2) -> it's because we store new target word by slicing the target word each time
def countConstruct(target, wordBank):
    if (target == ''): return 1 # if target becomes empty, we know there is least one way
    totalCount = 0
    for word in wordBank:
        if (target.startswith(word)):
            suffix = target[len(word):]
            numberOfWaysForRest = countConstruct(suffix, wordBank)
            totalCount += numberOfWaysForRest
    return totalCount

print(countConstruct('laylay', ['l', 'ay', 'lay'])) # result: 4

# Memoization
# m = target.length
# n = wordBank.length
# time = (n * m^2)
# space = O(m^2)
def countConstruct(target, wordBank, memo={}):
    if (target in memo): return memo[target]
    if (target == ''): return 1 # if target becomes empty, we know there is least one way
    totalCount = 0
    for word in wordBank:
        if (target.startswith(word)):
            suffix = target[len(word):]
            numberOfWaysForRest = countConstruct(suffix, wordBank, memo)
            totalCount += numberOfWaysForRest
    memo[target] = totalCount
    return totalCount

print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    'e',
    'eee',
    'eeeeee',
    'eeeeeeeeee'
])) # result: 0