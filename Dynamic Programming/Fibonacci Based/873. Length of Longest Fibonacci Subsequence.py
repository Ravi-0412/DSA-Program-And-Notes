# 1st method
# Logic :
"""
Save array A to a hash set s.
Start from base (A[i], A[j]) as the first two element in the sequence,
we try to find the Fibonacci like subsequence as long as possible,

Initial (a, b) = (A[i], A[j])
While the set s contains a + b, we update (a, b) = (b, a + b).
In the end we update the longest length we find.

Time Complexity:
O(N^2logM), where M is the max(A).

Since the values grow exponentially,
the amount of numbers needed to accommodate a sequence
that ends in a number M is at most log(M).
"""

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        s = set(A)
        res = 2
        for i in range(n):
            for j in range(i + 1, n):
                a, b, l = A[i], A[j], 2
                while a + b in s:
                    a, b, l = b, a + b, l + 1
                res = max(res, l)
        return res if res > 2 else 0

# Java
"""
class Solution {
    public int lenLongestFibSubseq(int[] A) {
        Set<Integer> s = new HashSet<Integer>();
        for (int x : A) s.add(x);
        int res = 2;
        for (int i = 0; i < A.length; ++i)
            for (int j = i + 1; j < A.length; ++j) {
                int a = A[i], b = A[j], l = 2;
                while (s.contains(a + b)) {
                    int temp = b;
                    b = a + b;
                    a = temp ;
                    l++;
                }
                res = Math.max(res, l);
            }
        return res > 2 ? res : 0;
        
    }
}
"""

# Method 2: DP + 2 sum
# Logic:
"""
For each A[i] find previous 2 elements sum up to A[i],
then it's a classical follow up problem for Two Sum
167. Two Sum II - Input array is sorted
if 2 elements A[l] and A[r] sum up to A[i]
dp[r][i]: length of longest fibonacchi sequence end with A[r], A[i]
dp[r][i] = dp[l][r] + 1
return the max(all posible dp[r][i])
"""

class Solution:
    def lenLongestFibSubseq(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[2]*n for _ in range(n)]   # default length will be two only between every pair.
        ans = 0
        for i in range(2,n):
            l, r = 0, i-1
            while l<r:
                if nums[l]+nums[r] > nums[i]:
                    r -= 1
                elif nums[l]+nums[r] < nums[i]:
                    l += 1
                else:
                    dp[r][i] = dp[l][r] + 1
                    ans = max(ans, dp[r][i])
                    r -= 1
                    l += 1
        return ans

# Java
"""
    public int lenLongestFibSubseq(int[] A) {
        int n = A.length;
        int max = 0;
        int[][] dp = new int[n][n];
        for (int i = 2; i < n; i++) {
            int l = 0, r = i - 1;
	        while (l < r) {
                int sum = A[l] + A[r];
                if (sum > A[i]) {
                    r--;  
                } else if (sum < A[i]) {
                    l++;
                } else {
                    dp[r][i] = dp[l][r] + 1;
                    max = Math.max(max, dp[r][i]);
                    r--;
                    l++;
                }
            }
        }
        return max == 0 ? 0 : max + 2;
    }


"""

# Note: Understand and do by this later, solution in sheet
