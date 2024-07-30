# logic: similar to "Two Sum".
# but here we can't find the other number directly like "Two Sum".

# for finding the other number :
# 1) we will store the 'gcd(n,k)' as key with 'frequency' as value.
# 2) for any number , want=  k//gcd. 
# Note: any multiple of 'want' will contribute ans.

# we have to find the product which is divisible by k.
# example if we need to make a pair which is divisible by 10 i.e k = 10, 
# so by far we have found 12 so the gcd of (12,10) will be 2 now what is the other number ?
# other_number = k//gcd = 10//2 = 5, we need to find it is 5 hence if we find 5's multiple or 5 we will add this pair to answer.

# time= (n* sqrt(n)) .
# since max number of divisor any number 'n' can have <= 2 * sqrt(n).

import math
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        frequency= collections.defaultdict(int)
        ans= 0
        for n in nums:
            Gcd = math.gcd(n, k)  # ex: 10 = k and we have nums[i] as 12 so gcd will be 2
            want= k // Gcd       # what do we want from upper ex: we need 5
            for num in frequency:
                if num % want== 0:
                    #so if we find a number that is divisible by 5 then we can multiply it to 12 and 
                    # make it a factor of 10 for ex we find 20 so it will be 240 which is divisible by 10 hence we will add it to answer.
                    ans+= frequency[num]  #we are adding the freq as we can find no of numbers that have same factor

            frequency[Gcd]= 1 + frequency.get(Gcd, 0)   # here we are increasing the freq of 2 so that if we find 5 next time we can add these to the answer
        return ans


# Method 2: More better and logical
# https://leetcode.com/problems/count-array-pairs-divisible-by-k/solutions/1785906/how-gcd-a-k-gcd-b-k-k-0-explained-with-example/

# Observation: 
# 1) If (a*b)%k == 0, then (gcd(a,k) * gcd(b,k)) % k == 0 and vice versa is also true i.e
# 2) if (gcd(a,k) * gcd(b,k)) % k == 0 then (a*b)%k == 0

# Here we will use 2nd property.
# We will store gcd(num, k) as key into hashmap and for cur number first we will find gcd and
# After that we will traverse whole hashmap to find another number following propert '2'.

# Proof of '2':
# For any number to be divisble by 'k' it need to have atleast all the prime factors of k.
# gcd(a,k) = Multiplication of all prime factors of 'k' available in 'a' and
# gcd(b,k) = Multiplication of all prime factors of 'k' available in 'b'.

# If (gcd(a,k) * gcd(b,k)) % k is 0, it means some of the prime factors of 'k' are contributed by 'a' and 
# some of the prime factors of 'k' are contributed by 'b' and 
# their multiplication has all the prime factors of 'k' which means 'a*b' is divisble by 'k'.

# Note: We dont care about prime factors of a or b which are not prime factors of k because they will not help us in making a*b divisible by k.

# Time Complexity - O(N*sqrt(K))
# Why sqrt(K) ?
# Since we are taking gcd, it means we are considering factors of K and the number of factors of K will not be above 2*sqrt(K).

import math
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        gcdCount = collections.defaultdict(int)
        ans = 0
        for num in nums:
            cur_gcd = math.gcd(num, k)
            for gc_d, count in gcdCount.items():
                if (cur_gcd * gc_d) % k == 0:
                    ans += count
            gcdCount[cur_gcd] += 1
        return ans

