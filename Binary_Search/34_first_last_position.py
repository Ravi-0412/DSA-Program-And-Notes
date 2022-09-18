# # same logic as we did for finding all the position of target 
# # in case of repeated elements
# # here worst case, time complexity may go: o(n) as while loop after
# # finding mid can go upto n
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         n= len(nums)
#         low= 0
#         high= n-1
#         index= 0
#         temp= 0
#         while(low<= high):
#             mid= int(low+ (high- low)/2)
#             if nums[mid]== target: 
#                 index= mid
#                 temp=1
#                 break
#             elif nums[mid]< target: 
#                 low= mid+ 1
#             else:
#                 high= mid-1
#         # middle index may not be the 1st position of taregt ele
#         if temp==0:  # it means element is not present
#             return [-1,-1]
#         else:
#             start= index-1
#             # for finding the target ele on left side of middle index
#             while(start>=0 and nums[start]==target):
#                 start-= 1
#             end= index+ 1
#             # for finding the target ele on right side of middle index
#             while(end<= n-1 and nums[end]== target):
#                 end+= 1
#             # when above two while loop will fail means till pre value
#             # of start and end target ele was there
#             return [start+1, end-1]



# 2nd method: Best one
# Time: o(logn), space:o(1)   
def search(nums,target,findStartIndex):
    ans= -1
    start= 0
    end= len(nums)-1
    while(start<= end):
        mid= start+ (end-start)//2
        if nums[mid]> target:
            end= mid-1
        elif nums[mid]< target:
            start= mid+1
        else:
            # potential ans has been found means
            # the target ele exist now we have to find 
            # its first and last index
            ans= mid  # updating the ans since we have got the target ele
            if(findStartIndex==1):  # this will execute to find the first position
                end= mid-1  # since we are finding the first index so we are updating
                            # the 'end' keeping 'start' constant because we have to find on left side of mid
            else:
                start= mid+1       # this will execute to find the last position
                                # since we are finding the last index so we are updating
                            # the 'start' keeping 'end' constant because we have to find on right side of the mid
    return ans  # will return first or last index depending upon 
                # the third parameter 'findStartIndex'
def searchRange(nums, target):
    ans= [-1,-1]  # initialising the result , nothing target will not be 
                  # there then it will retrun this only
    ans[0]= search(nums,target, 1) # will give the first position of target ele
    ans[1]= search(nums,target, 0)  # will give the last position of target ele
    return ans

nums= [5,7,7,8,8,10]
print(searchRange(nums,8))
print(searchRange(nums,6))
nums1= []
print(searchRange(nums1,0))



# # method 2: submitted on leetcode
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         ans= [-1,-1]
#         start= self.search(nums,target, 1)  # was missing 'self' before search
#                                             # and due to this was getting error again and again
#         end=   self.search(nums,target, 0)       
#         ans[0]= start
#         ans[1]= end
#         return ans
    
#     def search(self,nums,target,findStartIndex):
          # if findStartIndex== 1, it means we are finding the first position if '0' means we are finding the last position
#         ans= -1
#         start= 0
#         end= len(nums)-1
#         while(start<= end):
#             mid= start+ (end-start)//2
#             if nums[mid]> target:
#                 end= mid-1
#             elif nums[mid]< target:
#                 start= mid+1
#             else:
#                 # potential ans has been found
#                 ans= mid
#                 if(findStartIndex==1):
#                     end= mid-1
#                 else:
#                     start= mid+1
#         return ans
