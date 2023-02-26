# Brute force, O(n^2)
class Solution:
    def twoSum(numbers, target):
        for m in numbers:
            for n in numbers[1:]: # [1:] means, everything after first node
                if (m + n == target):
                    return [m, n]
    print(twoSum([2, 7, 11, 15], 9)) # return: [2, 7]
    
# Hashmap, O(n)
class Solution:
    def twoSum(numbers, target):
        prev = {}
        for num in numbers:
            diff = target - num
            if (diff in prev):
                return [diff, num]
            prev[num] = num
    
    print(twoSum([2, 7, 11, 15], 9)) # return: [2, 7]

# Hashmap, returning indexes
# Hashmap, O(n)
class Solution:
    def twoSum(numbers, target):
        prev = {}
        for i, num in enumerate(numbers):
            difference = target - num
            if (difference in prev):
                return [prev[difference], i]
            prev[num] = i
    
    print(twoSum([2, 7, 11, 15], 9)) # return: [0, 1]