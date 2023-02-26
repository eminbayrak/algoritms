# https://leetcode.com/problems/climbing-stairs/

# 70. Climbing Stairs
# Easy

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Constraints:
#     1 <= n <= 45

# O(2^n) solution, this is really slow, worst solution
def climbStairs(n) -> int:
    if n <= 1: return 1
    return climbStairs(n - 1) + climbStairs(n - 2)
        
# print(climbStairs(4)) # Result 3

# But if we pass higher number for n, the system would may crash
# For ex: climbStairs(50)

# To solve this issue, we can use "memoization" technique of dynamic programming with Recursion
def climbStairs(n: int, self = {}) -> int:
    if (n in self): return self[n]
    if (n <= 1): return 1
    self[n] = climbStairs(n - 1, self) + climbStairs(n - 2, self)
    return self[n]

# print(climbStairs(50)) # result: 20365011074

# memoization technique (Bottom Up) without Recursion
def climbStairs(self, n: int) -> int:
    # We can climb one stair with + 1 time as well as twoStairs with + 1 time 
    # so we make them equal to 1
    oneStair = 1
    twoStairs = 1
    for i in range(n - 1):
        temp = oneStair
        print("Temp: ", temp)
        print
        oneStair = oneStair + twoStairs
        print("One Stair: ", oneStair)
        print
        twoStairs = temp
        print("Two Stairs: ", twoStairs)
        print
    return(oneStair)

# print("Solution: ", climbStairs(0, 3))
            