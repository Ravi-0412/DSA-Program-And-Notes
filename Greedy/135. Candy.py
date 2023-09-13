# every children must be given at least '1' candy.
# So initialise ans array with '1' i.e ans = [1] *n .

# Logic: we have to make sure of two things:
# 1) children with a higher rating get more candy than its left neighbor.
# For this, Traverse from left to right and if :
# ratings[i] > ratings[i-1] : we must give ith child atleast one more candy than (i-1)th child :
# ans[i] = ans[i-1] +1 

# 2)  children with a higher rating get more candy than its right neighbor.
# for this, Traverse from Right to Left and if :
# ratings[i] > ratings[i+1] : we must give ith child atleast one more candy than (i+1)th child:
# ans[i] = ans[i+1] + 1

# Last sum of 'ans' will give the ans.

# Time = space = O(n)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        ans = [1] *n
        for i in range(1, n):
            if ratings[i] > ratings[i -1]:
                ans[i] = ans[i -1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                ans[i] = max(ans[i + 1] + 1, ans[i])  # 
        return sum(ans)


# Try in O(1) space
# https://leetcode.com/problems/candy/solutions/42770/one-pass-constant-space-java-solution/