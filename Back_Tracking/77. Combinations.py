# Logic: start from each number and find all combination we can make of 'k' numbers.
# Note: we only taking combination in increasing order because arrangement doesn't matter in combination.

# Note: All will be unique combination only because we are taking in increasing order only.

# time : O(n, k)  => 'n' choose 'k'.

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