# Approach:
"""
Problem statement suggwst that the power array is the array of power of 2's whose sum is value n. 
This is same as when u represent a number in binary, and consider only power of 2 which values are 1 in binary .
For example n = 5, binary = 101,
so n can be written as 1x2^2 + 0 x 2^1 + 1x 2^0.
= 2^2 + 2^0 = 4 + 1
So the array here will be [1, 4]

Now to check the ith bit if it is one or not we can simple check (n & ( 1 << i)) != 0

"""

from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        m = 10**9 + 7
        bint = []
        ans = []
        
        # Create power array
        for i in range(32):
            if (n & (1 << i)) != 0:
                bint.append(1 << i)
        
        for q in queries:
            i = q[0]
            p = bint[i]
            i += 1
            while i <= q[1]:
                p = (p * bint[i]) % m
                i += 1
            ans.append(p)
        
        return ans


# java
""""
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] productQueries(int n, int[][] queries) {
        int m = 1000000007;
        List<Integer> bint = new ArrayList<>();
        int[] ans = new int[queries.length];
        
        // Create power array
        for (int i = 0; i < 32; ++i) {
            if ((n & (1 << i)) != 0) {
                bint.add(1 << i);
            }
        }
        
        // Process queries
        for (int q = 0; q < queries.length; q++) {
            int i = queries[q][0];
            long p = bint.get(i++);
            while (i <= queries[q][1]) {
                p = (p * bint.get(i++)) % m;
            }
            ans[q] = (int) p;
        }
        
        return ans;
    }
}

"""