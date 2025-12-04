def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n                # 1

    prefix = 1                      # 2
    for i in range(n):              # 3
        result[i] = prefix          # 4
        prefix *= nums[i]           # 5

    suffix = 1                      # 6
    for i in range(n - 1, -1, -1):  # 7
        result[i] *= suffix         # 8
        suffix *= nums[i]           # 9

    return result                   # 10
