# Just you have to keep track of order of pieces.

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        order = {}  # [ele: index]. To keep track whether ele is getting served in same order or not for same piece.
                    # index of elements of pieces must be continous
        cnt = 0
        for i, num in enumerate(arr):
            order[num] = i
        for i in range(len(pieces)) :
            for j in range(len(pieces[i])) :
                # index whether ele is continous or not, using index value.
                if pieces[i][j] not in order or (j > 0 and order[pieces[i][j]] != order[pieces[i][j - 1]] + 1) :
                    return False
                cnt += 1
        return cnt == len(arr)


# My mistake in 1st try
# arr = [1,2,3], pieces = [[2],[1,3]].
# Giving : True but ans should be 'False'.

# No need of pre also we can check using index value.

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        order = {}
        cnt = 0
        for i, num in enumerate(arr):
            order[num] = i
        for i in range(len(pieces)) :
            pre = -1
            for j in range(len(pieces[i])) :
                if pieces[i][j] not in order or order[pieces[i][j]] < pre:
                    return False
                pre = order[pieces[i][j]]
                cnt += 1
        return cnt == len(arr)
        