# here we are checking with pre number and in 'subset' we were chekcing with next number till we find any distinct number.

# Here first time simply add because that will be a valid a permutation only but for next time after removing that ele.
# we can't add directly we will get duplicate since pre number can also be same and we add next number beside the pre num,
# we will get duplicate.

# This is the difference between 'subset and permutation'.

# So before adding any number we are checking if pre number was same, if was same then don't add that number.

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans= []
        self.dfs(nums,[],ans)
        return ans
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return 
        for i in range(len(nums)):
            if i >0 and nums[i]== nums[i-1]:  # i> 0: to add the number simply first time without checking and to avoid out of bound 'i-1'.
                continue
            # using 'while' is logically correct but if 'i' reaches to len(nums) then, automatically dfs will be called 
            # and will give error index out of bound(nums[i]).
            # But if we use if with continue then in this case, it will first go to for loop and if i== len(nums) then 
            # it will automatically come out of 'for' loop and dfs will not be called and we will not get any error.

            # while i >0 and i< len(nums) and nums[i]== nums[i-1]:  
            #     i+= 1                              

            # add nums[i] in the path and skip nums[i] from the original array.
            self.dfs(nums[:i] + nums[i+1: ], path + [nums[i]], res)