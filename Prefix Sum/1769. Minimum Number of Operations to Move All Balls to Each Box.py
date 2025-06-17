# Method 1: 
# Brute force
# Time: O(n^2), space: O(n)

"""
Just find the distance of each from one on left and right for each index.
"""

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # Get the total number of boxes
        n = len(boxes)
        # Initialize the answer array with zeros
        ans = [0] * n
        
        # Iterate over each box to calculate the number of operations required
        for i in range(n):
            # Initialize the count of operations required to move balls from the left
            leftCount = 0
            # Start checking boxes to the left of the current box
            j = i - 1
            while j >= 0:  # Continue until the first box
                if boxes[j] == '1':  # If a box contains a ball
                    # Add the distance between the current box and the box with the ball
                    leftCount += i - j
                j -= 1  # Move to the previous box
            
            # Initialize the count of operations required to move balls from the right
            rightCount = 0
            # Start checking boxes to the right of the current box
            k = i + 1
            while k < n:  # Continue until the last box
                if boxes[k] == '1':  # If a box contains a ball
                    # Add the distance between the current box and the box with the ball
                    rightCount += k - i
                k += 1  # Move to the next box
            
            # The total operations for the current box is the sum of left and right operations
            ans[i] = leftCount + rightCount
        
        # Return the result array with the minimum number of operations for each box
        return ans


# Methoid 2: 
# short version of Method 1

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        for i in range(n):
            for j in range(n):
                if boxes[j] == '1':
                    ans[i] += abs(j-i)
        return ans


# Method 3: 
# Optimised to O(n)
"""
DP Left to Right and Right To Left

Let leftDist[i] is the total distance after moving all the ball from the left side to ith box.
Let leftBallCnt is the number of balls after moving all the ball from the left side to ith box so far.
To calculate leftDist[i], we need to move leftBallCnt balls from (i-1)th box by one, so total distance:
leftDist[i] = leftDist[i-1] + leftBallCnt
Do the same with rightDist[i] and rightBallCnt in the right side.
To calculate total distance after moving all the ball from the left and the right side to ith box:
ans[i] = leftDist[i] + rightDist[i]
"""

class Solution(object):
    def minOperations(self, boxes):
        n = len(boxes)

        leftDist = [0] * n
        leftBallCnt = int(boxes[0])
        for i in range(1, n):
            leftDist[i] = leftDist[i - 1] + leftBallCnt
            leftBallCnt = leftBallCnt + int(boxes[i])

        rightDist = [0] * n
        rightBallCnt = int(boxes[n - 1])
        for i in range(n - 2, -1, -1):
            rightDist[i] = rightDist[i + 1] + rightBallCnt
            rightBallCnt = rightBallCnt + int(boxes[i])

        ans = [0] * n
        for i in range(n):
            ans[i] = leftDist[i] + rightDist[i]
        return ans
