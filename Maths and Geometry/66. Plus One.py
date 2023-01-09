class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n= len(digits)
        if digits[n-1]!= 9:
            digits[n-1]+= 1
            return digits
        else:
            digits[n-1]= 0
            j, carry= n-2, 1
            while j>= 0 and digits[j]==9 :
                digits[j]= 0
                j-= 1
            if j<0:
                digits.insert(0, 1)
            else:
                digits[j]+= carry
            return digits
