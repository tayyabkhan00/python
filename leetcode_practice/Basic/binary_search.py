def search(nums, target):
    left = 0                      # 1
    right = len(nums) - 1         # 2

    while left <= right:          # 3
        
        mid = (left + right) // 2 # 4
        
        if nums[mid] == target:   # 5
            return mid
        
        elif nums[mid] < target:  # 6
            left = mid + 1
        
        else:                     # 7
            right = mid - 1

    return -1                     # 8