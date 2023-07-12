# Note: Appplied same logic as "76. Minimum Window Substring".
# i.e keep chekcing if you have find any ans and then try to shrink the subarray and keep updating the ans.

# Here all ele is +ve and we are asked to find the minimum length so if curSum becomes >= target then we will have to remove ele from left
# Because adding more ele will lead to more curSum and we will get the wrong ans(i.e bigger value than expected).

# Note vvi: Whenever asked to find the minimum subarray length and that we can get by shrinking the window 
# then, always we will update the ans while shrinking the window till condition is valid i.e inside 2nd while loop.

# vvi: i.e condition bhi >= ka ho and minimum bhi chahiye then yhi logic use karenge.
# shrink the window in valid conition to get the minimum ans (keep updating the ans while whrinking the window).

# Note : We can also check if there exist any possible subarray or not.
# If sum(nums) < target then no subarray possible.

# How to solve?
# Ans: Just keep on adding the cur ele to 'sum' and after adding keep on reducing the window size from left
# till our window is valid because we need the 'minimum' length of subarray.

# Just similar logic as "76. Minimum Window Substring".

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n= len(nums)
        ans= n + 1  # max we can get ans= n  # genralise  ans = float('inf')
        i, j= 0, 0
        curSum= 0
        while j < n:
            curSum+= nums[j]
            while curSum >= target:
                ans= min(ans, j -i + 1)
                curSum-= nums[i]
                i+= 1
            j+= 1
        return ans if ans!= n + 1 else 0


# Note: it won't work if there is "-ve" number also since inner while loop can break before finding the 
# shortest subarray after adding the curr ele.

# e.g: [84,-37,32,40,95], target= 167.
# it will give output= 5 but it should be equal= 3.
# Reason: '95' ko add karne ke bad sum >= 167 ho jayega and jb hm window ko shrink karenge after removing
# '87' then sum < 167 ho jayega and loop break ho jayega. 
# But agar '-37' ko bhi remove kar de tb bhi mera sum > 167 rhega but ye case consider hi nhi hoga.
# e.g: [3,-2,5], k= 4. 
# output= 3 but ans should = 1.


# method 2: logic of Q :"862. Shortest Subarray with Sum at Least K"
# just commented the 2nd while loop of above Q.

# just think 'prefixSum[j] - prefixSum[q[0]]' = CurSum and
#  q for storing all the possible index from where we can get the valid subarray.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n= len(nums)
        prefixSum= [0] *(n+1)
        for i in range(n):
            prefixSum[i+ 1]= prefixSum[i] + nums[i]
        q= collections.deque()
        ans= n + 1
        j= 0
        while j < n + 1:
            # if found ans then try to shrink just like we used to do for "+ve" values
            while q and prefixSum[j] - prefixSum[q[0]] >= target:
                ans= min(ans, j - q.popleft())
            # while q and prefixSum[j] <= prefixSum[q[-1]]:
            #     q.pop()
            q.append(j) 
            j+= 1
        return ans if ans <=n else 0
    

