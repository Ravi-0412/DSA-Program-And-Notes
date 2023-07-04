# Logic: Maximum no of request we can accept such that for all building net leaving and moving = 0
# so we have to check all the possibility.

# For every request we have two choice i.e 1) Accept that or 2) Not accept that.

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
    

# My mistake :
# i just thought just accept all request then add the count of all those building whose leaving = moving.
# In this case we amy wrong ans or even '0' sometime.

# But if we can ignore some request then may get the ans i.e case when all building has leaving = moving.

# So from we get the idea that for every building we have two choices.
# That's what we implemented above.

# my code.
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        leaving  = [0]*n
        moving =   [0]*n
        for i, j in requests:
            leaving[i] += 1
            moving[j]   += 1
        print(leaving, moving)
        ans = 0
        for i in range(n):
            if leaving[i] == moving[i]:
                ans += leaving[i]
        return ans