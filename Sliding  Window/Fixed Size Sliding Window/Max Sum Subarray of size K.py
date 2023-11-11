# 1st method by brute force: O(n*k)

# 2nd method: By Sliding Window
# time: O(n)

# little concise way of writing the above code
# once you reach that window size, just keep updating your ans and remove the ele at 'i'th index from sum and incr 'i'
def maximumSumSubarray (self,K,Arr,N):
        i,j,sum1,max_sum= 0,0,0,-9999999999
        while j<N:
            sum1+= Arr[j]
            if j+1>=K:     # or j -i + 1 >= k:
                # Now we have reached the size 'k' so we can start updating our ans.
                max_sum= max(sum1, max_sum)
                sum1-= Arr[i]
                i+= 1
            j+= 1
        return max_sum


# Note vvvvi: At any instant curSum= sum of ele till index 'j' - sum of ele before index 'i'.
# it just represents sum of ele from index 'i' to index 'j'.  i.e prefixSum[j] - prefixSum[i-1]

