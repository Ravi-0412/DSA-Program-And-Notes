# time: O(n^2)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans= []
        for i in range(numRows):
            row_wise= []
            for j in range(i +1):
                # if we are at adding 1st and last ele at any row.
                if j== 0 or j== i:
                    row_wise.append(1)
                else:
                    num= ans[i-1][j-1] + ans[i-1][j]
                    row_wise.append(num)
            ans.append(row_wise)
        return ans


# python solution
# https://leetcode.com/problems/pascals-triangle/solutions/38128/python-4-lines-short-solution-using-map/


# Java Code
"""
import java.util.*;

class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans = new ArrayList<>();
        
        for (int i = 0; i < numRows; i++) {
            List<Integer> row_wise = new ArrayList<>();
            
            for (int j = 0; j <= i; j++) {
                // if we are adding the 1st and last element at any row.
                if (j == 0 || j == i) {
                    row_wise.add(1);
                } else {
                    int num = ans.get(i - 1).get(j - 1) + ans.get(i - 1).get(j);
                    row_wise.add(num);
                }
            }
            
            ans.add(row_wise);
        }
        
        return ans;
    }
}
"""

# C++ Code
"""
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans;
        
        for (int i = 0; i < numRows; i++) {
            vector<int> row_wise;
            
            for (int j = 0; j <= i; j++) {
                // if we are adding the 1st and last element at any row.
                if (j == 0 || j == i) {
                    row_wise.push_back(1);
                } else {
                    int num = ans[i - 1][j - 1] + ans[i - 1][j];
                    row_wise.push_back(num);
                }
            }
            
            ans.push_back(row_wise);
        }
        
        return ans;
    }
};
"""