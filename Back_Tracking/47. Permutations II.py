# here we are checking with pre number and in 'subset' we were chekcing with next number till we find any distinct number.

# Here first time simply add because that will be a valid a permutation only but for next time after removing that ele.
# we can't add directly we will get duplicate since pre number can also be same and we add next number beside the pre num,
# we will get duplicate.

# This is the difference between 'subset and permutation'.

# So before adding any number we are checking if pre number was same, if was same then don't add that number.

# Method 1: 
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans= []
        self.dfs(nums,[],ans)
        return ans
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return 
        for i in range(len(nums)):
            if i > 0 and nums[i]== nums[i-1]:  # i> 0: to add the number simply first time without checking and to avoid out of bound 'i-1'.
                continue
            # using 'while' is logically correct but if 'i' reaches to len(nums) then, automatically dfs will be called 
            # and will give error index out of bound(nums[i]).
            # But if we use if with continue then in this case, it will first go to for loop and if i== len(nums) then 
            # it will automatically come out of 'for' loop and dfs will not be called and we will not get any error.

            # while i >0 and i< len(nums) and nums[i]== nums[i-1]:  
            #     i+= 1                              

            # add nums[i] in the path and skip nums[i] from the original array.
            self.dfs(nums[:i] + nums[i+1: ], path + [nums[i]], res)


# Method 2:
# Exact similar as 'method 2' of first part i.e Q :"46.Permutations". Just slight change

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # To avoid duplicates
        def permutation(per):
            if len(per) == len(nums):
                ans.append(per)
                return
            for i in range(len(nums)):
                # Skip used elements or duplicate elements (only the first occurrence can be used)
                if i in included or (i > 0 and nums[i] == nums[i -1] and (i-1) not in included):
                    # 1) if current ele is already used or 
                    # 2) previous ele you have skipped and you want to use current ele
                    # having same value as previous so it will lead to duplicate.
                    # Because we only get duplicate while skipping.
                    continue
                # if prev ele is used or current ele is not used then we can take this ele
                # take this element.
                included.add(i) 
                permutation(per + [nums[i]])
                # while backtracking remove i
                included.remove(i) 

        n = len(nums)   
        ans = []
        included = set()
        permutation([])
        

# Java
"""
// method 2:
class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums); // Sort the array to avoid duplicates
        List<List<Integer>> ans = new ArrayList<>();
        Set<Integer> included = new HashSet<>();
        permutation(new ArrayList<>(), ans, nums, included);
        return ans;
    }

    private void permutation(List<Integer> per, List<List<Integer>> ans, int[] nums, Set<Integer> included) {
        // Base case: if the current permutation has the same length as the input array
        if (per.size() == nums.length) {
            ans.add(new ArrayList<>(per)); // Add the completed permutation to the result list
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            // Skip used elements or duplicate elements (only the first occurrence can be used)
            if (included.contains(i) || (i > 0 && nums[i] == nums[i - 1] && !included.contains(i - 1))) {
                continue;
            }

            // Mark the element as used
            included.add(i);
            per.add(nums[i]); // Add the element to the current permutation

            // Recurse with the updated state
            permutation(per, ans, nums, included);

            // Backtrack: remove the last added element and mark it as unused
            per.remove(per.size() - 1);
            included.remove(i);
        }
    }
}

"""