# Method 1: 

# Logic: start from each number and find all combination we can make of 'k' numbers.
# Note: we only taking combination in increasing order because arrangement doesn't matter in combination.

# Note: All will be unique combination only because we are taking in increasing order only.

"""
Time Complexity: 
Total number of combinations =  O(C(n, k))
For each valid combination, we spend O(k) time to copy the list before adding it to the result.
So the total time complexity is: O(C(n, k) * k)

Sapce: O(C(n, k)) , Storing each combination
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def combination(num , remainin_no, comb):
            if remainin_no == 0:
                # we got one combination
                ans.append(comb)
                return
            # we can take next number from any of greater reamining number till 'n'.
            for i in range(num + 1, n + 1):
                combination(i, remainin_no - 1, comb + [i])

        # starting from each number one by one
        # we need to go till 'n- k + 1' not 'n' because when we will start with number > 'n- k + 1', we will not get 'k' numbers.
        for num in range(1, n + 1): 
            combination(num, k-1, [num])
        return ans
    

# Java Code 
"""
import java.util.*;

class Solution {
    List<List<Integer>> ans = new ArrayList<>();

    private void combination(int num, int remainin_no, List<Integer> comb, int n, int k) {
        if (remainin_no == 0) {  
            // We got one combination
            ans.add(new ArrayList<>(comb));
            return;
        }
        // We can take the next number from any of the greater remaining numbers till 'n'.
        for (int i = num + 1; i <= n; i++) {
            List<Integer> newComb = new ArrayList<>(comb);
            newComb.add(i);
            combination(i, remainin_no - 1, newComb, n, k);
        }
    }

    public List<List<Integer>> combine(int n, int k) {
        ans.clear();
        // Starting from each number one by one
        // We need to go till 'n - k + 1' not 'n' because when we start with a number > 'n - k + 1', we will not get 'k' numbers.
        for (int num = 1; num <= n; num++) {  
            combination(num, k - 1, new ArrayList<>(List.of(num)), n, k);
        }
        return ans;
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
    vector<vector<int>> ans;

    void combination(int num, int remainin_no, vector<int> comb, int n, int k) {
        if (remainin_no == 0) {  
            // We got one combination
            ans.push_back(comb);
            return;
        }
        // We can take the next number from any of the greater remaining numbers till 'n'.
        for (int i = num + 1; i <= n; i++) {
            vector<int> newComb = comb;
            newComb.push_back(i);
            combination(i, remainin_no - 1, newComb, n, k);
        }
    }

    vector<vector<int>> combine(int n, int k) {
        ans.clear();
        // Starting from each number one by one
        // We need to go till 'n - k + 1' not 'n' because when we start with a number > 'n - k + 1', we will not get 'k' numbers.
        for (int num = 1; num <= n; num++) {  
            combination(num, k - 1, {num}, n, k);
        }
        return ans;
    }
};
"""

# Method 2:
"""
Without using outer for loop & calling recursion once.
Idea is excatly simple as 1st method, just take number in increasing order to avoid repitition.
"""
"""
Time Complexity: 
Total number of combinations =  O(C(n, k))
For each valid combination, we spend O(k) time to copy the list before adding it to the result.
So the total time complexity is: O(C(n, k) * k)

Sapce: O(C(n, k)) , Storing each combination
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(start, remaining, comb):
            if remaining == 0:
                ans.append(comb)
                return

            for i in range(start, n + 1):
                backtrack(i + 1, remaining - 1, comb + [i])

        backtrack(1, k, [])
        return ans

# Java
"""
import java.util.*;

class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> ans = new ArrayList<>();

        backtrack(1, k, n, new ArrayList<>(), ans);
        return ans;
    }

    private void backtrack(int start, int remaining, int n, List<Integer> comb, List<List<Integer>> ans) {
        if (remaining == 0) {
            ans.add(new ArrayList<>(comb));  // add a copy of current combination
            return;
        }

        for (int i = start; i <= n; i++) {
            comb.add(i);
            backtrack(i + 1, remaining - 1, n, comb, ans);
            comb.remove(comb.size() - 1);  // backtrack step
        }
    }
}
"""

# C++
"""
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> ans;
        vector<int> comb;
        backtrack(1, k, n, comb, ans);
        return ans;
    }

    void backtrack(int start, int remaining, int n, vector<int>& comb, vector<vector<int>>& ans) {
        if (remaining == 0) {
            ans.push_back(comb);  // store the current combination
            return;
        }

        for (int i = start; i <= n; i++) {
            comb.push_back(i);
            backtrack(i + 1, remaining - 1, n, comb, ans);
            comb.pop_back();  // backtrack
        }
    }
};
"""
