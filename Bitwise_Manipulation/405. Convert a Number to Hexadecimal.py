# first convert into positive equavalent value if number is negative using 2's complement logic.
# i.e positive value of 2's complement. e.g: for num == -1 => 2^32(1111....) 

# For this add '2^32' to given number.

# earn about 2's complement representation from link in sheet.

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0 :
            # will return positive value after converting into 2's complement.
            # i.e positive value of 2's complement. e.g: for num == -1 => 2^32(1111....)
            num = num + (1 << 32) 
        intToLetter = {10: "a" , 11 : "b" , 12 : "c" , 13 : "d" , 14 : "e", 15 : "f"}
        ans = ""
        while num :
            remainder = num % 16
            if remainder < 10:
                ans = str(remainder) + ans
            else:
                ans = intToLetter[remainder] + ans
            num = num // 16
        return ans


# decimal to binary
def toBinary(n):
    ans = ""
    while n >= 2 :
        remainder = n % 2
        ans = str(remainder) + ans
        n = n // 2
    print(str(n) + ans)
