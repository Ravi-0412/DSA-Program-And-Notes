#Intuition
# Consider the starting number X as start vertex. Consider y as target vertex where we have to reach in minimum number of steps.
# At each step, we have 4 options.
# 1)If the number X is divisible by 11, then divide by 11.
# 2)If it is divisible by 5,then divide by 5.
# 3)Increment x by 1
# 4)Decrement x by 1.

# Approach:
# This problem like minimum numbers of steps needed to reach from source to destination 
# with every vertex having 4 possible paths as x+1, x-1, x/11 and x/5. (x/11 and x/5 needs condition check).

# So from each number we get, we push the 4 numbers (x+1, x-1, x/5, x/11) into queue after checking the conditions.

# We also need to maintain an visited array to maintain the numbers which have been visited earlier. 
# For example, If I earlier got 6, then after doing x-1 we get 5, 
# then we should not go back to x+1 to get 6. So we mark visited every time we get a new number.

# Note: 1st time you will see 'y' that will be the ans only.

# Complexity
# Time complexity:
# O(max(X, Y))

# Can do using single source bfs using extra parameter


class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if y >= x:
            return y - x
        q = collections.deque()
        ans = 0
        visited = set()
        q.append(x)
        visited.add(x)
        while q:
            for i in range(len(q)):
                num = q.popleft()
                if num == y :
                    return ans
                if num > 10**4 or num <= 0:
                    continue
                # apply all four condition on 'num'
                # Avoid going that num which has been already visited
                if num % 11 == 0 and num // 11 not in visited:
                    q.append(num // 11)
                    visited.add(num // 11)
                if num % 5 == 0 and num // 5 not in visited:
                    q.append(num // 5)
                    visited.add(num // 5)
                if num - 1 > 0 and num - 1 not in visited:
                    q.append(num - 1)
                    visited.add(num -1)
                if num + 1 <= 10 **4 and num + 1 not in visited:
                    q.append(num + 1)
                    visited.add(num + 1)
            ans += 1


# vvi: Did by DP also
class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if y >= x:
            return y - x
        
        def solve(x):
            if y >= x:
                return y - x
            if dp[x] != -1:
                return dp[x]
            ans = abs(y - x )  # maximum possible ans
            option1 = 1 + x % 5 + solve(x// 5)   # After this operation next x = x //5
            option2 = 1 + (5 - x % 5) + solve(x// 5 + 1) # After this operation next x = x //5 + 1
            option3 = 1 + x % 11 + solve(x// 11)   # After this operation next x = x //11
            option4 = 1 + (11 - x % 11) + solve(x// 11 + 1) # After this operation next x = x //11 + 1
            ans = min(ans, option1, option2, option3, option4)
            dp[x] = ans
            return dp[x]

        dp = [-1] * (10**4 + 11)
        solve(x)
        return dp[x]
