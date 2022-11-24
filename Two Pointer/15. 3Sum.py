# to avoid duplicates best way i sort the array like we used to do in permutation ans combination problem
# and for every ele apply two sum if its not duplicate
# in when you find and then incr either only start or end pointer to avoid duplicates in the ans
# time: O(n^2)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans, n= [],len(nums)
        for i in range(n-2):
            if i>0 and nums[i]== nums[i-1]:   # simply skip so that no duplicate come in the ans
                continue
            start, end= i+1, n-1
            while start< end:
                threeSum= nums[i] + nums[start] + nums[end]
                if threeSum>0:
                    end-= 1
                elif threeSum <0:
                    start+= 1
                else:
                    ans.append([nums[i],nums[start], nums[end]])
                    # in this case there can be duplicates after 'start' pointer and before right pointer which may lead to duplicate if they form total= 0
                    # so either incr 'start' to new ele or decr 'end' to new element. No need to move both other move will be done by above two loop
                    start+= 1
                    while start < end and nums[start]== nums[start-1]:
                        start+= 1
        return ans


# better ans more understandable way
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    # check for duplicates and move both to next distinct ele
                    while l < r and nums[l] == nums[l+1]:  # move to next distinct ele
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l+= 1
                    r-= 1
        return res