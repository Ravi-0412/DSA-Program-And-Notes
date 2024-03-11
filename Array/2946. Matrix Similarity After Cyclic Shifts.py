# After shifting ele at cur index and ele that will come at cur index must be same in each row.  

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m ,n = len(mat) , len(mat[0])
        for i in range(0, m, 2):
            for j in range(n):
                ind = (j + k) % n
                if mat[i][j] != mat[i][ind]:
                    return False
        for i in range(1, m, 2):
            for j in range(n):
                ind = (j - k + n) % n
                if mat[i][j] != mat[i][ind]:
                    return False
        return True


# We can do in one loop also
# suppose we are at 'j'th index in a row 'i' then 
# 1) if we do right shift then 'j'th ele must be equal to '(j + k) % n'.
# 2) if we do left shift then '(j + k) % n'th ele must be equal to 'j'.

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m ,n = len(mat) , len(mat[0])
        for i in range(m):
            for j in range(n):
                ind = (j + k) % n
                if mat[i][j] != mat[i][ind]:
                    return False
        return True
