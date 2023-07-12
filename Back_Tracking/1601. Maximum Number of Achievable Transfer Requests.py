# Logic: Maximum no of request we can accept such that for all building net leaving and moving = 0
# so we have to check all the possibility.

# vvi : if we can ignore some request then may get the optimal ans i.e case when all building has leaving = moving.
# So from this, we get the idea that for every building we have two choices
#  i.e 1) Accept that or 2) Not accept that.

# Time Complexity: O(N * 2 ^ R)

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        count = [0]*n   # if leaving then we will incr the count by '1' else decrease by '1'.
        self.ans= 0
        
        def backtrack(i, reqAccepted):
            if i == len(requests):
                for c in count:
                    if c != 0:
                        return
                self.ans = max(self.ans, reqAccepted)
                return
            # if we accept the cur request
            f, t= requests[i]    # from, to
            count[f] += 1
            count[t] -= 1
            backtrack(i +1, reqAccepted + 1)
            # alter the made changes while coming back
            count[f] -= 1
            count[t] += 1

            # if we don't accept the request
            backtrack(i +1, reqAccepted)       

        backtrack(0, 0)
        return self.ans
    

# Doing like this is giving error don't know why.
# Have to ask someone.
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        count = [0]*n   # if leaving then we will incr the count by '1' else decrease by '1'.
        
        def backtrack(i):
            if i == len(requests):
                for c in count:
                    if c != 0:
                        return float('-inf')  # return any very large negtaive value so this combination didn't get included in ans.
                return 0

            ans = 0
            # if we accept the cur request
            f, t= requests[i]
            count[f] += 1
            count[t] -= 1
            ans = max(ans, 1 + backtrack(i +1))
            # alter the made changes while coming back
            count[f] -= 1
            count[t] += 1

            # if we don't accept the request
            ans = max(ans, backtrack(i +1))
            return ans
                
        return backtrack(0)