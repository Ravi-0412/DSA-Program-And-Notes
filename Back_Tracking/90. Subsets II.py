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