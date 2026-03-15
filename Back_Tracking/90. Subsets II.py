# Method 1: 

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
        """
        Thought Process:
        1. Sort to group duplicates.
        2. In the recursion tree:
           - Path A: Include the current element.
           - Path B: Exclude the current element AND all its duplicates.
        This prevents generating the same subset from different instances of the same value.
        """
        nums.sort()
        res = []
        
        def dfs(i, subset):
            # Base Case: Reached the end of the array
            if i == len(nums):
                res.append(list(subset)) # Append a copy
                return
            
            # Decision 1: Include nums[i]
            # Move to the immediate next index
            dfs(i + 1, subset + [nums[i]])
            
            # Decision 2: Exclude nums[i]
            # Skip all identical elements to avoid duplicate branches
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            # Move to the next distinct element
            dfs(i + 1, subset)

        dfs(0, [])
        return res

# Method 2: Using For loop
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Thought Process:
        1. Sort the input to ensure duplicates are adjacent.
        2. Use a for-loop to explore all possible 'next' elements.
        3. Skip duplicates ONLY if they are at the same depth (horizontal) 
           in the recursion tree.
        """
        nums.sort()
        res = []
        
        def backtrack(start, path):
            # Every path reached is a valid subset
            res.append(list(path))
            
            for i in range(start, len(nums)):
                # If nums[i] is same as previous and not the first element 
                # we are considering for this position, skip it.
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                # Move to next index, adding current number to path
                backtrack(i + 1, path + [nums[i]])

        backtrack(0, [])
        return res

# Java Code
"""
import java.util.*;

class Solution {
    List<List<Integer>> res = new ArrayList<>();

    private void dfs(int i, int[] nums, List<Integer> subset) {  
        // Just backtracking
        if (i == nums.length) {
            res.add(new ArrayList<>(subset));
            return;
        }
        // When you include the current index element.
        subset.add(nums[i]);
        dfs(i + 1, nums, subset);
        subset.remove(subset.size() - 1);

        // When you don't include the current index element.
        // You have to skip all the duplicates of the current element to avoid duplicates in the answer.
        // Now you can call the function at the next distinct element only.
        while (i + 1 < nums.length && nums[i + 1] == nums[i]) {
            i++;
        }
        dfs(i + 1, nums, subset);
    }

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums); // Sorting to handle duplicates
        res.clear();
        dfs(0, nums, new ArrayList<>());
        return res;
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> res;

    void dfs(int i, vector<int>& nums, vector<int> subset) {  
        // Just backtracking
        if (i == nums.size()) {
            res.push_back(subset);
            return;
        }
        // When you include the current index element.
        subset.push_back(nums[i]);
        dfs(i + 1, nums, subset);
        subset.pop_back();

        // When you don't include the current index element.
        // You have to skip all the duplicates of the current element to avoid duplicates in the answer.
        // Now you can call the function at the next distinct element only.
        while (i + 1 < nums.size() && nums[i + 1] == nums[i]) {
            i++;
        }
        dfs(i + 1, nums, subset);
    }

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end()); // Sorting to handle duplicates
        res.clear();
        vector<int> subset;
        dfs(0, nums, subset);
        return res;
    }
};
"""

# Extension: 
# Note: Apply same logic in all questions where duplicates are allowed and asking for unique subsets/combinations.
# i.e a) sorting 2) move to distinct number in case of not-take.
# e.g: 1) 40. Combination Sum II


