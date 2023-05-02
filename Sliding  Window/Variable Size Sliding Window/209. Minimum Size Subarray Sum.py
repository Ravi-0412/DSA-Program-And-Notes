# Note: Appplied same logic as "76. Minimum Window Substring".
# i.e keep chekcing if you have find any ans and then try to shrink the subarray and keep updating the ans.
# Exactly same as "713. Subarray Product Less Than K"

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n= len(nums)
        ans= n + 1  # max we can get ans= n
        i, j= 0, 0
        curSum= 0
        while j < n:
            curSum+= nums[j]
            while curSum >= target:
                ans= min(ans, j -i + 1)
                curSum-= nums[i]
                i+= 1
            j+= 1
        return ans if ans!= float('inf') else 0


# Note: it won't work if there is "-ve" number also since inner while loop can break before finding the 
# shortest subarray after adding the curr ele.

# e.g: [84,-37,32,40,95], target= 167.
# it will give output= 5 but it will be equal= 3.


# method 2: logic of Q :"862. Shortest Subarray with Sum at Least K"
# just commented the 2nd while loop.

# just think 'prefixSum[j] - prefixSum[q[0]]' = CurSum and q for storing all the possible index from where we can get the subarray.

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
    

