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
            # you have to skip all the duplicates of curr ele to avoid duplicate in the ans.
            # Now you can call the function at next distinct ele only.
            while i+1 < len(nums) and nums[i+1]== nums[i]:
                i+= 1
            dfs(i+1, subset)

        dfs(0, [])  
        return res


# Note: Apply same logic in all questions where duplicates are allowed and asking for unique subsets/combinations.
# i.e a) sorting 2) move to distinct number in case of not-take.
# e.g: 1) 40. Combination Sum II


# Java
"""
public class Solution {

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums); // Sort the nums array
        List<List<Integer>> res = new ArrayList<>();

        dfs(0, nums, new ArrayList<>(), res);

        return res;
    }

    private void dfs(int i, int[] nums, List<Integer> subset, List<List<Integer>> res) {
        if (i == nums.length) {
            res.add(new ArrayList<>(subset)); // Add a copy of the subset to the result list
            return;
        }

        subset.add(nums[i]); // Include the current element
        dfs(i + 1, nums, subset, res); // Recursive call with the next index and the updated subset
        subset.remove(subset.size() - 1); // Backtrack

        // Skip duplicates
        while (i + 1 < nums.length && nums[i + 1] == nums[i]) {
            i++;
        }
        dfs(i + 1, nums, subset, res); // Recursive call with the next index and the same subset
    }
}
"""