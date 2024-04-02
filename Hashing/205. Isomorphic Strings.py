# Focus on this: "No two characters may map to the same character, but a character may map to itself".

# Why : 1) s= "bbbaaa" , t = "aaabbb" is giveing  'True' ?
# Ans: while traversing when b != a then we replaced b -> a and later at index 3 when a !=b then we replaced a -> b.

# Now 2) s= "bbbaaab" , t = "aaabbbb" is giving  'False' ? Just one more 'b' added to 's' and 't' in above test case.
# while traversing when b != a then we replaced b -> a and later at index 3 when a !=b 
# VVi: But at index 6 if we skip seeing equal char i.e chr 'b' in both at same index then
# you are mapping / replacing char 'b' with char 'b' i.e b -> b .
# But earlier only you replaced b -> a . So there is two mapping for 'b' i.e 'a' and 'b' which is not allowed.
# That's why False

# Note vvi: So don't skip blindy in case char is equal.

# How to solve this? How to keep mapping one -> one ?
# 1) We need to keep track of 'which char of 's' we have replaced by which char 't' ' so that when we encounter same char of 's' again
# We can check the char by which we had replaced this earlier.
# 2) We need to keep track of 'which char of 't' we have used as replacement for char of 's' , so that when we encounter same char of 't' 
# in unequal case then we can check whether we can this char of 't as replacement or not.

# So used two hashmaps.

# Time = space = o(n)


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        used = {}    # [replaced_by:   replaced_for]
        seen = {}    # [replaced_for : replaced_by]
        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if c1 in seen:
                # then value by which we have replaced 'c1' must be same as 'c2'.
                if seen[c1] != c2:
                    return False
            # If 'c1' is not in seen then we need to check if 'c2' has been used for replacement for
            # other character or not. If used then means we can't use this. so not possible
            elif c2 not in used:
                seen[c1] = c2
                used[c2] = c1
            else:
                # In all other case , it will be False only
                return False
        return True
    

# Got confused a lot in this Q