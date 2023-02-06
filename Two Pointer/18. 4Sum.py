# just same logic as 'Three sum'.
# without Recursion: use 'k-2' for loop and one while loop for finding two sum in sorted array.

# But to avoid no of four loops , we did by recursion.
# very better. just change the value of 'k' it will work for all given 'k'.
# time: O(n^(k-1)) for both recursive and iterative way.
# here k= 4 so time: O(n^3).

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans, quad= [], []

        def kSum(k, start, target):
            if k!= 2:
                # just the outermost for loop we apply to get the k-sum.i.e for k=3 we iterate from '0' to 'n-2'.
                for i in range(start, len(nums)- k +1):
                    # check for duplicates first.
                    if i > start and nums[i]== nums[i -1]:
                        continue
                    quad.append(nums[i])
                    kSum(k-1, i+ 1, target- nums[i])
                    quad.pop()  
                return # after traversing the loop exit i.e simply return to check for next possible ans.

            else: # means k==2. just apply two sum approach for sorted array avoiding duplicates.
                # did in three sum 
                l, r = start, len(nums)-1
                while l < r:
                    if nums[l] + nums[r] < target:
                        l+= 1
                    elif nums[l] + nums[r] > target:
                        r-= 1
                    else:
                        ans.append(quad + [nums[l], nums[r]])
                        l+= 1
                        while l < r and nums[l]== nums[l-1]:
                            l+= 1
        
        kSum(4, 0, target)   # k=4, starting from index= 0, passing target also since it will keep changing.
        return ans

