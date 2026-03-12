def maxArea(height):
    left = 0                      # 1
    right = len(height) - 1       # 2
    max_water = 0                 # 3

    while left < right:           # 4
        
        width = right - left      # 5
        area = min(height[left], height[right]) * width   # 6
        
        max_water = max(max_water, area)  # 7
        
        if height[left] < height[right]:  # 8
            left += 1
        else:
            right -= 1

    return max_water              # 9