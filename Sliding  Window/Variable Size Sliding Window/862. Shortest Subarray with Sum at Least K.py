# vvi: Poistive values solution won't work since no is "-ve" number also because
#  inner while loop can break before finding the shortest subarray after adding the curr ele.
# e.g: [3,-2,5], k= 4. 
# if we will apply "+ve" values soln then output= 3 but ans should = 1.

# how to Handle the negative value?

# Note: "q" is storing the possible starting index from wich we can start our subarray for ans.
# And in every iteration , we are removing those index which can't be starting index of our ans subarray.

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n= len(nums)
        prefixSum= [0] *(n+1)
        for i in range(n):
            prefixSum[i+ 1]= prefixSum[i] + nums[i]
        q= collections.deque()
        ans= n + 1
        j= 0  # starting from '1' will give wrong ans.
        # our last prefixSum is at index 'n' so we will go till 'n'
        while j < n + 1:
            # for handling "+ve num" if found ans then try to shrink just like we used to do.
            while q and prefixSum[j] - prefixSum[q[0]] >= k:
                ans= min(ans, j - q.popleft())
            # to handle the "-ve" number.
            # it means the sum from index 'q[-1]' before curr index is '-ve'.
            # so if we start our ans subarray from index 'q[-1]' then it will be longer only because to reach the 
            # sum >= target from index 'q[-1]', we have to include the ele beyond beyond curr index 'j' also.
            # so why to start from that, better start from curr index 'j' to get shorter length.
            # That's why pop all those index.
            while q and prefixSum[j] <= prefixSum[q[-1]]:
                q.pop()
            q.append(j)   # every index can be possible starting index for ans subarray.
            j+= 1
        return ans if ans <=n else -1


# Note: if you will comment the "2nd while loop" then it will work for "+ve" values
# submitted by commenting for Q: "209. Minimum Size Subarray Sum".

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
