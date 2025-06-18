# Method 1: 
# just same logic as '90.subset2'.

# just find all the unique subsets and check sum of each subset
# unique subsets we did in Q no '78 Subsets' in last case


# recursive and better way to avoid duplicates.
# read logic here or in notes.       
# time: O(2^n *k), k= average length of subsequence(for printing/putting each subsequence into another data structure).
# space: O(k*x), k: average length of subset and x: no of combinations(ans) without recursive space.

# logic: All duplicates can come together in one combination but not in different different combination to avoid duplicates combination.
# if they will come in different combination then, we will get duplicates in the ans.

# Not vvi: we will get duplicates in ans only when we will 'not include' the cur ele.
# So when we skip then we will choose the next distinct ele.


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res= []
        
        def dfs(i, subset, target):   # just backtracking
            if target== 0:
                res.append(subset)
                return
                
            if i== len(candidates):
                return
            # when you include the curr index ele. but you can only include if curr index value is less than target.
            if candidates[i] <= target:
                dfs(i+1, subset + [candidates[i]], target - candidates[i])
            # when you don't include the curr index ele. But when you don't include the curr index,
            # you have to skip all the duplicates of curr ele to avoid duplicate in the ans.
            while i+1 < len(candidates) and candidates[i+1]== candidates[i]:
                i+= 1
            dfs(i+1, subset, target)

        dfs(0, [], target)  
        return res


# Java
"""
import java.util.*;

class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);  // sort to handle duplicates
        List<List<Integer>> res = new ArrayList<>();
        dfs(0, new ArrayList<>(), target, candidates, res);
        return res;
    }

    // just backtracking
    private void dfs(int i, List<Integer> subset, int target, int[] candidates, List<List<Integer>> res) {
        if (target == 0) {
            res.add(new ArrayList<>(subset));
            return;
        }

        if (i == candidates.length) {
            return;
        }

        // when you include the curr index ele. but you can only include if curr index value is less than target.
        if (candidates[i] <= target) {
            subset.add(candidates[i]);
            dfs(i + 1, subset, target - candidates[i], candidates, res);
            subset.remove(subset.size() - 1); // backtrack
        }

        // when you don't include the curr index ele. But when you don't include the curr index,
        // you have to skip all the duplicates of curr ele to avoid duplicate in the ans.
        while (i + 1 < candidates.length && candidates[i + 1] == candidates[i]) {
            i++;
        }

        dfs(i + 1, subset, target, candidates, res);
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

    void dfs(int i, vector<int>& candidates, vector<int> subset, int target) {
        // Just backtracking
        if (target == 0) {
            res.push_back(subset);
            return;
        }

        if (i == candidates.size()) {
            return;
        }

        // When you include the current index element, but you can only include it if its value is less than target.
        if (candidates[i] <= target) {
            subset.push_back(candidates[i]);
            dfs(i + 1, candidates, subset, target - candidates[i]);
            subset.pop_back();
        }

        // When you don't include the current index element.
        // But when skipping the current index, you must skip all duplicates of the current element to avoid duplicates in the answer.
        while (i + 1 < candidates.size() && candidates[i + 1] == candidates[i]) {
            i++;
        }

        dfs(i + 1, candidates, subset, target);
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end()); // Sorting to handle duplicates
        res.clear();
        vector<int> subset;
        dfs(0, candidates, subset, target);
        return res;
    }
};
"""



