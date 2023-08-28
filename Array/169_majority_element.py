# Note vvi: There can be exactly one majority ele.

# method 1:
# using dictionary(this i submitted on GFG)
class Solution:
    def majorityElement(self, A, N):
        middle_index= N//2
        hashmap={}
        for i in A:
            if i not in hashmap:  # searches for 'i' in keys of dictionary
                                  # not in values
                hashmap[i]= 1
            else:
                hashmap[i]+=1
        for key,value in hashmap.items():
            if value>middle_index:
                return key
        return -1

# Method 2: 

# if given majority elements always exist and array is sorted
# in this case middle index must be the index of majority element
# in this case, time: O(1), just return the middle ele 

# but here we are sorting then returning the mid ele so, time: 0(nlogn)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


# Method 3: Better one and Q is based on this only.

# Algo: (Moore’s Voting Algorithm)
# Just you have to find the winner on election.(No chance of draw)

# basic meaning: just cancel each other vote.
# it gives the majority ele i.e that has occured more than n/2 times
# by balancing the count i.e after seeing any other element, it 
# decreases the count if count is zero and  'm' is not equal to the current element.
# at alst 'm' will give the majority element

# note vvi: only valid for majority ele if they occur for sure. will not give the ele which has occured maximum no of times
# if the max_fre ele occur at the start then count will get decrement to '0' later and 'm' will have different ele at last
# then will give incorrect ans 

# Time: O(n) , space : O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n= len(nums)
        cnt=0
        m= None     # m storing elements with maximum frequency ele till any index
        for i in range(n):
            if cnt==0:  # only update the m when count= 0 because if count!= 0 then it means m is the most occuring ele till that index
                m= nums[i]  
                cnt+= 1
            else:
                if nums[i] == m:  # if m and array ele is same then increase the count by 1 
                    cnt+= 1
                else:  # else decrease the count by 1
                    cnt-= 1
        return m


# Another way of writing the same logic
# More logical

# Har ele ke passs 2 choice : 
# i) majority ele h. 
# is case me count ko bs increment karna h.
# ii) majority ele nhi h.
# is case me count ko decrease karna h and agar count == 0 ho gya decrease karne ke bad
# Then, majority ele ko update kar dena h current ele se and count = 1 kar dena h.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = nums[0]  # Assume majority is nums[0]
        count = 1   # nums[0]
        for i in range(1, len(nums)):
            if nums[i] == m:
                count += 1
            else:
                count -= 1
                if count == 0:
                    m = nums[i]
                    count = 1
        return m


# Another way of writing the above code
# on this approach, we can solve the Q :"229. Majority Element II".

# Just relate to real life counting of votes in ele i.e how a condidate wins.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = None  
        count = 0   
        for n in nums:
            if n == m:
                # vote of majority ele will increase.
                count += 1
            elif count == 0:
                # cur ele will become majority ele (current winning condidate)
                m , count = n, 1
            else:  # count > 0
                # cur ele can't be the winning condidate, it will just reduce the vote of cur winning condidate i.e cur majority ele
                count -= 1
        return m