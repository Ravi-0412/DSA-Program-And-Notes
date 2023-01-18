# logic already done in subset Q:78  at last
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans= [[]]
        end= 0
        nums.sort()
        for i in range(len(nums)):
            start= 0   # automatically we will copy from index '0' only but in case of duplicates start will change to end+1
            # checking for duplicates item
            if i>0 and nums[i-1]== nums[i]:
                start= end + 1    # newly created array in pre step will start from here only
            end= len(ans)-1
            for j in range(start,len(ans)):
                inner= ans[j].copy()
                inner.append(nums[i])
                ans.append(inner)
        return ans


# recursive way: way better and logical
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res= []
        
        def dfs(i, subset):   # just backtracking
            if i== len(nums):
                res.append(subset)
                return
            # when you include the curr index ele.
            dfs(i+1, subset + [nums[i]])
            # when you don't include the curr index ele. But when you don't include the curr index,
            # you have to skip all the duplicates of curr ele to avoid duplicate in the ans.
            while i+1 < len(nums) and nums[i+1]== nums[i]:
                i+= 1
            dfs(i+1, subset)

        dfs(0, [])  
        return res
