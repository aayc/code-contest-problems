def hourglassSum (arr):
    max_hourglass = -1000000
    for r in range(0, len(arr) - 2):
        for c in range(0, len(arr) - 2):
            max_hourglass = max(max_hourglass, arr[r][c] + arr[r][c + 1] + arr[r][c + 2] + arr[r + 1][c + 1] + arr[r + 2][c] + arr[r + 2][c + 1] + arr[r + 2][c + 2])
    return max_hourglass

