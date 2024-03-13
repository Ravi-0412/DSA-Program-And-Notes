# time: O(3^4)

# maximum recursion depth will go: '4' because we only need to form '4' dots.

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 :
            return []
        ans= []

        def backtrack(i, dots, curIP):
            if dots== 4 and i== len(s):
                ans.append(curIP[:-1])  # to remove the last dot
                return 
            if dots > 4 :
                return
            # for next dot we only need to check the next three char because 4 char together will be sure > 255.
            for j in range(i, min(i+3, len(s))):
                # checking integer value must be <= 255 and there is no leading zeroes.
                # for leading zeroes:  # take 1 digit is always good
                #take 2 or 3 digits etc, first digit cannot be '0'
                if int(s[i: j+1]) <= 255 and (i== j or s[i] != "0"):
                    backtrack(j+1, dots + 1, curIP + s[i: j+1] + ".")
            
        backtrack(0, 0, "")
        return ans
