# just same way we did for two strictly sorted arrays.
# Since both matrices is in strictly increasing order so there will be no duplicates in individual matrices.

# Time: O(n*n), space = O(1)

class Solution:
    def countPairs(self, mat1, mat2, n, x):
        r1, c1 = 0, 0
        r2, c2 = n - 1, n - 1
        ans = 0
        
        while r1 < n and r2 >= 0:
            current_sum = mat1[r1][c1] + mat2[r2][c2]
            
            if current_sum == x:
                ans += 1
                
                # Move to the next element in mat1
                if c1 == n - 1:
                    r1 += 1
                    c1 = 0
                else:
                    c1 += 1

                # Move to the previous element in mat2
                if c2 == 0:
                    r2 -= 1
                    c2 = n - 1
                else:
                    c2 -= 1
            elif current_sum > x:
                # Move to the previous element in mat2
                if c2 == 0:
                    r2 -= 1
                    c2 = n - 1
                else:
                    c2 -= 1
            else:
                # Move to the next element in mat1
                if c1 == n - 1:
                    r1 += 1
                    c1 = 0
                else:
                    c1 += 1
        
        return ans
    

# Now given that the matrices are sorted but not strictly (i.e., duplicates are allowed).
# just same way we did for two sorted arrays with duplicates
class Solution:
    def countPairs(self, mat1, mat2, n, x):
        def get_next(mat, r, c, n):
            """Get the next element in the matrix given row and column."""
            if c == n - 1:
                return r + 1, 0
            else:
                return r, c + 1
        
        def get_prev(mat, r, c, n):
            """Get the previous element in the matrix given row and column."""
            if c == 0:
                return r - 1, n - 1
            else:
                return r, c - 1

        r1, c1 = 0, 0
        r2, c2 = n - 1, n - 1
        ans = 0
        
        while r1 < n and r2 >= 0:
            current_sum = mat1[r1][c1] + mat2[r2][c2]
            
            if current_sum == x:
                # Count duplicates in mat1
                count1 = 1
                next_r1, next_c1 = get_next(mat1, r1, c1, n)
                while next_r1 < n and mat1[next_r1][next_c1] == mat1[r1][c1]:
                    count1 += 1
                    next_r1, next_c1 = get_next(mat1, next_r1, next_c1, n)
                
                # Count duplicates in mat2
                count2 = 1
                prev_r2, prev_c2 = get_prev(mat2, r2, c2, n)
                while prev_r2 >= 0 and mat2[prev_r2][prev_c2] == mat2[r2][c2]:
                    count2 += 1
                    prev_r2, prev_c2 = get_prev(mat2, prev_r2, prev_c2, n)
                
                ans += count1 * count2
                
                # Move to the next different elements
                r1, c1 = get_next(mat1, r1, c1, n)
                r2, c2 = get_prev(mat2, r2, c2, n)
            elif current_sum < x:
                r1, c1 = get_next(mat1, r1, c1, n)
            else:
                r2, c2 = get_prev(mat2, r2, c2, n)
        
        return ans