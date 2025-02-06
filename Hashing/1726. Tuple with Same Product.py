# Method 1: Check if 'd' is present using a,b,c (three loops)
# Time: O(N^3) = space

# Optimised one, # Time: O(N^2)
"""
VVI: We count the product of every 2 distinct numbers .

Q) Every tuple has 8 permutations, How?
No of ways of arranging (a* b) = 2 {(a,b),(b,a)}
No of ways of arranging (c*d) = 2 {(c,d),(d,c)}
No of wasy of arranging (a*b) and (c*d) = 2  {(a*b)=(c*d), (c*d)=(a*b)}
Hence the total no of ways = 2*2*2 =8 

e.g: From test case 1 [2,3,4,6] we have count map which is {6:1, 8:1, 12:2, 18:1 , 24:1}, 
and from test case 3 [2,3,4,6,8,12] we know that when we loop to 8, 
we have additional products 8*2, 8*3, 8*4, 8*6 = 16, 24, 32, 48 to add to count map, 
then our count map becomes {6:1, 8:1, 12:2, 16:1, 18:1 , 24:2, 32:1, 48:1}, 24:2 makes res += 8, 
then keep doing this for last element 12, you will see res == 40.
"""

# Time: O(n^2)

from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums):
        n = len(nums)
        product_count = defaultdict(int)
        res = 0

        for i in range(n):
            for j in range(i):
                prod = nums[i] * nums[j]
                # Every tuple has 8 permutations
                res += 8 * product_count[prod]
                product_count[prod] += 1

        return res

# Java
"""
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int tupleSameProduct(int[] nums) {
        int n = nums.length;
        Map<Integer, Integer> productCount = new HashMap<>();
        int res = 0;

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                int prod = nums[i] * nums[j];
                // Every tuple has 8 permutations
                res += 8 * productCount.getOrDefault(prod, 0);
                productCount.put(prod, productCount.getOrDefault(prod, 0) + 1);
            }
        }

        return res;
    }
}
"""
