# Explantion in notes, page no = 168

# Time : O(n)
class Solution:
    def maximumBooks(self, books):
        n = len(books)
        diff = [0]*n
        for i in range(n):
            diff[i] = books[i] - i
        # Now find the 1st smaller on left for each element in 'diff' arr.
        nextSmallerLeft = [-1] * n
        stack = []   # will store [value , index]
        for i in range(n):
            while stack and stack[-1][0] >= diff[i]:
                stack.pop()
            if stack:
                nextSmallerLeft[i] = stack[-1][1]   # index 
            stack.append([diff[i], i])
        # print(diff, nextSmallerLeft)
        
        # now Apply dp to get the ans
        dp = [0] * n
        # dp[i]: denotes maximum sum we can get for a subarray ending at index i
        dp[0] = books[0]
        for i in range(n):
            prev = nextSmallerLeft[i]
            if prev != -1:
                noOfEle = i - prev    # no of elements in subarray forming AP with cd = 1 having last element as books[i]
                firstValue = books[i] - noOfEle + 1   # starting value of this AP
                sum = ((firstValue + books[i]) * noOfEle) // 2
                dp[i] = max(sum, sum + dp[prev])
            else:
                # means all elements from index '0' to index 'i' forms AP with cd = 1
                # maximum no of ele can be = i + 1 but can't be more than books[i] when books[i] is the last ele of AP.
                noOfEle = min(i + 1, books[i])
                firstValue = books[i] - noOfEle + 1   # starting value of this AP
                sum = ((firstValue + books[i]) * noOfEle) // 2
                dp[i] = sum  # only equal to sum.
        
        return max(dp)   # our ans will be equal to maximum value in dp

s = Solution()
# books = [8,5,2,7,9]
books = [8,2,3,7,3,4,0,1,4,3]
books = [7,0,3,4,5]
books = [4, 2, 3, 1]
print("ans: ", s.maximumBooks(books))

