
# Given a single input string, write a function that produces all possible anagrams
# of a string and outputs them as an array. At first, don't worry about
# repeated strings.  What time complexity is your solution?

# Extra credit: Deduplicate your return array without using uniq().

# example usage:
# var anagrams = allAnagrams('abc');
# console.log(allAnagrams('abc')); // [ 'abc', 'acb', 'bac', 'bca', 'cab', 'cba' ]

def allAnagrams(str):
    arr = list(str)
    for i in arr:
        if i:
            arr.append(arr[i])
    return arr
str = 'abc'

print(allAnagrams(str))
