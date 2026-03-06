"""
My mistake :  for every index i, the number of times s[i] appears in s must be the exact same as the number of times t[i] appears in t.
but it won't work:
e.g: s = "ababab", t = "bbbaaa"
Should be False but this logic will give correct.
Why False ? 
Mapping a -> b , b -> b  
There is two mapping for 'b' i.e from 'a' and 'b' itself but it should be only only.
"""

# Method 1:
"""
This Problem is all about One-to-One Mapping (Bijective mapping). For two strings to be isomorphic, 
every character in string $s$ must map to exactly one character in string $t$, and vice versa.

 Logic & Thought Process :
 The Core Constraint:
     If s[i] maps to t[i], then every time we see s[i] again, it must be paired with t[i].
      Conversely, two different characters in $s$ cannot map to the same character in t.
Two-Way Check:
    A mapping from s -> t is not enough. For example, if s = "ab" and t = "aa", 'a' maps to 'a' and 'b' maps to 'a'. 
    This is invalid because two characters map to the same target.
We can solve this using two Hash Maps or by checking if the number of unique pairs matches the number of unique characters in both strings.

Time = space = O(m + n)
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Logic:
        Maintain two dictionaries to ensure a unique bidirectional mapping.
        map_st: stores s[i] -> t[i]
        map_ts: stores t[i] -> s[i]
        """
        map_st = {}
        map_ts = {}
        
        # We can use zip to iterate through both strings simultaneously
        for char_s, char_t in zip(s, t):
            # Check if char_s has been mapped before
            if char_s in map_st:
                if map_st[char_s] != char_t:
                    return False
            else:
                # If not, create the mapping
                map_st[char_s] = char_t
                
            # Check if char_t has been mapped before (the reverse check)
            if char_t in map_ts:
                if map_ts[char_t] != char_s:
                    return False
            else:
                # If not, create the reverse mapping
                map_ts[char_t] = char_s
                
        return True

  # Method 2:
  """
  1. len(set(s)): How many unique characters are in s?
  2. len(set(t)): How many unique characters are in t?
  3. len(set(zip(s, t))): How many unique mapping pairs exist? 
  If all three numbers are equal, the mapping is perfectly 1-to-1.

  If s = "egg" and t = "add"
  zip(s, t) creates: ('e', 'a'), ('g', 'd'), ('g', 'd')
  set(zip("egg", "add")) becomes {('e', 'a'), ('g', 'd')} (Size = 2)
  """
