# Note vvi: if n = a + b + c + .... then n^2 > a^2 + b^2 + c^2 + ...
# So it is better to remove the maximum possible ele of same color to get the maximum points.

# Recursive way TLE

# Note : Let dp(l, r, k) denote the maximum points we can get in boxes[l..r] if we have extra k boxes which is the same color with boxes[l] in the left side.
# For example: boxes = [3, 3, 1, 3, 3]
# The dp(l=3, r=4, k=2) is the maximum points we can get in boxes[3..4] if we have extra 2 boxes the same color with boxes[3] in the left side, 
# it's the same as we find the maximum points in boxes = [3, 3, 3, 3] .

# Since (a+b)^2 > a^2 + b^2, where a > 0, b > 0, so it's better to greedy to remove all contiguous boxes of the same color, instead of split them.
# So we increase both l and k while boxes[l+1] == boxes[l].

# Now, we have many options to consider:

# Option 1, remove all boxes which has the same with boxes[l], total points we can get is dp(l+1, r, 0) + (k+1)*(k+1) (k left boxes and the lth box have the same color)
# Other options, we try to merge non-contiguous boxes of the same color together, by:
# Find the index j, where l+1 <= j <= r so that boxes[j] == boxes[l].
# Total points we can get is dp(j, r, k+1) + dp(l+1, j-1, 0)

# https://leetcode.com/problems/remove-boxes/solutions/1402561/c-java-python-top-down-dp-clear-explanation-with-picture-clean-concise/
# https://www.youtube.com/watch?v=ncW3zm_J3qY

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        def points(i, j, k):
            if i>j:
                return 0
            # 1) 1st choice is to calculate the ans here i.e remove the same color boxes as boxes[i]
            # for this check if there is more boxes of same color as boxes[i] on right (just an optimisation to reduce the no of recursive calls)
            # this will tell number of boxes[i] to the left of curr 'i' when we will remove middle numbers

            while i + 1 <= j and boxes[i]== boxes[i+1]:
                i+= 1
                k+= 1   # streak of same color will increase
            # # option1 is to remove the current ith number. we will left with '0' streak for next as it will be distinct only.
            ans= (k + 1)* (k + 1) + points(i+1, j, 0)   # 'k+1' because cur box i.e box[i] we have to add also

            # option 2 is to remove the number in the middle to get more boxes together as boxes[i]
            # e.g: [1,2,2,1,2,2], if i = 2 then it is better to remove '1'(3rd index) to get more '2' together for max points
            
            # Note: Here we will remove the middle values only when there is chances of getting same value later 
            # If not then this case(unequal one) will get covered in above recursive call only.
            for m in range(i+1, j+1):
                if boxes[i]== boxes[m]:
                    # if we can get some more boxes of same color as boxes[i].
                    # we will split from here. streak will continue to the right part(k + 1) and left part streak will break (0)
                    ans= max(ans, points(i+1, m-1, 0) + points(m, j, k + 1))  # Here not adding the cost since cost of it will get calculated before above recursive function only.
            return ans

        n= len(boxes)
        i, j, k= 0, n-1, 0
        return points(i, j, k)


# time: O(n^4)
# space: O(n^3)
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        def points(i, j, k):
            if i > j:
                return 0
            if dp[i][j][k]!= -1:
                return dp[i][j][k]
            i0, k0= i, k   # we will return for the calling variable for which function was called  at last (in dp)
                           # As we are changing the value of 'i', and 'k' so we have to store these value somewhere.

            # 1) 1st choice is to calculate the ans here i.e remove the same color boxes as boxes[i]
            # for this check if there is more boxes of same color as boxes[i] on right (just an optimisation to reduce the no of recursive calls)
            # this will tell number of boxes[i] to the left of curr 'i' when we will remove middle numbers

            while i + 1 <= j and boxes[i]== boxes[i+1]:
                i+= 1
                k+= 1   # streak of same color will increase

            #  remove the cur 'i'th ele.
            ans= (k + 1)* (k + 1) + points(i+1, j, 0)   # 'k+1' because cur box i.e box[i] we have to add also

            # option 2 is to remove the number in the middle to get more boxes together as boxes[i]
            # e.g: [1,2,2,1,2,2], if i = 2 then it is better to remove '1'(3rd index) to get more '2' together for max points
            for m in range(i+1, j+1):
                if boxes[i]== boxes[m]:
                    # we will split from here. streak will continue to the right part(k + 1) as we are including 'm' in right part and left part streak will break (0)
                    ans= max(ans, points(i+1, m-1, 0) + points(m, j, k + 1))
            dp[i0][j][k0] = ans
            return dp[i0][j][k0]

        n= len(boxes)
        dp= [[[-1 for t in range(n+ 1)] for j in range(n +1)] for i in range(n +1)]
        i, j, k= 0, n-1, 0  
        return points(i, j, k)


