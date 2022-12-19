# time: O(n)= space
# this approach will work for both positive and negative number
# VVVI: analyse this and pre same problem properly

# isme hm invalid case like 'curr_sum>k' check nhi kar rhe kyonki aage number negative aake sum ko reduce kar sakta h
# isliye yahan hm koi ele ko remove nhi kar sakte.. so bina two pointer ke karna easy rhega
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
        if sum == K: # condition is valid
            maxLen = max(maxLen, j - i + 1)
        elif sum > K: # if condition is invalid then pop ele i.e subtract the 'ith' index ele from sum till it becomes smaller than  'k'
            while (sum > K):
                sum -= A[i]
                i += 1
            if (sum == K):   # while subtracting it make become= k also then update the ans
                  maxLen = max(maxLen, j - i + 1)
        j += 1
    return maxLen


# Note VVVI: ek cheez Variable size sliding window me hmesha yaad rakho
# 1)agar koi ele ans wala condition ko follow kar rha h tb include karte raho ya ans ke anusar(liye) 
# curr index wala ele here 'j' me operation karte raho..and

# 2) then check karo for two cases:
# i) check for valid condition i.e if condition is valid. agar jo chahiye wo condition reach kar gya ho
# then ans ko update karo 

# ii) elif check for proper invalid condition acc to Q i.e if condition is invalid
# then pre index say 'i' pe tab tak operate karo(or do the process to remove pre index 'i'th ele)
# jb tak condition valid n ho jaye(use while loop with same elif condition) and while trying to making condition valid. 
# you may come across valid case also inside this so,every time you operate on pre index 'i'
# then keep checking for valid case also , if found add that to ans.. That's it

# yhi do case bnega isme

