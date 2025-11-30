# 1. Brute Force (Beginner Method — O(n²))
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
print(twoSum([2, 7, 11, 15], 9))


# 2. HashMap Method (BEST — O(n))
def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
print(twoSum([2, 7, 11, 15], 9))

# 3. Using enumerate + dictionary (clean version)
def twoSum(nums, target):
    table = {}  
    for i, num in enumerate(nums):
        need = target - num
        if need in table:
            return [table[need], i]
        table[num] = i
print(twoSum([2, 7, 11, 15], 9))

# 4. Two-Pointer Technique (Requires Sorted Array — O(n log n) due to sorting)
def twoSum(nums, target):
    nums_with_indices = list(enumerate(nums))
    nums_with_indices.sort(key=lambda x: x[1])  # Sort by the number value
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums_with_indices[left][1] + nums_with_indices[right][1]
        if current_sum == target:
            return [nums_with_indices[left][0], nums_with_indices[right][0]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
print(twoSum([2, 7, 11, 15], 9))

# 5. Using Set for Lookup (O(n), but less efficient than HashMap due to lack of index tracking)
def twoSum(nums, target):
    seen = set()
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [nums.index(complement), i]
        seen.add(num)              
print(twoSum([2, 7, 11, 15], 9))

# 6. Using List Comprehension (Inefficient — O(n²))
def twoSum(nums, target):
    return next(([i, j] for i in range(len(nums)) for j in range(i + 1, len(nums)) if nums[i] + nums[j] == target), None)
print(twoSum([2, 7, 11, 15], 9))

# 7. Using itertools.combinations (Inefficient — O(n²))
import itertools
def twoSum(nums, target):
    for (i, num1), (j, num2) in itertools.combinations(enumerate(nums), 2):
        if num1 + num2 == target:
            return [i, j]
print(twoSum([2, 7, 11, 15], 9))

# 8. Using numpy (Not recommended for this problem — O(n²))
import numpy as np
def twoSum(nums, target):
    arr = np.array(nums)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
print(twoSum([2, 7, 11, 15], 9))

# 9. Recursive Approach (Inefficient — O(n²))
def twoSum(nums, target, start=0):
    if start >= len(nums):
        return None
    for j in range(start + 1, len(nums)):
        if nums[start] + nums[j] == target:
            return [start, j]
    return twoSum(nums, target, start + 1)
print(twoSum([2, 7, 11, 15], 9))

# 10. Using pandas (Not recommended for this problem — O(n²))
import pandas as pd
def twoSum(nums, target):
    df = pd.DataFrame({'num': nums})
    for i in range(len(df)):
        for j in range(i + 1, len(df)):
            if df.at[i, 'num'] + df.at[j, 'num'] == target:
                return [i, j]
print(twoSum([2, 7, 11, 15], 9))