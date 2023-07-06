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

# method 4 vvi: find the sum of set bits at all the positions and divide by 3
# if sum of set bits at that position is not divisible by 3 then it means the single number has set bit at that position.
# time: O(32* n)

# Note vvi: This method will work only for positive number in case of python.
# Detailed explanation in notes, page : 137

def singleNumber(self, nums: List[int]) -> int:
        ans= 0
        for i in range(32): # since max bits in any number can be 32
            check_set= 1<< i   # to check whether ith bit of that num is set bit or not so took left shift of 1 'i' times
            no_set_bits = 0      
            for num in nums:
                if num & check_set:  # if 1 then 
                    no_set_bits += 1    # add to the set_bit
            # now check whether sum of set bits at that position is divisible by 3 or not
            if no_set_bits %3!= 0:      
                # update the ans
                ans= ans | check_set   # put '1' at ith position in the ans keeping other bit same in ans.
        return ans


# Method 4.1 : Same above method that will work in case of both negative and positive numbers.
# Analyse this properly 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans= 0
        for i in range(32): # since max bits in any number can be 32
            check_set= 1<< i   # to check whether ith bit of that num is set bit or not so took left shift of 1 'i' times
            no_set_bits = 0      
            for num in nums:
                if num & check_set !=0:  # if 1 then 
                    no_set_bits += 1    # add to the set_bit
            # now check whether sum of set bits at that position is divisible by 3 or not
            if no_set_bits %3 == 1:      
                # update the ans
                ans= ans | check_set   # put '1' at ith position in the ans keeping other bit zero
        # print(ans, ~ans + 1 , (~ans + 1) & 0xffffffff)
        # print(0xffffffff)
        isPositive = (ans >> 31)  & 1 == 0
        return ans if isPositive else -((~ans + 1) & 0xffffffff)

# method 4.2: 
# Better & easier one than 4.1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans= 0
        for i in range(32): # since max bits in any number can be 32
            check_set= 1<< i   # to check whether ith bit of that num is set bit or not so took left shift of 1 'i' times
            no_set_bits = 0      
            for num in nums:
                if num & check_set !=0:  # if 1 then 
                    no_set_bits += 1    # add to the set_bit
            # now check whether sum of set bits at that position is divisible by 3 or not
            if no_set_bits %3 == 1:      
                # update the ans
                ans= ans | check_set   # put '1' at ith position in the ans keeping other bit zero
        if ans <= 2**31 - 1:  # in 2's complement notation, +ve number can have value representation till 2**(n-1) -1.
            # Means ans is +ve number then only we can get ans less than this
            return ans
        # if negative then just find the positive value and return with '-ve' sign to get the actual number.
        return -(2**32 - ans)

# method 5 vvi: needs a lot of thinking but better method

# This Q was made for checking this method only.
# time: O(n)

# logic:  Page no: 141

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


# java version
# method 3

# class Solution {
#     public int singleNumber(int[] nums) {
        
#         int ans= 0;
#         for(int i= 0; i <32; i++) 
#         {
#             int count = 0;
#             for(int num : nums) 
#             {
#                 if(((num >>i) & 1) == 1 ){
#                     count += 1;
#                     }
#             }
#             if(count % 3 != 0)
#                 ans = ans |(1<<i);
#         }
#         return ans;
#     }
# }