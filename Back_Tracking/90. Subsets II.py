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


# recursive way: way better and logical.
# logic: All the duplicates must come to same subset, must not go to different subset otherwise we will get duplicate subset in the ans.
# for checking duplicates array must be sorted.

# while adding the curr ele into ans, we will not get the duplicate but we don't want to include that ele then we may get duplicate.
# like [1,2,1]: if we add first '1' and exclude second '1' (including '2' in both) then we will get duplictae [1,2] (two times).
# for for checking duplicates array must be sorted to find the duplicate num easily.

# And when we don't want to include the curr ele then we have to skip all the next duplicate also.
# so using while loop till we find any distinct ele.

# other everything is just same as subset Q.
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
            # when you don't include the curr index ele.
            #  But when you don't include the curr index,
            # you have to skip all the duplicates of curr ele to avoid duplicate in the ans.
            # Now you can call the function at next distinct ele only.
            while i+1 < len(nums) and nums[i+1]== nums[i]:
                i+= 1
            dfs(i+1, subset)

        dfs(0, [])  
        return res


