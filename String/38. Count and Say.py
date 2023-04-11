# just did seeing the pattern.


class Solution:
    def countAndSay(self, n: int) -> str:
        pre= "1"
        for i in range(2, n+1):
            cur= ""
            j= 0  # will traverse each char in  pre string to find the ans for next sequence
            while j < len(pre):
                ch= pre[j]
                count= 1  # default it will be '1' for each char.
                k= j+1
                while k < len(pre) and pre[k]== ch:
                    count+= 1
                    k+= 1
                cur+= str(count) + ch
                j= k
            
            pre= cur
        return pre