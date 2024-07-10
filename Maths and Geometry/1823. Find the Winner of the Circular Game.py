# method 1: Brute force
# time: O(n*k)= O(n^2)
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # k = k  % n   # this will give wrong ans as 'n' will change after 'n' operations
        num= [i for i in range(1, n+1)]
        start= 0  # index from which we will start counting
        while len(num) > 1:
            loser_index= (start + k-1) % len(num)
            # remove the friend at loser_index
            num.pop(loser_index)
            # now update start for next time
            start= loser_index   # we have to start from index just after cur friend is removed but after removing we will start from this loser_index only.(1 kam ho gya h isliye yahan se hi start karenge).
        return num[0]
            
# Method 2: Using Dp
# Observation : 
# for n == 1 => answer will be always '1' for any value of 'k'
# Now: say , k= 2
# i) n = 2 , circle = [1, 2] => ans = 1 
# ii) n = 3 , circle = [1, 2, 3] => ans = 3 which is same as '(ans[n-1] + k) % n' + 1
# iii) n = 4 , circle = [1, 2, 3, 4] => ans = 1 which is same as '(ans[n-1] + k) % n' + 1

# why adding '+1'?
# Note: for 'f(n, k)' if we do '%' by 'n' then answer will be in range : 0 to n-1
# so to bring ans in range '1 to n', just add '1' at very last.

# so from here we get one pattern i.e f(n, k)= (f(n-1, k) + k) % n && ad '+1' while returning to convert into 1-based indexing.

# time= O(n), space= O(1)
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ans = 0  # for n = 0 , ans = '1' but we are taking '0-based' indexing
        for i in range(2, n+1):
            ans= (ans + k) % i
        return ans +  1
