# Write a function `canConstruct(target, wordBank)` that accepts 
# a target string and an array of strings.

# The function should return a boolean indicating whether or not 
# the `target` can be constructed by concatenating elements of the `wordBank` array.

# You may reuse elements of `wordBank` as many times as needed.

# For example: canConstruct(abcdef, [ab, abc, cd, def, abcd]), result: true

# Brute force, exponential complexity
# m = target.length
# n = wordBank.length
# time = (n^m * m)
# space = O(m^2) -> it's because we store new target word by slicing the target word each time
def canConstruct(target, wordBank):
    if (target == ''): return True
    for word in wordBank:
        if (target.startswith(word)):
            suffix = target[len(word):]
            if (canConstruct(suffix, wordBank) == 0):
                return True
    return False

print(canConstruct('laylay', ['l', 'ay', 'lay'])) # result: True

# Memoization
# m = target.length
# n = wordBank.length
# time = (n * m^2)
# space = O(m^2)
def canConstruct(target, wordBank, memo={}):
    if (target in memo): return True
    if (target == ''): return True
    
    for word in wordBank:
        if (target.startswith(word)):
            suffix = target[len(word):]
            if (canConstruct(suffix, wordBank, memo) == 0):
                memo[target] = True
                return True
    memo[target] = False
    return False

print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    'e',
    'eee',
    'eeeeee',
    'eeeeeeeeee'
])) # result: False