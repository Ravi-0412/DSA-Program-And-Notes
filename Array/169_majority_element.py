# o(n^2) : 1st method
# just count the occurences of each element

import math
n= int(input("enter the value of n \n"))
lst= []
for i in range(n):
    x=int(input("enter the number \n"))
    lst.append(x)
print(lst)
middle= math.floor(n/2)
def majority_element():
    j=0  # 'j-1' will give the index of majority element
    for i in range(n):
        flag=0
        j+=1  
        fre= lst.count(lst[i])
        if fre>middle:
            flag=1
            break
    if(flag==1):
        print("majority element is: ",lst[j-1] )
    else:
        print('no majority element exist')

majority_element()


# Leetcode solution: 2nd method(Moore’s Voting Algorithm): 
# basic meaning: just cancel each other vote.
# it gives the majority ele i.e that has occured more than n/2 times
# by balancing the count i.e after seeing any other element, it 
# decreases the count if count is zero and  'm' is not equal to the current element.
# at alst 'm' will give the majority element



# note: only valid for majority ele if they occur for sure. will not give the ele which has occured maximum no of times
# if the max_fre ele occur at the start then count will get decrement to '0' later and 'm' will have different ele at last
# then will give incorrect ans 
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n= len(nums)
        middle= math.floor(n/2)
        cnt=0
        m= None     # m storing elements with maximum frequency ele till any index
        for i in range(n):
            if cnt==0:  # only update the m when count= 0 because if count!= 0 then it means m is the most occuring ele till that index
                m= nums[i]  
                cnt+= 1
            else:
                if m==nums[i]:  # if m and array ele is same then increase the count by 1 
                    cnt+= 1
                else:  # else decrease the count by 1
                    cnt-= 1
        return m
                    


# if given majority elements always exist and array is sorted
# in this case middle index must be the index of majority element
# in this case, time: O(1), just return the middle ele 

# but here we are sorting then returning the mid ele so, time: 0(nlogn)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]



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


