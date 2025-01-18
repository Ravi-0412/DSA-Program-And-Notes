# logic: 

"""
orginal: A[0], A[1], .... A[n-1]
derived: A[0]^A[1], A[1]^A[2] .... A[n-1]^A[0]

xor(derived) = (A[0]^A[1])^(A[1]^A[2])^ .... ^(A[n-1]^A[0]) = 0

The necessary and sufficient condition for derived to have an original is
xor(derived) == 0

And this will be only = 0 if all numbers will be present in even freqeuency.
But since here array is binary so we can also say that frequency of one should be even.
or 'sum(derived) % 2 == 0'.

So When original and derived is binary sequence,
this equals to sum(derived) % 2 == 0.

Note: this can apply to any q of this type.
"""

# time: O(n)
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return sum(derived) % 2== 0 
