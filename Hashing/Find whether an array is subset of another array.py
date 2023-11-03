# Subset means: arr1 should contain all ele of arr2 and quantity of all those ele in arr1 must be >= arr2.

# time= space= O(n)
from collections import Counter
def isSubset( a1, a2, n, m):
    hashmap1= Counter(a1)
    hashmap2= Counter(a2)
    for key, val in hashmap2.items():
        if val > hashmap1[key]:
            return "No"
    return "Yes"


# same way we can check "Two array is equal or not".
# frequency must be equal of each ele.

# Note: If order also mattering then it won't work.

from collections import Counter
class Solution:
    def check(self,A,B,N):
        hashmap1= Counter(A)
        hashmap2= Counter(B)
        for key, val in hashmap2.items():
            if val != hashmap1[key]:
                return False
        return True