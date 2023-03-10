# logic in notes, page: 126

# Recursive way TLE
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        def points(i, j, k):
            if i>j:
                return 0
            # first find the consecutive number starting with boxes[i]
            # this will tell number of boxes[i] to the left of curr 'i' when we will remove middle numbers. 
            while i + 1 <= j and boxes[i]== boxes[i+1]:
                i+= 1
                k+= 1
            # option1 is to remove the current ith number
            ans= (k+1)* (k+1) + points(i+1, j, 0)

            # option 2 is to remove the number in the middle if there is some number which is same as boxes[i]
            for m in range(i+1, j+1):
                if boxes[i]== boxes[m]:
                    ans= max(ans, points(i+1, m-1, 0) + points(m, j, k +1))
            return ans

        n= len(boxes)
        i, j, k= 0, n-1, 0
        return points(i, j, k)


# time: O(n^4)
# space: O(n^3)
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        def points(i, j, k, dp):
            if i>j:
                return 0
            if dp[i][j][k]!= -1:
                return dp[i][j][k]
            i0, k0= i, k   # we will return for the calling variable for which function was called  at last (in dp)
            # first find the consecutive number starting with boxes[i]
            # this will tell number of boxes[i] to the left of curr 'i' when we will remove middle numbers. 
            while i + 1 <= j and boxes[i]== boxes[i+1]:
                i+= 1
                k+= 1
            # option1 is to remove the current ith number
            ans= (k+1)* (k+1) + points(i+1, j, 0, dp)

            # option 2 is to remove the number in the middle if there is some number which is same as boxes[i]
            for m in range(i+1, j+1):
                if boxes[i]== boxes[m]:
                    ans= max(ans, points(i+1, m-1, 0, dp) + points(m, j, k +1, dp))
            dp[i0][j][k0]= ans
            return dp[i0][j][k0]

        n= len(boxes)
        dp= [[[-1 for t in range(n+ 1)] for j in range(n +1)] for i in range(n +1)]
        i, j, k= 0, n-1, 0
        return points(i, j, k, dp)
