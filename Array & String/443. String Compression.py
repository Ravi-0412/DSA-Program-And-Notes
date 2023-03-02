# Didn't submit but correct only.
class Solution:
    def compress(self, chars: List[str]) -> int:
        AnsIndex= 0
        i =0
        while i  < len(chars):
            curChar, count= chars[i], 0
            while i < len(chars) and chars[i] == curChar:
                i+= 1
                count+= 1
            # first append the char
            chars[AnsIndex]= curChar
            AnsIndex+= 1 
            # now append its count if count > 1.
            if count > 1:
                for c in str(count):
                    chars[AnsIndex]= c
                    AnsIndex+= 1
        return AnsIndex
        # return len(chars) # will give incorrect ans as chars will be diff but compiler is automatically modifying char till our ans.

