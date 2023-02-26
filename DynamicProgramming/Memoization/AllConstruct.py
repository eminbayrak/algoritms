# Write a function `allConstruct(target, wordBank)` that accepts a target 
# string and an array of strings.

# The function should return a 2D array containing all of the ways 
# that the `target` can be constructed by concatenating elements of the `wordBank` array.
# Each element of the 2D array should represent one combination that 
# contracts the `target`.

# You may reuse elements of `wordBank` as many times as needed.

# For example:
# allConstruct('purple', ['purp', 'p', 'le', 'purple']) 	
# Result: [['purp', 'le'], ['p', 'ur', 'p', 'le']]

# Brute force
def allConstruct(target, wordBank):
    if (target == ''): return [[]]
    result = []
    for word in wordBank:
        if (target.startswith(word)):
            # next line: prepend word to each inner list of the list returned by allConstruct
            result += [[word] + x for x in allConstruct(target[len(word):], wordBank)]
    return result

print(allConstruct('purple', ['purp','p', 'ur', 'le', 'purpl'])) 
# Output: [['purp', 'le'], ['p', 'ur', 'p', 'le']]

# Memoization
def allConstruct(target, wordBank, memo={}):
    if (target == ''): return [[]]
    if (target in memo): return memo[target]
    result = []
    for word in wordBank:
        if (target.startswith(word)):
            result += [[word] + x for x in allConstruct(target[len(word):], wordBank)]
    
    memo[target] = result
    return result

print(allConstruct('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz',
                   ['a','aaaaa', 'aaaaaaaa', 'aaaaaaaaaa', 'aaaaaaaaaaaaa']))

# Output: []