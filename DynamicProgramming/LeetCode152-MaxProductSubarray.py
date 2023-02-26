# 152. Maximum Product Subarray - Medium

# Given an integer array nums, find a contiguous non-empty subarray within 
# the array that has the largest product, and return the product.
# It is guaranteed that the answer will fit in a 32-bit integer.
# A subarray is a contiguous subsequence of the array.

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

def maxProductSubArray(nums) -> int:
    if nums:
        queue = [nums]
        result = []
        while len(queue) > 0:
            level = []
            for i in range(len(queue)):
                current = queue.pop(0)
                level.append(current)
            result.append(level)
            
    return result

if __name__ == '__main__':
    nums = [3, 4, -7, 1, 3, 3, 1, -4]
    
    print(maxProductSubArray(nums))