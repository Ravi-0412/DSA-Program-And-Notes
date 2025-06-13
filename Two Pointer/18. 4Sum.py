# Method 1 : 

# just same logic as 'Three sum' 
# without Recursion: use 'k-2' for loop and one while loop for finding two sum in sorted array.

# But to avoid no of for loops , we did by recursion.
# very better. just change the value of 'k' and target it will work for all given 'k' and any target.
# time: O(n^(k-1)) for both recursive and iterative way.
# here k= 4 so time: O(n^3).
# sapce: O(1), after neglacting recursion depth

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
import java.util.*;

class Solution {
    List<List<Integer>> ans;

    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        ans = new ArrayList<>();
        kSum(nums, 4, 0, target, new ArrayList<>());
        return ans;
    }

    void kSum(int[] nums, int k, int start, long target, List<Integer> quad) {
        // k==2. just apply two sum approach for sorted array avoiding duplicates(Did in Three sum).
        // it is just acting as base action. No return, it will automatically return after while loop.
        if (k == 2) {
            int l = start, r = nums.length - 1;
            while (l < r) {
                long sum = nums[l] + nums[r];
                if (sum < target) {
                    l++;
                } else if (sum > target) {
                    r--;
                } else {
                    List<Integer> temp = new ArrayList<>(quad);
                    temp.add(nums[l]);
                    temp.add(nums[r]);
                    ans.add(temp);
                    l++;
                    while (l < r && nums[l] == nums[l - 1]) {
                        l++;
                    }
                }
            }
        } else {
            // just the outermost 'for loop' we apply to get the 'k-sum'. i.e for k=3 we iterate from '0' to 'n-2' from index 'start'.
            // Last two ele we will find using Two sum, so '-k+1'.

            // Any ele from remaining can be next ele
            for (int i = start; i <= nums.length - k; i++) {
                // check if we can take this 'nums[start]' as first element.
                if (i > start && nums[i] == nums[i - 1]) {
                    // if we take this 'nums[i]' as first element then it will give duplicate.
                    continue;
                }
                List<Integer> newQuad = new ArrayList<>(quad);
                newQuad.add(nums[i]);
                kSum(nums, k - 1, i + 1, target - nums[i], newQuad);  // added one ele so decrease 'k' by '1' and target by 'nums[i]'. 
            }
        }
    }
}
"""


# C++
"""
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
    vector<vector<int>> ans;

public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        kSum(nums, 4, 0, (long long)target, {});
        return ans;
    }

    void kSum(vector<int>& nums, int k, int start, long long target, vector<int> quad) {
        // k==2. just apply two sum approach for sorted array avoiding duplicates(Did in Three sum).
        // it is just acting as base action. No return, it will automatically return after while loop.
        if (k == 2) {
            int l = start, r = nums.size() - 1;
            while (l < r) {
                long long sum = (long long)nums[l] + nums[r];
                if (sum < target) {
                    l++;
                } else if (sum > target) {
                    r--;
                } else {
                    vector<int> temp = quad;
                    temp.push_back(nums[l]);
                    temp.push_back(nums[r]);
                    ans.push_back(temp);
                    l++;
                    while (l < r && nums[l] == nums[l - 1]) {
                        l++;
                    }
                }
            }
        } else {
            // just the outermost 'for loop' we apply to get the 'k-sum'. i.e for k=3 we iterate from '0' to 'n-2' from index 'start'.
            // Last two ele we will find using Two sum, so '-k+1'.

            // Any ele from remaining can be next ele
            for (int i = start; i <= nums.size() - k; i++) {
                // check if we can take this 'nums[start]' as first element.
                if (i > start && nums[i] == nums[i - 1]) {
                    // if we take this 'nums[i]' as first element then it will give duplicate.
                    continue;
                }
                vector<int> newQuad = quad;
                newQuad.push_back(nums[i]);
                kSum(nums, k - 1, i + 1, target - nums[i], newQuad);  // added one ele so decrease 'k' by '1' and target by 'nums[i]'. 
            }
        }
    }
};
"""