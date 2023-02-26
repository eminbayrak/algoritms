
def smallest3Numbers(arr, n):
    min1 = min2 = min3 = float('inf')
    
    for i in range(0, n):
        
        if arr[i] < min1:
            min3 = min2
            min2 = min1
            min1 = arr[i]
        elif arr[i] < min2:
            min3 = min2
            min2 = arr[i]
        elif arr[i] < min3:
            min3 = arr[i]
    
    print(f"1st smallest number {min1}")
    print(f"2nd smallest number {min2}")
    print(f"3rd smallest number {min3}")
    
arr = [4, 9, 1, 32, 121]
n = len(arr)
smallest3Numbers(arr, n)

# Output: 
# 1st smallest number 1
# 2nd smallest number 4
# 3rd smallest number 9