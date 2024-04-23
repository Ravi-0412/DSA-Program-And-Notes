# if no given is only positive then we can apply sliding window with two pointer.

class Solution:
    def lenofLongestSubarray(self, nums, target) :
        n = len(nums)
        ans = -1  # any min value that can't be ans
        i, j = 0, 0
        curSum = 0
        while j < n:
            curSum += nums[j]
            # Keep on removeing ele from start for till subarray sum is invalid
            while i <= j and curSum > target:
                curSum -= nums[i]
                i += 1
            if curSum == target:
                ans = max(ans , j - i + 1)
            j += 1
        return -1 if ans == -1 else n - ans


# Solution: will work with both positive and negative numbers.

# time: O(n)= space

# vvi: just similar to "Two sum" method.
# this approach will work for both positive and negative number
# VVVI: analyse this and pre same problem properly

# isme hm invalid case like 'curr_sum > k' check nhi kar rhe kyonki aage number negative aake sum ko reduce kar sakta h
# isliye yahan hm koi ele ko remove nhi kar sakte.. so bina two pointer ke karna easy rhega.

# Note: agar 'k- curSum' check karenge hashmap me to galat ans dega kyonki let say remainingSum= x
# then k- curSum= x  => k= curSum + x which is not True But
# curSum - k = x  then  curSum = k + x which is True. Means we can get curSum by adding 'k' to the remainingSum (x).
# it also means we can get 'k' by removing remainingsum .

# Note: hm map me agar curSum present nhi h tb hi hm "update" kar rhe (i.e first time only) because we wanted the longest subarray.
# vvi: if have told to "find the Smallest subarray with sum equal to k" then we will update everytime to minimise the length.

class Solution:
    def lenOfLongSubarr (self, A, N, K) : 
        # just same logic as no of subarray with given sum 'k'
        prefix_sum= {}    # will store the [curr_sum: index]
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


# Another way of writing the above logic 
# Better one

# just will check for complement each time not by curSum.
# very good and concise approach.
class Solution:
    def lenOfLongSubarr (self, A, N, K) : 
        # just same logic as no of subarray with given sum 'k'
        prefix_sum= {0:-1}    # for handling the corner case when 'curSum-k'== 0. it will only mean that 'curSum==k' in above logic.
        max_length,curr_sum= 0, 0
        for i in range(N):
            curr_sum+= A[i]
            if (curr_sum-K) in prefix_sum:                                  
                max_length= max(max_length,i-prefix_sum[curr_sum-K])  

            # Add the curr_sum if not present. if we update always then we will not get our actual ans as
            # it will reduce the length when it will found as extra sum i.e 'curr_sum -k'
            if curr_sum not in prefix_sum:
                prefix_sum[curr_sum]= i    # i will tell the length of key in the prefix_sum 
                
        return max_length


# Note: Agar 'curSum; check karenge har ele ke bad then ye question reduce ho jayega
# "Largest subarray with 0 sum".


# Note: Agar smallest subarray pucha hota tb 'Har bar index' ko update karte taki range small ho.

# Related Q:
# 1) "Smallest Subarray with Sum K"
# 2) "1658. Minimum Operations to Reduce X to Zero"
# 3) "560. Subarray Sum Equals K"



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

