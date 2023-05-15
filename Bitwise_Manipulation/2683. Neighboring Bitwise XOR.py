# logic: 

# orginal: A[0], A[1], .... A[n-1]
# derived: A[0]^A[1], A[1]^A[2] .... A[n-1]^A[0]

# xor(derived) = (A[0]^A[1])^(A[1]^A[2])^ .... ^(A[n-1]^A[0]) = 0

# The necessary and suffisant condition for derived to have an original is
# xor(derived) == 0
# Note: this can apply to any q of this type.

# When original and derived is binary sequence,
# this equals to sum(derived) % 2 == 0.

# time: O(n)
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return sum(derived) % 2== 0 