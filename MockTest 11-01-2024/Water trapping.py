def trap(heights):
    if not heights or len(heights) < 3:
        return 0

    n = len(heights)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], heights[i])

    right_max[n-1] = heights[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], heights[i])

    trapped_water = 0
    for i in range(n):
        trapped_water += min(left_max[i], right_max[i]) - heights[i]

    return trapped_water

# Example usage:
heights1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
result = trap(heights1)
print(result)  # Output: 6
