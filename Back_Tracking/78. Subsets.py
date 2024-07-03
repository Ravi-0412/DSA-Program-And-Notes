# method 1:
# logic: just make the recursion tree by including the first letetr 
# and 'not including' the 1st letter .
# and whenever you will find the given string empty then that will be our one of the subset.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res= []
        
        def dfs(i, subset):   # just backtracking
            if i== len(nums):
                res.append(subset)
                return
            # when you include the curr index ele.
            dfs(i+1, subset + [nums[i]])
            # when you don't include the curr index ele.
            dfs(i+1, subset)

        dfs(0, [])  
        return res

# Method 2 : Using Bit Masking

# n : len(nums)
# every subset is represented by a binary number of 'n' bits.
# VVI: Each bit represents whether the number at that index exists in the subset or not.
# No of subsets = 2^n . Using these 2^n numbers [0,2^n-1], we will try to find the number in that subset.

# For better understanding, go through link in sheet.

# if asked for only non-empty subsets then before adding temp into ans check:
# if len(temp) > 0 then only add.

# Time: O(2^n * n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for num in range(1 << n):
            temp = []
            # add the number whose 'index' bit is set in num
            for i in range(n):
                # if 'i'th bit is set in 'num then nums[i] is part of this subset.
                if (num >> i) & 1:
                    temp.append(nums[i])
            ans.append(temp)
        return ans

# method 3:
# iterative way:

# logic: Accept and reject is happening with 'ans so far'
# for each new number, 
# we can either pick it or not pick it. 
# 1, if pick, just add current number to every existing subset.
# 2, if not pick, just leave all existing subsets as they are.
# We just combine both into our result.

# For example, {1,2,3} intially we have an emtpy set as result [ [ ] ]
# Considering 1, if not use it, still [], if use 1, add it to [ ], so we have [1] now
# Combine them, now we have [ [ ], [1] ] as all possible subset

# Next considering 2, if not use it, we still have [ [ ], [1] ], 
# if use 2, just add 2 to each previous subset, we have [2], [1,2]
# Combine them, now we have [ [ ], [1], [2], [1,2] ]

# Next considering 3, if not use it, we still have [ [ ], [1], [2], [1,2] ], 
# if use 3, just add 3 to each previous subset, we have [ [3], [1,3], [2,3], [1,2,3] ]
# Combine them, now we have [ [ ], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3] ]

# time: O(n*2^n), where 2^n is the total no of subsets and 
# we are copying the number to n subsets each time we encounter a num of the array

# space- O(n*2^n), where 2^n is the total no of subsets and 
# n is the space taken by each subset

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        outer= [[]]   # our final ans will contain list of list
        for num in nums:   # for each number in the array
            n= len(outer) 
            for i in range(n):
                internal= outer[i].copy()  # copy the internal list of outer list one by one
                internal.append(num)       # and append the number to all the existing list
                outer.append(internal)    # and at alst append the internal created list to the outer list
        return outer


# concise way of writing above code:
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         outer= [[]]   # our final ans will contain list of list
#         for num in nums:
#             outer+= [items+ [num] for items in outer]
#         return outer


# Related Q: 
# 1) 90. Subsets II


# Java
"""
// method 1:

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(nums, 0, new ArrayList<>(), res);
        return res;
    }

    private void dfs(int[] nums, int index, List<Integer> subset, List<List<Integer>> res) {
        if (index == nums.length) {
            res.add(new ArrayList<>(subset));  // Make a copy of the current subset
            return;
        }
        
        // Include the current index element
        subset.add(nums[index]);
        dfs(nums, index + 1, subset, res);
        
        // Exclude the current index element
        subset.remove(subset.size() - 1);
        dfs(nums, index + 1, subset, res);
    }
}

// method 2:
public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        int n = nums.length;
        List<List<Integer>> ans = new ArrayList<>();
        
        for (int num = 0; num < (1 << n); num++) {
            List<Integer> temp = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if ((num >> i & 1) == 1) {
                    temp.add(nums[i]);
                }
            }
            ans.add(temp);
        }
        
        return ans;
    }
}

// method 3:
public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> outer = new ArrayList<>();
        outer.add(new ArrayList<>());  // Start with an empty subset

        for (int num : nums) {
            int n = outer.size();
            for (int i = 0; i < n; i++) {
                // Make a copy of the current subset
                List<Integer> internal = new ArrayList<>(outer.get(i));
                // Add the current number to the copied subset
                internal.add(num);
                // Add the new subset to the list of subsets
                outer.add(internal);
            }
        }
        
        return outer;
    }
}

"""