# How can we do?
# Ans: while traversing the array we will just incr the count in its row and col number.
# it means we have seen one more ele in that row and col.

# and whenever either 'no of ele in row= 'no of col' OR 'no of ele in col= no of row' then, we will return that index.

# vvi: for knowing the row and col of all ele, we will store their row and col in hashmap to get in O(1).
# so first store the rowNo and colNo of each ele in hashmap.
# All ele are distinct so there will be no problem.

# After that traverse the array and keep a freq hashmap for both row and col to check how many ele we have seen in that row or col.

# time: O(m*n)
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n= len(mat), len(mat[0])
        rowNo= {}   # will store the row of each number
        colNo= {}   # will store the column no of each number
        for i in range(m):
            for j in range(n):
                num= mat[i][j]
                rowNo[num]= i
                colNo[num]= j
        # now traverse the array and incr the frequency in their row and col.
        # if no of ele in their row will be equal to cols OR no of ele in their col will be equal to rows 
        # then means we have found either row or column with all elements painted
        freq_row= {}  # will keep track of number of ele we have seen till now in each row
        freq_col= {}  # will keep track of number of ele we have seen till now in each col
        # we can use array also for this.
        for i, num in enumerate(arr):
            # get the row and col of this num
            row, col= rowNo[num], colNo[num]
            # incr the freq by '1' in both row and col and keep on checking whether that row/col has been filled 
            freq_row[row]= 1 + freq_row.get(row, 0)
            freq_col[col]= 1 + freq_col.get(col, 0)
            if freq_row[row]== n or freq_col[col]== m:
                return i