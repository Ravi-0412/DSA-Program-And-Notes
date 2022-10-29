# My mistakes
# in this i was not doing any operation in case of no match
# so if in case if (0,0) doesn't match then it was simply returning false
# but we have to check further cell also in case doesn't matches

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.helper(0,0,board,word)
    
    def helper(self,row,col,board,word):
        if not word:
            return True
        if board[row][col]== word[0]:
            temp= board[row][col]
            board[row][col]= True     # so that next time it does not take this same cell in case matches
            if col+1 <len(board[0]) and board[row][col+1]!= True:  # can go right
                if self.helper(row,col+1,board,word[1:]):
                    return True
            if col-1 >=0 and board[row][col-1]!= True:  # can go left
                if self.helper(row,col-1,board,word[1:]):
                    return True
            if row-1 >= 0 and board[row-1][col]!= True:  # can go up
                if self.helper(row,col+1,board,word[1:]):
                    return True
            if row+1 <len(board) and board[row+1][col]!= True:  # can go right
                if self.helper(row+1,col,board,word[1:]):
                    return True
            board[row][col]= temp

# here it is giving "maximum recursion depth exceeded"
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.helper(0,0,board,word)
    
    def helper(self,row,col,board,word):
        if not word:
            return True
        if board[row][col]!= word[0]:
            if col+1 <len(board[0]):  # can go right
                if self.helper(row,col+1,board,word):
                    return True
            if col-1 >=0 and board[row][col-1]!= True:  # can go left
                if self.helper(row,col-1,board,word):
                    return True
            if row-1 >= 0 and board[row-1][col]!= True:  # can go up
                if self.helper(row-1,col,board,word):
                    return True
            if row+1 <len(board) and board[row+1][col]!= True:  # can go down
                if self.helper(row+1,col,board,word):
                    return True
        
        if board[row][col]== word[0]:
            temp= board[row][col]
            board[row][col]= True     # marking visited ,so that next time it does not take this same cell in case matches
            if col+1 <len(board[0]) and board[row][col+1]!= True:  # can go right
                if self.helper(row,col+1,board,word[1:]):
                    return True
            if col-1 >=0 and board[row][col-1]!= True:  # can go left
                if self.helper(row,col-1,board,word[1:]):
                    return True
            if row-1 >= 0 and board[row-1][col]!= True:  # can go up
                if self.helper(row-1,col,board,word[1:]):
                    return True
            if row+1 <len(board) and board[row+1][col]!= True:  # can go down
                if self.helper(row+1,col,board,word[1:]):
                    return True
            board[row][col]= temp
        return False



# to call the function only at once at any cell better so like this always in case of grid problem
# correct only but giving TLE
# time: O(m*n*dfs), dfs will take O(l) for each call and we have four choices at each step so time complecity of dfs= O(4^l), l= len(word)
# # total time complexity= O(m*n*4^l) 
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col= len(board), len(board[0])
        path= set()
        
        def dfs(r,c,word):
            if not word:
                return True
            if r<0 or r>=row or c<0 or c>= col or board[r][c]!= word[0] or (r,c) in path:
                return False
            # it means we have found the matching char at (r,c)
            path.add((r,c))  # added in path so that this cell char doesn't repeat in same cycle
            res= dfs(r,c-1,word[1:])  or dfs(r,c+1,word[1:]) or dfs(r-1,c,word[1:]) or dfs(r+1,c,word[1:])    # left,right,up,down
            # now backtrack if we don't ans by adding the char at (r,c)
            path.remove((r,c))
            return res
        
        for r in range(row):
            for c in range(col):
                if dfs(r,c,word):
                    return True
        return False

# if we don't want to use the path set for visited then do like this. this i did in my mistake (2nd one)
# Tle
class Solution:
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res
        