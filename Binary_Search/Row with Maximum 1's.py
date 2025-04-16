"""
Method 1: Brute force
Logic: Traverse every row and check number of ones in that.

Time: O(row * col)
"""

"""
Method 2: Jut use sorted property of row.
For each row find the index of 1st one say column 'c' then number of ones in 
that column = col - c

Time: O(row*(log*Col))
"""

def rowMaxOnes(mat, m ,n):
    row, col = len(mat), len(mat[0])
    maxOnes, ans = 0, -1
    for i in range(row):
        ind = findIndexOfFirstOne(mat[i], 1)
        noOfOnes = col - ind
        if noOfOnes > maxOnes:
            ans = i
            maxOnes = noOfOnes
    return ans

def findIndexOfFirstOne(arr, target):
    n = len(arr)
    start, end = 0, n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return start


"""
Method 3: Most Optimised

Start from top-right.

Time: O(m+ n)
"""

def rowMaxOnes(mat, m, n):
    # Initialize variables to track the maximum number of 1s and corresponding row index
    maxOnes, ans = 0, -1

    # Start from the top-right corner of the matrix
    r, c = 0, n - 1

    # Traverse the matrix until we go out of bounds
    while r < m and c >= 0:
        if mat[r][c] == 1:
            # If we see a 1, move left (we're still in the same row)
            c -= 1
            # Update the answer to current row since it has more 1s
            ans = r
            # Update maxOnes = total columns - current column index - 1
            maxOnes = n - c - 1
        else:
            # If we see a 0, move down to the next row
            r += 1

    # Return the row index with the maximum number of 1s
    return ans
