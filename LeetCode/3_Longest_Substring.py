# 3. Longest Substring Without Repeating Characters
# Medium

# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:

# Input: s = ""
# Output: 0

# Solution video: https://www.youtube.com/watch?v=wiGpQwVHdE0

import time

# time O(n), space O(n)
class Solution:
    def lengthOfLongestSubstring(s: str):
        charSet = set()
        result = 0
        leftPointer = 0
        for rightPointer in range(len(s)):
            while s[rightPointer] in charSet:
                charSet.remove(s[leftPointer])
                leftPointer += 1
            charSet.add(s[rightPointer])
            result = max(result, rightPointer - leftPointer + 1)
        return result
    
    print(lengthOfLongestSubstring("abcabcbb")) # Expected Output: 3
            