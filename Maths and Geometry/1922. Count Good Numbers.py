# Prime = [2,3,5,7]   between '0' to '9'
# even = [0,2,4,6,8]  between '0' to '9'

# Logic: if n = 1 then ans = 5 i.e 0,2,4,6,8  (all even)
# if n == 2 , we need to place prime number at odd position(last position)
# for this we have '4' possibility(no of prime) for each number generated in 'f(n-1)' i.e for n == 1
# so ans = 5 * 4

# if n == 3 then we need to place even number at even position(last position).
# for this we have '5' possibility(no of even no) for each number generated in 'f(n-1)' i.e for n == 2
# so ans = 5 * 4 *5

# Sequence will repeat for n=4, n= 5 and so on.

# i.e 5*4*5*4*5*4*5........

# Note: we can also reduce it to 20*20*20*......  
# i.e for n = 2 ans = 20, n= 4 ans = 20^2 and so on till n //2.

# From here we can observe that if n = even then our ans = 20^(n//2)
# But if n is odd then we need to multiply '5' to 20^(n//2) i.e ans = 20^(n//2) *5

# Note vvi: So now our Q reduces to find 20^m where m = n//2 then multiply '5' based on 'n' is odd or even.

# But if we will find the power(20, m) by normal it won't work because of larger value that we will get in power.
# So for this we will apply modulo by '10**9 + 7' at each step while calculating power.

# Explanation:
# storing answers that are too large for their respective datatypes is an issue with normal power method.
# In such instances, you must use modulus (%). Instead of finding x^n, you must find (x^n) % M.
# For example, run the implementation of the method to find . The solution will timeout, 
# while the solution will run in time but it will produce garbage values.

# If we needed to find 2^(10^5) or something big, then approach will run in O(logn) time, but produces garbage values as ans.

# time: O(logn)

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5

        def myPow(x, m):
            if m == 0: 
                return 1
            smallAns= myPow(x, m//2) % mod
            if m % 2 == 1:
                # if odd 
                return (x* smallAns* smallAns) % mod
            # if even
            return (smallAns* smallAns) % mod
        
        mod = 10 **9 + 7
        q , r = n // 2, n% 2
        power = myPow(20, q)
        return  power % mod if r == 0 else (power *5) % mod

        