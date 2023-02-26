# Problem: Say that you are a traveler on a 2D grid. 
# You begin in the top-left corner and your goal is the travel to the bottom-right corner. 
# You may only move down or right.

# In how many ways can you travel to the goal on a grid with dimensions m * n?

# Write a function `gridTraveler(m, n)` that calculates this.

# Brute force, recursion, exponential
# O(2^n+m) time, O(n+m) space
def gridTraveler(m, n):
    # base cases
    if m == 1 or n == 1: return 1
    if m == 0 or n == 0: return 0
    
    return gridTraveler(m - 1, n) + gridTraveler(m, n - 1)

print(gridTraveler(2, 3)) # Expected output: 3