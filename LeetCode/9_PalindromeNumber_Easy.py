# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. 
# For example, 121 is palindrome while 123 is not.
# Example 1:

# Input: x = 121
# Output: true

class Solution:
    def isPalindromeString(num: int) -> bool:
        reverse = str(num)[::-1]
        if reverse == str(num): return True
        return False
    
    
    print(isPalindromeString(12321)) # Expected output: True
