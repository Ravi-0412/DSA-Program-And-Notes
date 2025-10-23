# Method 1: 

# just same as we did in "subsequnce with given sum" . only difference is
# 1) here in case arr[0]<=k i.e when we are including that index don't increment that index as we can include any ele any no of times
# As in case of subsequence repitition does not happen.
# 2) we will check for ans(base case) only when we will get the target first then for array end.

# time: O(2^t *k), t= target , k= length of every subsequence(for printing/putting each subsequence into another data structure)
# every ele will have t possibility in worst case i.e let target= 10 and 1st ele =1 
# space: O(k*x), k: average length of subset and x: no of combinations(ans) without recursive space

# same as subset.

# note: This is valid because number given are all distinct and positive.
# if given distinct number having both positive and negative value then we will have to check each subsequences at end if it's sum= target.

# Note: Since number is distinct then automatically we will get the unique combinations because there is no chance of duplicate combination.
# If not distinct then we will have to modify this little. can see in Q : "40. Combination Sum II".

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res= []
        self.SubsequenceSum(candidates,target,[],res)
        return res
    
    def SubsequenceSum(self,arr,k,path,res):
        if k== 0:
            res.append(path)
            return
        if not arr:  # not writing this will give error 'index out of bound' since we are not giving any base for index==n or 'not arr'
            return
        # if we include the current ele, then add arr[ind] into the ans
        if arr[0]<=k:   # i was skipping this condition. my mistake
                        # without this condition it will go into infinite loop will never stop because you can take same ele any number of tiems.
            self.SubsequenceSum(arr,k-arr[0],path+ [arr[0]],res)   # don't incr the index as repitition is allowed
        # if we don't include the current ele 
        self.SubsequenceSum(arr[1:],k,path,res)

# java
""""
import java.util.*;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        subsequenceSum(candidates, target, new ArrayList<>(), res, 0);
        return res;
    }

    public void subsequenceSum(int[] arr, int k, List<Integer> path, List<List<Integer>> res, int index) {
        if (k == 0) {
            res.add(new ArrayList<>(path));  // add copy of path
            return;
        }
        if (index == arr.length) {  // not writing this will give error 'index out of bound'
            return;
        }

        // if we include the current ele, then add arr[ind] into the ans
        if (arr[index] <= k) {  // i was skipping this condition. my mistake
                                // without this condition it will go into infinite loop will never stop because you can take same ele any number of times.
            path.add(arr[index]);
            subsequenceSum(arr, k - arr[index], path, res, index);  // don't incr the index as repetition is allowed
            path.remove(path.size() - 1);  // backtrack
        }

        // if we don't include the current ele 
        subsequenceSum(arr, k, path, res, index + 1);
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> res;

    void SubsequenceSum(vector<int>& arr, int k, vector<int> path, int index) {
        if (k == 0) {  
            // We got one valid combination
            res.push_back(path);
            return;
        }
        if (index >= arr.size()) {  
            // Not writing this will give error 'index out of bound' since we are not providing any base for index == n or empty array case
            return;
        }
        // If we include the current element, then add arr[ind] into the answer
        if (arr[index] <= k) {   
            // Skipping this condition was a mistake.
            // Without this condition, it will go into an infinite loop and never stop because the same element can be taken any number of times.
            path.push_back(arr[index]);
            SubsequenceSum(arr, k - arr[index], path, index);   // Don't increment index as repetition is allowed
            path.pop_back();
        }
        // If we don't include the current element 
        SubsequenceSum(arr, k, path, index + 1);
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        res.clear();
        vector<int> path;
        SubsequenceSum(candidates, target, path, 0);
        return res;
    }
};
"""


# Method 2:
"""
i) Does not pass res as a parameter
ii) Does not use a global or class variable
iii) Only uses return values from functions to build the result

How ans is getting added in python ?
ans = []                      # empty 1D list
part = [[2,2,3], [7]]         # this is a 2D list from recursion

ans += part                   # same as ans.extend(part)

What happens now ?
ans starts as []
part is [[2,2,3], [7]]
+= takes each element of part and adds it into ans
ans == [[2,2,3], [7]]

Why It Works (in one line)

ans += part does not add part as a single element, it unpacks it and adds each inner list → so ans changes from 1D to 2D naturally.

Contrast:
Operation	                        Result
ans.append(part)	                [[[2,2,3], [7]]] (3D style)
ans += part or ans.extend(part)	    [[2,2,3], [7]] (2D)
"""

class Solution:
    def combinationSum(self, candidates, target):
        return self.SubsequenceSum(candidates, target, [])

    def SubsequenceSum(self, arr, k, path):
        # If target is met → return a list containing this valid path
        if k == 0:
            return [path]

        # If array is empty → return no solution
        if not arr:
            return []

        ans = []

        # Include current element if it's <= remaining sum
        if arr[0] <= k:
            ans += self.SubsequenceSum(arr, k - arr[0], path + [arr[0]])

        # Exclude current element and move forward
        ans += self.SubsequenceSum(arr[1:], k, path)

        return ans

# Java
"""
import java.util.*;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        return helper(candidates, target, 0, new ArrayList<>());
    }

    private List<List<Integer>> helper(int[] arr, int target, int index, List<Integer> path) {
        if (target == 0) {
            List<List<Integer>> base = new ArrayList<>();
            base.add(new ArrayList<>(path));
            return base;
        }
        if (index == arr.length || target < 0) {
            return new ArrayList<>();
        }

        List<List<Integer>> ans = new ArrayList<>();

        // Include arr[index] if <= target
        if (arr[index] <= target) {
            path.add(arr[index]);
            ans.addAll(helper(arr, target - arr[index], index, path));
            path.remove(path.size() - 1); // backtrack
        }

        // Exclude current element → move to next
        ans.addAll(helper(arr, target, index + 1, path));

        return ans;
    }
}
"""

# C++
"""
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        return solve(candidates, target, 0, {});
    }

    vector<vector<int>> solve(vector<int>& arr, int target, int index, vector<int> path) {
        if (target == 0) {
            return { path };  // return a 2D list with one valid path
        }
        if (index == arr.size() || target < 0) {
            return {};  // return empty 2D list
        }

        vector<vector<int>> result;

        // Include element
        if (arr[index] <= target) {
            vector<int> withCurr = path;
            withCurr.push_back(arr[index]);
            vector<vector<int>> include = solve(arr, target - arr[index], index, withCurr);
            result.insert(result.end(), include.begin(), include.end());
        }

        // Exclude element → move forward
        vector<vector<int>> exclude = solve(arr, target, index + 1, path);
        result.insert(result.end(), exclude.begin(), exclude.end());

        return result;
    }
};
"""

