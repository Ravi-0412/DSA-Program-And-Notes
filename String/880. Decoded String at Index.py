# Logic: Only the character in the Kth position matters rather than the whole string decoded, so we only keep track of curLength('n').

# Note: why k %= n ?

# If we have a decoded string like 'appleappleappleappleappleapple' and an index like K = 24, the answer is the same if K = 4.

# In general, when a decoded string is equal to some word with 'size' length repeated some number of times,
# (such as apple with size = 5 repeated 6 times), the answer is the same for the index K as it is for the index K % size.

# We can use this insight by working backwards, keeping track of the size of the decoded string. 
# Whenever the decoded string would equal some word repeated d times, we can reduce K to K % (word.length).

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        n = 0 # will store the length of decoded string till now

        # Just go till length of decoded string becomes >=k.
        i = 0
        while i < len(s):
            c= s[i]
            n = n *int(c) if c.isdigit() else n + 1
            if n >= k:
                break
            i += 1
        # Now traverse back from cur index 'i' to find the actual char.
        j = i
        while j >= 0:
            c = s[j]
            if c.isdigit():
                n /= int(c)  # length before this 'digit'
                k %= n
            else:
                # we will only get our ans if it is a char and when k == n or k == 0.
                if k == n or k == 0:
                    return c
                n -= 1
            j -= 1