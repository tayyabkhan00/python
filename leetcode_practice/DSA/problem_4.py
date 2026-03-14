def climbStairs(n):

    if n <= 2:          # 1
        return n

    first = 1           # 2
    second = 2          # 3

    for i in range(3, n+1):   # 4
        third = first + second   # 5
        
        first = second          # 6
        second = third          # 7

    return second               # 8