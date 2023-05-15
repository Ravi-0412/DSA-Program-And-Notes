# time: O(n)
# logic: just traverse the string and keep adding their value.


class Solution:
    def romanToInt(self, s: str) -> int:
        special= {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4,'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        # with the help of these special only we will find the ans.
        if s in special:
            return special[s]
        n= len(s)
        ans= 0
        pre= None
        i= 0
        while i < n:
            # first check if we can get any two digit special char.
            if i + 1 < n and s[i: i+ 2] in special:
                ans+= special[s[i: i+ 2]]
                i+= 2
            else:
                pre= s[i]
                count= 1
                while i+ 1 < n and s[i]== s[i+1]:
                    count+= 1
                    i+= 1
                i+= 1
                ans+= special[pre] * count
        return ans


# method 2:
# logic: just replace all the special two digit character(like for 4,9 ect..) with normal one
# so that we can apply the logic directly

class Solution:
    def romanToInt(self, s: str) -> int:
        special= {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4,'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        if s in special:
            return special[s]
        n= len(s)
        s = s.replace("IV", "IIII")
        s=  s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s=  s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s=  s.replace("CM", "DCCCC")
        number= 0
        for c in s:
            number+= special[c]
        return number


# method 3:
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) -1):
            # for handling the cases like 4,9 etc...
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:  # for normal case
                z += roman[s[i]]
        return z + roman[s[-1]]   # last one will be left