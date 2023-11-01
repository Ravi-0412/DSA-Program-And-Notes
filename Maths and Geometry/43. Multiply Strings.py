# just conversion of logic we do the multiplication normally.
# time: O(m*n)
# space: O(m+ n)


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # if "0" in [num1] or "0" in [num2]:
        #     return "0"
        if "0" in [num1, num2]: return "0"  # concise way of writing above
        len1, len2= len(num1), len(num2)
        ans= [0]*(len1 + len2)
        num1, num2= num1[::-1], num2[::-1]  # revrsing to do multiplication left to right.
        for i1 in range(len1):
            for i2 in range(len2):
                digit= int(num1[i1]) * int(num2[i2])
                ans[i1 + i2]+= digit # directly add no matter single digit number or double digit number as carry for next will be given from here.
                                     # we have to add with already values of this position.
                # forward if carry to the next position in the ans'
                ans[i1+ i2+ 1]+= ans[i1 + i2] //10   # ading if any carry
                # now update the ans for current position
                ans[i1 + i2]= ans[i1 + i2]%10   

        # ans will be in reverse order. so 1st we have to reverse then remove the '0' from the left and then return the ans
        ans, beg= ans[::-1], 0
        while beg < len(ans) and ans[beg]== 0:
            beg+= 1
        return "".join(str(e) for e in ans[beg:])


# 1) if "0" in num1 or num2:  means if any of num1 or num2 will contain even a single zero then it will return the "0"
# 2) if "0" in [num1] or [num2]: it means if all char in array num1 or num2 is "0" then return  "0".
# 3) if "0" in [num1, num2]: just shorter way of writing the '2'.
