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


# Method 2: Optimising to O(1) space
# Link: https://leetcode.com/problems/candy/solutions/135698/simple-solution-with-one-pass-using-o-1-space/
# Logic:
"""
The fundamental idea is that we aren't bothering with calculating each child's 
candy value itself, but rather it's impact on the total needed.
For upwards and equal slopes these values align. 
But for the downward slope we keep track of how much more candies we have to add to the previous kids 
to satisfy the requirement of them having more candy than lower rated neighbours to the right.

This method is basically answering this question: If I insert one more kid to the end of this array, 
how does the total amount of candy needed change.
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # If there are no children (empty ratings list), return 0
        if len(ratings) == 0:
            return 0
        
        # Initialize variables:
        # ret: total number of candies needed (starting with 1 for the first child)
        # up: length of the current increasing sequence of ratings
        # down: length of the current decreasing sequence of ratings
        # peak: length of the last peak in an increasing sequence
        ret = 1
        up = 0
        down = 0
        peak = 0
        
        # Loop through the ratings list starting from the second child (index 1)
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                # If current rating is greater than the previous one, we are in an increasing sequence
                up += 1        # Increase the "up" counter
                peak = up      # Update the peak value
                down = 0       # Reset the "down" counter since we are in the increasing streak 
                ret += 1 + up  # Add candies for the current child and all previous in the increasing sequence
            elif ratings[i - 1] == ratings[i]:
                # If current rating is equal to the previous one, just give 1 candy (no slope)
                peak = up = down = 0  # Reset all counters
                ret += 1              # Add 1 candy for the current child
            else:
                # If current rating is less than the previous one, we are in a decreasing sequence
                up = 0            # Reset the "up" counter since the decreasing streak starts
                down += 1         # Increase the "down" counter
                # Add candies for the current child and adjust based on whether we are still above the peak
                ret += down
                # if peak is not large enough, then we need to make peak larger
                if peak < down:
                    ret += 1

        # Return the total number of candies required
        return ret
        
