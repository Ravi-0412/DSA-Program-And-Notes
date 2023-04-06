# method 1: Brute force
# time: O(n*k)= O(n^2)
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        num= [i for i in range(1, n+1)]
        start= 0  # index from which we will start counting
        while len(num) > 1:
            loser_index= (start + k-1) % len(num)
            # remove the friend at loser_index
            num.pop(loser_index)
            # now update start for next time
            start= loser_index   # we have to start from index just after cur friend is removed but after removing we will start from this loser_index only.(1 kam ho gya h isliye yahan se hi start karenge).
        return num[0]
            

# i was not able to find the pattern.

# logic: if we find the and for 'f(n-1,k)' then we can add '+k' in this to get ans for 'f(n,k)'.
# Reason: if we add one more friend then we will have to move in cirlce one more time to kill one more person after getting the ans fro pre one. (n-1) & so on.

# time= O(n)
# space= O(n). Recursion Auxiliary space
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ans= self.solve(n, k) + 1   # '+1' to bring into '1' based indexing.
        return ans
    
    def solve(self, n, k):
        if n== 1:  # since doing '%' so for n==1 it will return '0' only but in actual it should '1' so before returning addingf '+1'.
            return 0
        return (self.solve(n-1, k) + k) % n   # calculating in zero based indexing i.e for 'f(n-1,k ) doing '%' with 'n' for finding ans for 'f(n,k)'.
                                            # it should be '%' by 'n+1' but then we will get incorrect ans. 


# tabulation + space optimisation
# time= O(n), space= O(1)
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ans= 0
        for i in range(2, n+1):
            ans= (ans + k) % i
        return ans +  1
    
