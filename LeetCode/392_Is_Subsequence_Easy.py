# 392. Is Subsequence
# Easy

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed 
# from the original string by deleting some (can be none) of the characters without 
# disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

# Brute Force O(n^2)
def isSubsequence(s: str, t: str) -> bool:
    if len(s) > len(t): return False
    
    char = ''
    for i in range(len(t)):
        for j in range(len(s)):
            if t[i] == s[j]:
                char += (s[j])
    return char == s

# O(n)
def isSubsequence2(s: str, t: str) -> bool:
    if not s: return True
    i = 0
    for j in range(len(t)):
        if t[j] == s[i]:
            i += 1
        if i == len(s):
            return True
    return False

print(isSubsequence("abcq", "ahbgdc")) # Output: False

print(isSubsequence2("abc", "ahbgdc")) # Output: True


def printLinkedList(head):
    current = head
    while current:
        print(current.left)
        current = current.next
        
    
