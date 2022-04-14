# time: O(n)
# VVVI: analyse this and pre same problem properly
class Solution:
    def lenOfLongSubarr (self, A, N, K) : 
        # just same logic ass no of subarray with given sum 'k'
        prefix_sum= {}  # this time we will initialise for '0' as we have to find the length
        max_length,curr_sum= 0, 0
        for i in range(N):
            curr_sum+= A[i]
            if curr_sum== K:
                max_length= i+1
            elif (curr_sum-K) in prefix_sum:  # just same logic as 'no of subarray with given sum'
                max_length= max(max_length,i-prefix_sum[curr_sum-K])  # if 'diff' is present in the array then update the max_length
            # only add the curr_sum in prefix_sum if it is not present
            # as we have to find the max_length
            if curr_sum not in prefix_sum:
                prefix_sum[curr_sum]= i
                
        return max_length

