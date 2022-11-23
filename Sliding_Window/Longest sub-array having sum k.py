# time: O(n)= space
# this approach will work for both positive and negative number
# VVVI: analyse this and pre same problem properly

class Solution:
    def lenOfLongSubarr (self, A, N, K) : 
        # just same logic as no of subarray with given sum 'k'
        prefix_sum= {}  
        max_length,curr_sum= 0, 0
        for i in range(N):
            curr_sum+= A[i]
            if curr_sum== K:  # then automatically max_length will be equal= i+1
                max_length= i+1
            elif (curr_sum-K) in prefix_sum:  # then it means sum= k is posibble after the value(index only) of 'curr_sum -k' in prefix_sum 
                                            # like after that value till curr index we can get the required sum as "curr_sum-k" is extra and we to remove that extra index
                                            # extra sum can be negative or positive no problem                                
                max_length= max(max_length,i-prefix_sum[curr_sum-K])  

            # Add the curr_sum if not present. if we update always then we will not get our actual ans as it will reduce the length when it will found as extra sum i.e 'curr_sum -k'
            if curr_sum not in prefix_sum:
                prefix_sum[curr_sum]= i    # i will tell the length of key in the prefix_sum 
                
        return max_length



# if no given is only positive then we can apply sliding window with two pointer

def lenOfLongSubarr(A, N, K):
    i, j, sum = 0, 0, 0
    maxLen = -sys.maxsize -1
    while j < N:
        sum += A[j]
        if sum == K:
            maxLen = max(maxLen, j - i + 1)
        elif sum > K:   # pop ele i.e subtract the 'ith' index ele from sum till it becomes smaller than  'k'
            while (sum > K):
                sum -= A[i]
                i += 1
            if (sum == K):   # while subtracting it make become= k also then update the ans
                  maxLen = max(maxLen, j - i + 1)
        j += 1
    return maxLen


