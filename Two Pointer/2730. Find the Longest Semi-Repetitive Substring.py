# Intuition: Just we need to take careof pre 2 indexes where s[i] == s[i -1] or s[i] == s[i + 1]

# Method 1:

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
# we only need 'cur' index(i), last_index of matching(last), 2nd_last index of matching char.

# For any index 'i', we can include till 'i - second_last'.
# One repitition is allowed and one char we can include from 2nd_last.

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ans = 0
        second_last , last = -1, -1  # will store starting index i.e 'i-1' where s[i] == s[i -1].
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                second_last , last = last , i -1
            ans= max(ans, i - second_last) 
        return ans
    

# Note: Keep this method in mind , may help in other Q as well.

