# just same logic as 'Three sum'.
# without Recursion: use 'k-2' for loop and one while loop for finding two sum in sorted array.

# But to avoid no of for loops , we did by recursion.
# very better. just change the value of 'k' and target it will work for all given 'k' and any target.
# time: O(n^(k-1)) for both recursive and iterative way.
# here k= 4 so time: O(n^3).

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []

        def kSum(k, start, target, quad):
            # k==2. just apply two sum approach for sorted array avoiding duplicates(Did in Three sum).
            # it is just acting as base action. No return, it will automatically return after while loop.
            if k== 2:
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
            else:
                # just the outermost 'for loop' we apply to get the 'k-sum'.i.e for k=3 we iterate from '0' to 'n-2' from index 'start'.
                # Last two ele we will find using Two sum, so '-k+1'.

                # Any ele from remaining can be next ele
                for i in range(start, len(nums)- k +1):
                    # check if we can take this 'nums[start]' as first element.
                    if i > start and nums[i]== nums[i -1]:
                        # if we take this 'nums[i]' as first element then it will give duplicate.
                        continue
                    kSum(k-1, i+ 1, target- nums[i], quad + [nums[i]])  # added one ele so decrease 'k' by '1' and target by 'nums[i]'. 
                return # after traversing the loop exit i.e simply return to check for next possible ans.

        kSum(4, 0, target, [])   # k=4, starting from index= 0, passing target also since it will keep changing.
                            # 'k' tells how many more ele we need to find starting from index 'start' to make sum = target.
                            # 'start' is just same as outer index of our for loop solution.
        return ans

# Java
"""
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<>();
        kSum(4, 0, (long)target, new ArrayList<>(), nums, ans);
        return ans;
    }
    
    private void kSum(int k, int start, long target, List<Integer> quad, int[] nums, List<List<Integer>> ans) {
        if (k == 2) {
            int l = start, r = nums.length - 1;
            while (l < r) {
                long sum = (long)nums[l] + nums[r];
                if (sum < target) {
                    l++;
                } else if (sum > target) {
                    r--;
                } else {
                    List<Integer> tempQuad = new ArrayList<>(quad);
                    tempQuad.add(nums[l]);
                    tempQuad.add(nums[r]);
                    ans.add(tempQuad);
                    l++;
                    while (l < r && nums[l] == nums[l - 1]) {
                        l++;
                    }
                }
            }
        } else {
            for (int i = start; i < nums.length - k + 1; i++) {
                if (i > start && nums[i] == nums[i - 1]) {
                    continue;
                }
                List<Integer> tempQuad = new ArrayList<>(quad);
                tempQuad.add(nums[i]);
                kSum(k - 1, i + 1, target - nums[i], tempQuad, nums, ans);
            }
        }
    }
}

"""


