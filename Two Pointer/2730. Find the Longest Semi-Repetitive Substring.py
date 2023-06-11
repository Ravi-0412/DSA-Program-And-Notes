# logic: store all indexes (first index) where s[i] == s[i+ 1].

# time= space = O(n)
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n= len(s)
        if n== 1 or n== 2:
            return n
        indexes= [-1]  # will store the 1st index where s[i]== s[i-1]. '-1' to handle the corner cases.
        for i in range(n -1):
            if s[i] == s[i+1]:
                indexes.append(i)
        # means only one time we have found adjacent ele same so whole string will be our ans.
        if len(indexes) <= 2:
            return n
        # to handle the case when len(indexes) > 2 and there is no matching at last then to consider the substring from last also as ans if possible . e.g: "1223345678"
        if indexes[-1] != n - 2:
            indexes.append(n - 1)
        # now our ans will be equal to max difference between value of => max(2-0, 3-1, 4-2,...)
        # Because one repition we can include in our ans.
        ans= 1
        for i in range(2, len(indexes)):
            ans= max(ans, indexes[i] - indexes[i-2])
        return ans

# method 2: using Two pointer
# time= O(n)
# space: O(1)

# just converted the above logic in form of pointers.
# we only need 'cur' index(j), last_index of matching(last), previous index that we can include in our ans(i).

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n= len(s)
        if n== 1 or n== 2:
            return n
        i, j, last= 0, 1, 0 
        # 'i' will tell the starting index of subsring for possible ans
        # 'last' will denote the 'last index' where we have found 's[j]== s[j-1]' = j
        # 'j' will denote the cur index
        ans= 1
        while j < len(s):
            if s[j] == s[j -1]:
                if last:  # from 2nd time we will move 'i' as one repitition is allowed.
                    i= last
                last= j
            ans= max(ans, j- i + 1)    #'+' to include the last index where repitition was found.
            j += 1
        return ans

