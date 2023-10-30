# Just same as " 445. Add Two Numbers II".

# Apply same logic as above Q.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1   # we have to add '+1'.
        for i in range(n - 1, -1, -1):
            carry , num = divmod(digits[i] + carry , 10)
            digits[i] = num
        return [1] + digits if carry else digits  # if carry == 1 add '1' to start of array
