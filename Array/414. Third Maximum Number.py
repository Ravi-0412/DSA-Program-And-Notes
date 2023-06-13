# method 1: sort and check from last and count the distinct number you have seen till now.
# time: O(n*logn)

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = len(nums)
        if n <=2:
            return max(nums)
        nums.sort()
        count= 1
        for i in range(n-1, 0, -1):
            if nums[i]  != nums[i-1]:
                count += 1
                if count == 3:
                    return nums[i-1]
        return max(nums)
    

# method 2:
# logic: keep track of first_max, 2nd_max, 3rd_max after you each ele you see.
# time: O(3* n)
class Solution(object):
    def thirdMax(self, nums):
        v = [float('-inf'), float('-inf'), float('-inf')]   # [first_max, second_max, third_max]
        for num in nums:
            if num not in v:
                if num > v[0]:   v = [num, v[0], v[1]]  # make first= num, second= pre_first, third= pre_2nd
                elif num > v[1]: v = [v[0], num, v[1]]  # keep first same, make  second= num &  third= pre_2nd
                elif num > v[2]: v = [v[0], v[1], num]  # keep first & second same, & make third= num
        # return max(nums) if float('-inf') in v else v[2]
        return v[2] if v[2] != float('-inf') else v[0]