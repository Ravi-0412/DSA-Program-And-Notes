# 1st method by brute force: O(n*k)

# 2nd method: By Sliding Window
# time: O(n)
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        i,j,sum,max_sum= 0,0,0,-999999999
        while(j<N):
            sum+= Arr[j]
            if j-i+1 <K:  # means we have not reached the size of the window
                          # so only incr j. keep incr j only until you recah the req win size
                j+= 1
            elif j-i+1== K: # means we have reached the size of the window
                            # so update the max_sum and sum and incr j and j also
                max_sum= max(max_sum,sum)
                sum-= Arr[i]    # now remove the 'ith' ele from sum for next iteration
                # now update the pointers to maintain the window size 
                i+= 1
                j+= 1
        return max_sum


# little concise way of writing the above code
# once you reach that window size, just keep updating your ans and remove the ele at 'i'th index from sum and incr 'i'
def maximumSumSubarray (self,K,Arr,N):
        i,j,sum1,max_sum= 0,0,0,-9999999999
        while j<N:
            sum1+= Arr[j]
            if j+1>=K:
                max_sum= max(sum1, max_sum)
                sum1-= Arr[i]
                i+= 1
            j+= 1
        return max_sum


# Note vvi: At any instant curSum= sum of ele till index 'j' - sum of ele before index 'i'.
# it just represents sum of ele from index 'i' to index 'j'.  (prefixSum way).

