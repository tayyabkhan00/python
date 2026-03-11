def lengthOfLongestSubstring(s):
    char_set = set()       # 1
    left = 0               # 2
    max_length = 0         # 3

    for right in range(len(s)):   # 4
        
        while s[right] in char_set:   # 5
            char_set.remove(s[left])  # 6
            left += 1                 # 7
        
        char_set.add(s[right])        # 8
        
        max_length = max(max_length, right - left + 1)  # 9

    return max_length                 # 10