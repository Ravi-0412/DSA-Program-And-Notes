# more clarity for Q: if all numbers in the array is negative then return smallest poitsive i.e '1'.
# if all number in range are present then return the greatest of all number beyond array i.e maxNo +1 


# method 1:
# logic: first find the range of number i.e min no in arr and max no in array.
# now check for positive number which is not present in the array.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minNo, maxNo = min(nums), max(nums)
        if maxNo <= 0:  # all number in array is negative
            return 1
        numSet= set(nums)   # to check whether a num is present or not in O(1).
        for num in range(1, maxNo):
            if num not in numSet: 
                return num
        # means all no in range are present.
        return maxNo + 1

# method 2:
# in c++ its working in python not working.
class Solution {
public: 
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size(); 
        for (int i = 0; i < n; i++)
            while (nums[i] > 0 && nums[i] <= n && nums[nums[i] - 1] != nums[i])
                swap(nums[i], nums[nums[i] - 1]);
        for (int i = 0; i < n; i++)
            if (nums[i] != i + 1)
                return i + 1;
        return n + 1;
    }
};


# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         n= len(nums)
#         for i in range(n):
#             while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
#                 nums[i], nums[nums[i] -1]= nums[nums[i] -1], nums[i]
        
#         for i in range(n):
#             if nums[i]!= i+1:
#                 return i +1
#         return n + 1