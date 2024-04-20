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


# Java solution:
"""
public class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> triangle = new ArrayList<List<Integer>>();
        for (int i=0; i<numRows; i++){
            List<Integer> row =  new ArrayList<Integer>();
            for (int j=0; j<i+1; j++){
                if (j==0 || j==i){
                    row.add(1);
                } else {
                    int num = triangle.get(i-1).get(j-1) + triangle.get(i-1).get(j);
                    row.add(num);
                }
            }
            triangle.add(row);
        }
        return triangle;
    }
}
"""