# 1st method: time o(n),space o(n) 

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        temp,n= nums.copy(), len(nums)
        k= k%n
        for i in range(n):
            nums[(i+k)%n]= temp[i]
        return nums

# 2nd method: very concise one
# Observation: ans = last k ele + first 'n-k' ele
# time= space= O(n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n= len(nums)
        k= k%n
        # print(nums[(n-k):] + nums[:(n-k)])  # will print correct one only but at return time it will return the original array only 
        # return nums[(n-k):] + nums[:(n-k)]   # this one will return the original array only, because this is not changing the values in original array

        # correct one
        # nums[:]= nums[(n-k):] + nums[:(n-k)]  # or use negative slicing 
        nums[:] = nums[-k:] + nums[:-k]   # better one
        
         # nums[:]= nums[-k:] + nums[:n-k]  # this will give incorrect ans in case of one ele and k=0, it will just add that array two times
        return nums

# Note:
# 1) nums[:] = nums[n-k:] + nums[:n-k] 
# 2) nums = nums[n-k:] + nums[:n-k]
# The 1st one can truly change the value of old nums
# but the following one(2nd one) just changes its reference to a new nums not the value of old nums. 
# it just create a copy of 'nums' and changes the value inside the copied list


# 3rd method: optimising the space complexity to O(1) for right rotation
# logic: 1)Reverse the last 'k' elements.. Q given reverse right so reverse the last 'k' elements
# 2) Reverse the remaining ele 'n-k' element from start 
# 3) and finally reverse the whole array 
# Time: o(n),space: o(1)


# for left rotation : 
# logic: 1)Reverse the first 'k' elements..Q given reverse left so reverse the first 'k' elements
# 2) Reverse the remaining ele 'n-k' from last i.e from index 'k+1' to 'n-1'
# 3) and finally reverse the whole array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n= len(nums)   
        k=k%n
        def reverse(a,l,h):
            i,j=l,h
            while(i<j):
                nums[i],nums[j]= nums[j],nums[i]
                i+= 1
                j-= 1
            
        reverse(nums,n-k,n-1)   # last 'k' elements
        reverse(nums,0,n-k-1)   # remaining 'n-k' ele from start
        reverse(nums,0,n-1)
