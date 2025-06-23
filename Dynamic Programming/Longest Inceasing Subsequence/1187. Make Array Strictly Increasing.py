# method 1: 
# Recursion + memoisation

# logic: 
# Note vvi: if you find arr1[i] > arr1[i+1] then you can't move simply ahead, you have to consider the swapping one also.
# Because you have to fidn the minimum swap.

# Here here choices will come and subproblem will repeat.

# For each element in arr1, you can either choose to not swap it or swap it with some element in arr2.

# 1) If you don't swap it, you need to make sure current element in arr1 is bigger than
# previous element in arr1. Otherwise you have to swap it.

# 2) If you swap it, you need to pick up the smallest element in arr2 that is bigger than the previous element in arr1. 
# If no such element in arr2, you can't swap

# dfs(i, prev): "i" represents index in arr1. "prev" represents the previous element in arr1 after swap (or maybe not swap). 
# It returns the minimal changes required to make 0~i of arr1 increasing.


# time: O(n^2 * logn)

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        n = len(arr1)

        def binary_search(x):
            # Find smallest element > x in arr2 using normal binary search
            left, right = 0, len(arr2) - 1
            pos = len(arr2)  # default to len(arr2) if none found
            while left <= right:
                mid = (left + right) // 2
                if arr2[mid] > x:
                    pos = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return pos
        
        dp = {float('-inf'): 0}

        for i in range(n):
            new_dp = {}
            for pre, cost in dp.items():
                # 1) no swap
                if arr1[i] > pre:
                    if arr1[i] not in new_dp or new_dp[arr1[i]] > cost:
                        new_dp[arr1[i]] = cost
                
                # 2) swap
                j = binary_search(pre)
                if j < len(arr2):
                    if arr2[j] not in new_dp or new_dp[arr2[j]] > cost + 1:
                        new_dp[arr2[j]] = cost + 1
            dp = new_dp
        
        if not dp:
            return -1
        return min(dp.values())

# Java Code 
"""
import java.util.*;

class Solution {
    int[] arr1, arr2;
    Map<String, Integer> memo;

    public int makeArrayIncreasing(int[] arr1, int[] arr2) {
        this.arr1 = arr1;
        this.arr2 = Arrays.stream(arr2).distinct().sorted().toArray();
        this.memo = new HashMap<>();
        int ans = dfs(0, Integer.MIN_VALUE);  // starting index 0 and pre = -infinity
        return ans == Integer.MAX_VALUE ? -1 : ans;
    }

    private int dfs(int ind, int pre) {
        if (ind >= arr1.length)
            return 0;  // we have traversed whole array

        String key = ind + "#" + pre;
        if (memo.containsKey(key)) return memo.get(key);

        // 1) if curr index 'ind' has value greater than last ele i.e pre then no need of swap
        int noSwap = arr1[ind] > pre ? dfs(ind + 1, arr1[ind]) : Integer.MAX_VALUE;

        // 2) find the rightmost position of 'pre' in arr2
        int j = Arrays.binarySearch(arr2, pre + 1);
        if (j < 0) j = -j - 1;

        // make pre = arr2[j], just swapping pre i.e. instead of arr1[ind] -> arr2[j]
        int swap = j < arr2.length ? 1 + dfs(ind + 1, arr2[j]) : Integer.MAX_VALUE;

        int result = Math.min(swap, noSwap);
        memo.put(key, result);
        return result;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <string>
using namespace std;

class Solution {
public:
    int makeArrayIncreasing(vector<int>& arr1, vector<int>& arr2) {
        sort(arr2.begin(), arr2.end());
        arr2.erase(unique(arr2.begin(), arr2.end()), arr2.end());  // removing duplicates
        this->arr1 = &arr1;
        this->arr2 = &arr2;
        return dfs(0, INT_MIN);
    }

private:
    vector<int>* arr1;
    vector<int>* arr2;
    unordered_map<string, int> memo;

    int dfs(int ind, int pre) {
        if (ind >= arr1->size())
            return 0;  // we have traversed whole array

        string key = to_string(ind) + "#" + to_string(pre);
        if (memo.count(key)) return memo[key];

        // 1) if curr index 'ind' has value greater than last ele i.e pre then no need of swap
        int noSwap = (*arr1)[ind] > pre ? dfs(ind + 1, (*arr1)[ind]) : INT_MAX;

        // 2) find the rightmost position of 'pre' in arr2
        auto it = upper_bound(arr2->begin(), arr2->end(), pre);
        int swap = it != arr2->end() ? 1 + dfs(ind + 1, *it) : INT_MAX;

        int res = min(noSwap, swap);
        memo[key] = res;
        return res == INT_MAX ? -1 : res;
    }
};
"""


# Method 2:
# Tabulation 
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        n = len(arr1)

        def binary_search(x):
            # Find smallest element > x in arr2 using normal binary search
            left, right = 0, len(arr2) - 1
            pos = len(arr2)  # default to len(arr2) if none found
            while left <= right:
                mid = (left + right) // 2
                if arr2[mid] > x:
                    pos = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return pos
        
        # dp[i][j] will store the minimum cost to make array increasing up to index i
        # with last element equal to some value represented by j (index in arr2 or arr1)
        # However, since arr1 elements can vary widely, we will keep track of pairs (last_val, cost)
        # This is similar to memo but now stored per i.
        
        # To simulate this, we keep a dictionary at each step i: dp[i] = {last_val: cost}
        dp = [{} for _ in range(n+1)]
        dp[0][float('-inf')] = 0  # Base case: before start, last element = -inf, cost = 0
        
        for i in range(n):
            for pre, cost in dp[i].items():
                # 1) no swap
                if arr1[i] > pre:
                    if arr1[i] not in dp[i+1] or dp[i+1][arr1[i]] > cost:
                        dp[i+1][arr1[i]] = cost
                
                # 2) swap
                j = binary_search(pre)
                if j < len(arr2):
                    if arr2[j] not in dp[i+1] or dp[i+1][arr2[j]] > cost + 1:
                        dp[i+1][arr2[j]] = cost + 1
        
        if not dp[n]:
            return -1
        return min(dp[n].values())

