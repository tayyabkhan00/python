def containsNearbyDuplicate(nums, k):
    index_map = {}                     # 1

    for i, num in enumerate(nums):     # 2
        
        if num in index_map and i - index_map[num] <= k:  # 3
            return True                # 4
        
        index_map[num] = i             # 5

    return False                       # 6