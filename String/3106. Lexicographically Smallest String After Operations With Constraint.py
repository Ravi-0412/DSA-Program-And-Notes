# Just try to replace each char with smallest possible char from 'a' to 'z'.

class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        ans = ""
        n = len(s)
        for c1 in s:
            replaced = False
            # check if we can replace c1 with smallest lexographically 
            # we can only replace if we have sufficient available 'k'/
            for i in range(97, 123):
                # only replace if chr(i) is smaller and there is suficient 'k' either linearly or circular
                if i < ord(c1) and (ord(c1) - i  <= k or 26 - (ord(c1) - i) <= k) :
                    ans += chr(i)  
                    k -= min(ord(c1) - i , 26 - (ord(c1) - i))
                    replaced = True
                    break
            if replaced == False:
                # If we can't replace then add the same char
                ans += c1
        return ans