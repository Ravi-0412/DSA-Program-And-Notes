# store in dictionary and count the value 
# time: o(n), space= o(n)
# submitted on GFG
class Solution:
    def singleElement(self, arr, N):
        hashmap= {}
        for num in arr:
            if num not in hashmap:
                hashmap[num]= 1
            else:
                hashmap[num]+= 1
        for i in range(N):
            if hashmap[arr[i]]!=3:
                return arr[i]


# method 2: (submitted on GFG): Good one
# Logic: find the 3*(sum of all distinct no) - sum(array)
# after this you will left with 2*missing_number
# so now divide it by two
#  and we can get sum of all distinct no by storing in set

# this is valid for all this type of problem for every frequency

# time: O(n), space: O(n)

class Solution:
    def singleElement(self,arr, N):
        return (3*sum(set(arr))-sum(arr))//2


# method 3: submitted on Leetcode
# using 'Counter' object
# counter counts  fre of all the obj in a list,tuple
# internally it creates a dictionary only
# time: n, space: n
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        frequency= Counter(nums) # a dictionary will be created storing
                                 # the fre of each ele
        for i in frequency:
            if frequency[i]==1:
                return i


# method 4: find the sum of set bits at all the positions and divide by 3
# if sum of set bits at that position is not divisible by 3 then it means the single number has set bit at that position
# time: O(32* n)
# This method will work only for positive number

def singleNumber(self, nums: List[int]) -> int:
        ans= 0
        for i in range(32): # since max bits in any number can be 32
            check_set= 1<< i   # to check whether ith bit of that num is set bit or not so took left shift of 1 'i' times
            sum_bits = 0      
            for num in nums:
                if num & check_set:  # if 1 then 
                    sum_bits+= 1    # add to the set_bit
            if sum_bits %3!= 0:     # now check whether sum of set bits at that position is divisible by 3 or not 
                                    # if not divisible by 3 then
                ans= ans | check_set   # put '1' at ith position in the ans keeping other bit zero
        return ans


# method 4: needs a lot of thinking but better method
# using bit manipulation
#submitted on leetcode(didn't do myself)
# have to look later properly
# time: O(n)

# logic:  "ones" and "twos" to be sets that are keeping track of which numbers have appeared once and twice respectively.
# https://leetcode.com/problems/single-number-ii/solutions/43294/challenge-me-thx/
# for intuition read comment by "anshumanmishra" in above link.

# when any ele will occur three times then twos and ones wil be '0' for that number.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos= 0, 0
        for num in nums:
            ones= (ones ^ num) & ~twos
            twos= (twos ^ num) & ~ones
        return ones


# if we would have to return the number the single number that appear two and 
# all other appear three times then simply we would have returned 'two' in above logic.


# method 5: other method like finite state machine 
