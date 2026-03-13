def spiralOrder(matrix):
    result = []
    
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:

        # traverse left → right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # traverse top → bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # traverse right → left
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            # traverse bottom → top
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result