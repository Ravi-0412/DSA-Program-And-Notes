# Logic: to avoid duplicates , 1)we will have to bring all the duplicates together so that we can easily check for duplicates,
# and best way to bring same ele together is just sort the array.
# 2) For avoiding we can include the first element either 'i' or 'j' or 'k' but 
# for other element we will have to check to skip if previous element is same.

# Method1: Brute Force
# Just check all the possibility

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n - 2):
            # if not 1st element then skip otherwise it will lead to duplicate.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 1):
                # if not 1st element for cur 'i' then skip otherwise it will lead to duplicate.
                if j > i + 1 and nums[j] == nums[j -1]:
                    continue
                for k in range(j + 1, n):
                    # if not 1st element for cur 'j' then skip otherwise it will lead to duplicate.
                    if k > j + 1 and nums[k] == nums[k -1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        ans.append([nums[i], nums[j], nums[k]])
        return ans

# Method 2: Optimise using Two sum.
# and for every ele apply two sum if its not duplicate. and since sorted so we can use two pointer approach for Two sum.

# Note: Since only number is mattering in ans (not index) , we can sort array.
# If index were asked to return then we can't sort.

# note: in case if we find any ans then before updating start or end  pointer ,we will check for duplicates 
# because if we simply incr both then it can lead to duplicate ans.
# No need to check in unequal case.

# Also in outer loop, we will only apply "two sum" for cur number if it is distinct only.

# time: O(n^2)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans, n= [],len(nums)
        for i in range(n-2):
            # check if we can take this 'nums[i]' as first element.
            if i>0 and nums[i]== nums[i-1]:   # simply skip so that no duplicate come in the ans
                # if we take this 'nums[i]' as first element then it will give duplicate
                continue
            start, end= i+1, n-1  # check for 'Two sum' in remaining array ahead.
            while start < end:
                threeSum= nums[i] + nums[start] + nums[end]
                if threeSum > 0:
                    end -= 1
                elif threeSum < 0:
                    start += 1
                else:  # means we have found one of the ans.
                    ans.append([nums[i],nums[start], nums[end]])
                    # in this case there can be duplicates after 'start' pointer and before right pointer, 
                    # which may lead to duplicate if they form total= 0
                    # so either incr 'start' to new ele or decr 'end' to new element. No need to move both otherwise we may miss some answers.
                    start += 1
                    # checking for duplicates
                    while start < end and nums[start]== nums[start-1]:
                        start+= 1
        return ans


# Note: Jahan bhi distinct ka bat ho sorting ka ek bar jaroor socho.

# Similar Q: 
# 1) 18. 4Sum
# 2) Count the triplets



# java
"""

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<>();
        int n = nums.length;
        for (int i = 0; i < n - 2; i++) {
            // Check if we can take this 'nums[i]' as the first element.
            if (i > 0 && nums[i] == nums[i - 1]) {
                // Simply skip so that no duplicates come in the answer
                // If we take this 'nums[i]' as the first element, then it will give a duplicate
                continue;
            }
            int start = i + 1, end = n - 1;  // Check for 'Two sum' in the remaining array ahead.
            while (start < end) {
                int threeSum = nums[i] + nums[start] + nums[end];
                if (threeSum > 0) {
                    end--;
                } else if (threeSum < 0) {
                    start++;
                } else {  // Means we have found one of the answers.
                    ans.add(Arrays.asList(nums[i], nums[start], nums[end]));
                    // In this case, there can be duplicates after 'start' pointer and before the right pointer,
                    // which may lead to duplicates if they form total = 0.
                    // So either increase 'start' to a new element or decrease 'end' to a new element.
                    // No need to move both, otherwise, we may miss some answers.
                    start++;
                    // Checking for duplicates
                    while (start < end && nums[start] == nums[start - 1]) {
                        start++;
                    }
                }
            }
        }
        return ans;
    }
}

"""