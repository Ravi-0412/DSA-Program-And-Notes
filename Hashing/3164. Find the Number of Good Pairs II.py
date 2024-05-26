# Brute force:
# check each pair using two loops.
# Time: O(n^ 2)

# Optimisation

# 1st see how to find factors of a given number 'N'.

# 1) convert N into the product of prime numbers by prime factorization 
# N = X^a * y^b * z^c
# where X, Y and Z are the prime numbers and a, b and c are their respective powers.

# Total Number of Factors for N = (a+1) (b+1) (c+1)

# How to find it using code.
# For this we traverse the given number till its square root.
# say from 'i = 1' to its sqrt(N).
# if 'i' is factor of 'N' then 'N // i' will be also a factor of 'N'.
# so increase count by '2' if 'i != N //i ' else increase count by '1' to avoid duplicates.

# i will be smaller factor and 'N //i' will be bigger one.

def findNoOfFactors(num):
    cnt = 0
    i = 1 
    pairs = []
    while i * i <= num:
        if num % i == 0:
            if i != num // i:
                cnt += 2
                pairs.append([i, num // i])
                
            else:
                cnt += 1
                pairs.append([i])
        i += 1
    print("all factors: ", pairs)   # [smaller, bigger]
    return cnt

# num = 20
# num = 15
# num = 18
print(findNoOfFactors(num))


# Now come to actual question.
# for each number in num1, find all factors like above method.
# For count, store the frequency of 'nums2[i] * i' into a hashmap.
# And check each factor check if it is present in hashmap and icnrement the count.

# Time: O(10**5 * sqrt(10**6)) = O(10 ** 8)

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Create a hashmap to store counts of nums2[j] * k
        divisor_count = defaultdict(int)
        for num in nums2:
            divisor_count[num * k] += 1
        good_pairs = 0
        # For each number in nums1, find all its divisors and check against the hashmap
        for num in nums1:
            for j in range(1, int(num ** 0.5) + 1):
                if num % j == 0:
                    # j is a divisor
                    if j in divisor_count:
                        good_pairs += divisor_count[j]
                    # num // j is also a divisor if it's different from j
                    if j != num // j and num // j in divisor_count:
                        good_pairs += divisor_count[num // j]
        return good_pairs