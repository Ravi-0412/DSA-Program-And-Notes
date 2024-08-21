# Already done in basic math.

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # Create a list to mark non-prime numbers
        not_prime = [False] * n
        count = 0
        
        for i in range(2, n):
            if not not_prime[i]:
                # if 'i' is prime then all it's multiple will be non-prime
                count += 1
                j = 2
                while i *j < n:
                    not_prime[i * j] = True
                    j += 1
                    
        return count

"""
public class Solution {
    public int countPrimes(int n) {
        boolean[] notPrime = new boolean[n];
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (notPrime[i] == false) {
                count++;
                for (int j = 2; i*j < n; j++) {
                    notPrime[i*j] = true;
                }
            }
        }
        
        return count;
    }
}
"""