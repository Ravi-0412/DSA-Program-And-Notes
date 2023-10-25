# just did seeing the pattern.

# for visualisation:
# n = 1: return 1 is the base case
# n = 2: return count of last entry i.e. 1 1
# n = 3: return count of last entry i.e. two 1's so 21
# n=4: we have one 2 and one 1 so 1211
# n=5: , we have one 1 and one 2 and two 1's so -> 111221
# n=6: we have three 1's, two 2's and one 1 so -> 312211
# n = 7: we have one 3, one 1, two 2's and two 1's -> 13112221
# ...
# n = i: return counts in front of the number for entry of i-1 case

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