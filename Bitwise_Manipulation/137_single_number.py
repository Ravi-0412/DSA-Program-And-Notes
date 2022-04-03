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

time: O(n), space: O(n)

class Solution:
    def singleElement(self,arr, N):
        return int((3*sum(set(arr))-sum(arr))/2)


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

# method 4: needs a lot of thinking but better method
# using bit manipulation
#submitted on leetcode(didn't do myself)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones,twos= 0,0
        # ones stores the count of ele occuring  one time at any current time
        # two stores the count of ele occuring two time at any current time
        
        # first check if ele is occuring two times
        # if occuring for 2nd time,set 'twos' to 'num' itself and reset 'ones' to 0
        # if occuring for third times then twos and ones will be num itself
                
        # and if any no has occured three times, make both 'twos' and 'ones' equal to zero at last
        for num in nums:
            twos= twos|(ones & num)    # & will check whether it has already occured
                                      # for 1st time and if true then '|' will set twos to 1
                                    
            # if it is not true,means occuring for 1st time then set ones to the current no 
            # to check in twos in next iteration(here we cant use '|' as it will give only '1' or '0')
            # but we need no itself at 1st time(for returning) and 2nd time we have to make ones =0
            ones= ones^num
            
            # now check if no has occured  three times or not
            # if no has already occured three times then val of both twos and ones will be equal to num            
            non_three= ~(ones & twos) # will give true if 'num' has not occured for three times
                                    # means we have to maek it zero if ele has occured three times(means twos=1,ones=1)
                                    # otherwise make it equal to 1(num)  in all other cases
                                    # so only 'NAND' can do this operation like first check if something
                        # is common bw ones and twos, if common negate it to make it false
                        #otherwise make it true
            
            # now update the value of ones and twos both to zero if ele has occured three times
            # otherwise keep the same, for this we have to use '&' with non_three
            ones= ones & non_three
            twos= twos & non_three
            
        # now return ones 
        return ones

# in comment 'num' means = 1 only 


# general method for above approaches
for (int i : nums) {
    xm ^= (xm-1 & ... & x1 & i);
    xm-1 ^= (xm-2 & ... & x1 & i);
    .....
    x1 ^= i;
    
    mask = ~(y1 & y2 & ... & ym) where yj = xj if kj = 1, and yj = ~xj if kj = 0 (j = 1 to m).    # mask here means like 'non_three' and all

    xm &= mask;
    ......
    x1 &= mask;
}


# method 5:
