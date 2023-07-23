# method 1:
# 4th method : using dictionary(this i submitted on GFG)
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
# basic meaning: just cancel each other vote.
# it gives the majority ele i.e that has occured more than n/2 times
# by balancing the count i.e after seeing any other element, it 
# decreases the count if count is zero and  'm' is not equal to the current element.
# at alst 'm' will give the majority element

# note: only valid for majority ele if they occur for sure. will not give the ele which has occured maximum no of times
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
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = nums[0]  # Assume majority is 'm'.
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



