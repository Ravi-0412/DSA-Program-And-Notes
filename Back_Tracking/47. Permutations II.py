# Method 1: 

# here we are checking with pre number and in 'subset' we were chekcing with next number till we find any distinct number.

# Here first time simply add because that will be a valid a permutation only but for next time after removing that ele.
# we can't add directly we will get duplicate since pre number can also be same and we add next number beside the pre num,
# we will get duplicate.

# This is the difference between 'subset and permutation'.

# So before adding any number we are checking if pre number was same, if was same then don't add that number.

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
//Method 1
import java.util.*;

class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums); // To avoid duplicates
        List<List<Integer>> res = new ArrayList<>();
        dfs(nums, new ArrayList<>(), res);
        return res;
    }

    private void dfs(int[] nums, List<Integer> path, List<List<Integer>> res) {
        if (nums.length == 0) {
            res.add(new ArrayList<>(path));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1])  
                // i > 0: to add the number simply first time without checking and to avoid out of bound 'i-1'.
                continue;

            // using 'while' is logically correct but if 'i' reaches to len(nums), then automatically dfs will be called
            // and will give error index out of bound (nums[i]).
            // But if we use if with continue, then in this case, it will first go to for loop and if i == len(nums), 
            // it will automatically come out of 'for' loop and dfs will not be called and we will not get any error.

            // add nums[i] in the path and skip nums[i] from the original array.
            int[] newNums = new int[nums.length - 1];
            for (int j = 0, k = 0; j < nums.length; j++) {
                if (j != i) newNums[k++] = nums[j];
            }
            List<Integer> newPath = new ArrayList<>(path);
            newPath.add(nums[i]);
            dfs(newNums, newPath, res);
        }
    }
}

//Method 2
import java.util.*;

class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums); // To avoid duplicates
        List<List<Integer>> ans = new ArrayList<>();
        Set<Integer> included = new HashSet<>();
        permutation(nums, new ArrayList<>(), ans, included);
        return ans;
    }

    private void permutation(int[] nums, List<Integer> per, List<List<Integer>> ans, Set<Integer> included) {
        if (per.size() == nums.length) {
            ans.add(new ArrayList<>(per));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            // Skip used elements or duplicate elements (only the first occurrence can be used)
            if (included.contains(i) || (i > 0 && nums[i] == nums[i - 1] && !included.contains(i - 1))) {
                // 1) if current ele is already used or 
                // 2) previous ele you have skipped and you want to use current ele
                // having same value as previous so it will lead to duplicate.
                // Because we only get duplicate while skipping.
                continue;
            }

            // If prev ele is used or current ele is not used, then we can take this ele.
            // Take this element.
            included.add(i);
            per.add(nums[i]);
            permutation(nums, per, ans, included);
            // while backtracking remove i
            included.remove(i);
            per.remove(per.size() - 1);
        }
    }
}

"""

# C++ Code 
"""
//Method 1
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    void dfs(vector<int> nums, vector<int> path, vector<vector<int>>& res) {
        if (nums.empty()) {
            res.push_back(path);
            return;
        }
        for (int i = 0; i < nums.size(); i++) {
            if (i > 0 && nums[i] == nums[i - 1])  
                // i > 0: to add the number simply first time without checking and to avoid out of bound 'i-1'.
                continue;
            
            // using 'while' is logically correct but if 'i' reaches to len(nums), then automatically dfs will be called
            // and will give error index out of bound (nums[i]).
            // But if we use if with continue, then in this case, it will first go to for loop and if i == len(nums), 
            // it will automatically come out of 'for' loop and dfs will not be called and we will not get any error.

            // while (i > 0 && i < nums.size() && nums[i] == nums[i - 1])  
            //     i++;                               

            // add nums[i] in the path and skip nums[i] from the original array.
            vector<int> newNums = nums;
            newNums.erase(newNums.begin() + i);
            vector<int> newPath = path;
            newPath.push_back(nums[i]);
            dfs(newNums, newPath, res);
        }
    }

    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end()); // To avoid duplicates
        vector<vector<int>> res;
        dfs(nums, {}, res);
        return res;
    }
};

//Method 2 
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

class Solution {
public:
    void permutation(vector<int>& nums, vector<int> per, vector<vector<int>>& ans, set<int>& included) {
        if (per.size() == nums.size()) {
            ans.push_back(per);
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            // Skip used elements or duplicate elements (only the first occurrence can be used)
            if (included.find(i) != included.end() || (i > 0 && nums[i] == nums[i - 1] && included.find(i - 1) == included.end())) {
                // 1) if current ele is already used or 
                // 2) previous ele you have skipped and you want to use current ele
                // having same value as previous so it will lead to duplicate.
                // Because we only get duplicate while skipping.
                continue;
            }

            // If prev ele is used or current ele is not used, then we can take this ele.
            // Take this element.
            included.insert(i);
            per.push_back(nums[i]);
            permutation(nums, per, ans, included);
            // while backtracking remove i
            included.erase(i);
            per.pop_back();
        }
    }

    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end()); // To avoid duplicates
        vector<vector<int>> ans;
        set<int> included;
        permutation(nums, {}, ans, included);
        return ans;
    }
};

"""