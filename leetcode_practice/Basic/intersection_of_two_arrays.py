def intersect(nums1, nums2):
    freq = {}                     # 1
    result = []                   # 2

    for num in nums1:             # 3
        freq[num] = freq.get(num, 0) + 1   # 4

    for num in nums2:             # 5
        if num in freq and freq[num] > 0:  # 6
            result.append(num)            # 7
            freq[num] -= 1                # 8

    return result                 # 9
