# Logic: There will be only two case in which collision won't happen i.e
# i) When all will move clockwise   ii) all will move anti-clockwise

# so ans for at least one collision = total possible way - 2
# And total possible way = 2**n because each monkey has two direction to move i.e either clockwise or anti-clockwise.

class Solution:
    def monkeyMove(self, n: int) -> int:
        mod = 10**9 + 7
        ways = self.myPow(2, n)
        return (ways - 2 + mod) % mod  # Ensure non-negative result 
    
        # Note: if ways -2 < 0 means in reality 'ways' must be > 10**9 + 7
        # so we have to add 'mod' to get the actual ans.
        # e.g: ways = 10**9 + 7 + 1 then after taking mod , ways = 1 and after '-2', ans = -1
        # But our ans should be 10**9 + 6 (10**9 + 7 + 1  - 2)
    
    def myPow(self, x, n):
        if n == 0: 
            return 1
        smallAns = self.myPow(x, n//2)
        smallAns = (smallAns * smallAns) % 1000000007
        if n%2 == 1:  
            return (x* smallAns) % 1000000007
        # if even
        return smallAns

# java
""""
public class Solution {
    private static final int MOD = 1_000_000_007;

    public int monkeyMove(int n) {
        long ways = myPow(2, n) % MOD;
        return (int) ((ways - 2 + MOD) % MOD); // Ensure non-negative result
    }

    private long myPow(int x, int n) {
        if (n == 0) {
            return 1;
        }
        long smallAns = myPow(x, n / 2);
        smallAns = (smallAns * smallAns) % MOD;
        if (n % 2 == 1) {
            return (x * smallAns) % MOD;
        }
        return smallAns;
    }
}
"""