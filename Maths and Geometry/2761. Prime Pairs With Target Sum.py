# method 1: Brute force

# Logic: if we somemehow store the all primes numbers in a list then this q will reduce to 
# 'Find all pairs in a sorted list such that sum of pair = n'. (just two sum in sorted list).

# using 'Sieve of Eratosthenes' to check whether a number is prime or not.

# time: O(n*sqrt(n)). TLE due to n = 10^6

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:

        def isPrime(num):
            j = 2
            while j * j <= num:
                if num % j == 0:
                    return False
                j += 1
            return True

        primes = []
        for num in range(2 , n + 1):
            if isPrime(num):
                primes.append(num)
                
        ans= []
        i, j = 0, len(primes) - 1
        while i <= j:
            if primes[i] + primes[j] == n:
                ans.append([primes[i], primes[j]])
                i, j= i + 1, j - 1
            elif primes[i] + primes[j] > n:
                j -= 1
            else:
                i += 1
        return ans


# method 2:
# just same logic only but instead of checking each number whether prime or not,
# We are just marking the all multiples of a prime number till sqrt(n) as non-prime if it is prime.

# time complexity: n/2 + n/3 + n/5 +n/7 +.... n/p (where p will be the nearest prime to num)
# n(1/2 + 1/3+ 1/5+ 1/7 +.....)= n(loglogn) == O(n*log(logn))
class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        possiblePrimes = [True] *(n+ 1)
        i = 2 
        while i *i <= n:
            if possiblePrimes[i]:
                # if 'i' is prime then all its multiple must be non-prime
                # so make all multiple of 'i' non-prime
                j = i *2
                while j <= n:
                    possiblePrimes[j] = False  # making multiple of i.e 'j' as non-prime
                    j += i    # to move to next multiple of 'i'.
            i += 1
        
        # Now store all prime numbers in different array
        primes = []
        for i in range(2, n + 1):
            if possiblePrimes[i]:  # if 'i' is prime
                primes.append(i)

        ans= []
        i, j = 0, len(primes) - 1
        while i <= j:
            if primes[i] + primes[j] == n:
                ans.append([primes[i], primes[j]])
                i, j= i + 1, j - 1
            elif primes[i] + primes[j] > n:
                j -= 1
            else:
                i += 1
        return ans
