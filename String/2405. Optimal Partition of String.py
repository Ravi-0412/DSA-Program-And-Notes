# Method 1:
# Logic: Try to make every partition as big as possible.
# So keep adding char in cur partition until you see that char again in that partition.

# Time = O(2*n) , adding and removing the same char in set
# space : O(n)

class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        ans = 1
        for c in s:
            if c in seen:
                seen.clear()  # to keep track of cur partition
                ans += 1
            seen.add(c)   # have to add in both seen and unseen case.
        return ans


# Method 2:
# Instead of clearing the set again and again just store the last occurrence of each char in an array.
# Note: If you see same char again with last seen >= current starting partition , 
# means that char is repeating in current partition.

# Logic is same as above only.

# Time = o(N), space = O(26)

class Solution:
    def partitionString(self, s: str) -> int:
        lastSeen = [-1]*26
        curPartitionStart = 0   # will store the starting index for current partition
        ans = 1
        for i, c in enumerate(s):
            index = ord(c) - ord('a')  # getting the index of 'c'.
            if lastSeen[index] >= curPartitionStart:
                ans += 1
                curPartitionStart = i
            lastSeen[index] = i
        return ans

# Method 3: Using bit
# Most optimised.

# Time = O(n) , space = O(1)

# But have confusion in time complexity i.e s = zzzzzzz....  then, we will need to shift '25' time to check.
# Have to ask someone about this.

class Solution:
    def partitionString(self, s: str) -> int:
        ans = 1
        flag = 0   # will tell whether any char already occured(set) or not occured(not set) in cur partition.
        # for 'a' it will be rightmost bit and for 'z' it will be leftmost bit
        for i , c in enumerate(s):
            bit_no = ord(c) - ord('a')  # bit no for 'c' in flag
            if flag & (1 << bit_no):
                # means set so will start new partition from here
                ans += 1
                flag = 0  # to check cur starting partition
            # Set the bit of 'c' in flag
            flag = flag | (1 << bit_no)
        return ans

