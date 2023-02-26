# Check if a large number is divisible by 3 or not

def check(num):
    res = 0
    while num > 0:
        r = num % 10
        res = res * 10 + r
        num //= 10
    return (res % 3 == 0)

num = 1332
if (check(num)) :
    print("Yes")
else :
    print("No")