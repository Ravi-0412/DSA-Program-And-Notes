# Approach
# Note: 1) Max possible move is 2. What ever is the configuration, queen can be captured in 2 moves
# using Rook.
# 2) Now when ever the two pieces are head to head and the third pice is not in between them 
# then we can capture queen in 1 step. This can be possible in 4 different ways :
# a) rook and queen in same row
# b)rook and queen in the same column
# c) bishop and queen in the same anti- diagonal
# d) bishop and queen in the same diagonal
# Only check for above four cases along with the check that the 3rd piece is not in between two direct capture.

# Complexity
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # case a : Rook is in same row as queen
        if a == e:
            # check if bishop in between rock and queen. if yes then 2 else 1
            # (rook -> bishop -> queen ) or (queen -> bishop -> rook)
            return 2 if a == c and (b < d < f or b > d > f) else 1
        # case2 : Rook is in same column as queen
        if b == f:
            # check if bishop in between rock and queen. if yes then 2 else 1
            # (rook -> bishop -> queen ) or (queen -> bishop -> rook)
            return 2 if b == d and (a < c < e or a > c > e) else 1
        # case 3: Bishop and queen is in anti-diagonal(upper-right to bottom-left)
        if c + d == e + f:
            # check if rook comes in between . if yes then two else 1
            # rook comes be in same diagonal + (bishop -> rook -> queen ) or (queen -> rook -> bishop)
            return 2 if a + b == c + d and (c < a < e or c > a > e) else 1
        # case 4: Bishop and queen is in same diagonal(upper -left to bottom - right)
        if c - d == e -f:
            # check if rook comes in between . if yes then two else 1
            # rook comes be in same diagonal + (bishop -> rook -> queen ) or (queen -> rook -> bishop)
            return 2 if a - b == c - d and (c < a < e or c > a > e) else 1
        return 2