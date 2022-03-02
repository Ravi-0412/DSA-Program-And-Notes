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


# Leetcode solution: 2nd method(Moore’s Voting Algorithm)
# it just give the element that has occured most no of times(not the total frequency of that element )
# by balancing the count i.e after seeing any other element it 
# decreases the count if count is zero and  'm' is
# not equal to the current element
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n= len(nums)
        middle= math.floor(n/2)
        cnt=0
        global m      # m storing elements with maximum frequency
        for i in range(n):
            if cnt==0:
                m= nums[i]  
                cnt+= 1
            else:
                if m==nums[i]:
                    cnt+= 1
                else:
                    cnt-= 1
# now check the no of occurences of the elemnet that has occured most no of times
# if greater than middle then 'm' is majority element
# else no majority element exist
        x= nums.count(m)
        if x> middle:
            return m
                    


# leetcode 3rd method(if given majority elements always exist)
# in this case middle index must be the index of majority element
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


