"""
Follow up of question: 157. Read N Characters Given Read4
We can call read(), multiple times, then how will you handle this case? 

The Trap: If you call read(buf, 1) and read4 grabs 4 characters, you return 1. In your current code, the other 3 characters are wiped out when the function ends.
Fix: You must introduce class-level state (Persistence). Use a self.queue or self.buffer to store those extra 3 characters. 
Every time read is called, you check the self.queue first before calling read4 again.

Q) what is the difference between call once and call multiple times.
The buffer read4 is pulling from persists across user defined read calls.

Consider a get_3(buff) function which does the following:
1: creates temp
2: calls read4(temp)
3: put the first three elements of temp into buff
4: returns 3

Pretend read4 has "aaabbbccc" in its pipeline
The desired behavior of two get_3 calls is:
1: call get_3(buff). buff = aaa, 3 is returned
2: call get_3(buff). buff = bbb, 3 is returned

However this is not what happens.

On the first call of get_3(buff), this is what happens:
1: temp is created
2: we call read4(temp), it puts "aaab" into temp and returns 4
3: we move "aaa" from temp into buff
4: we return 3

The state of read4 is now "bbccc"
On the second call of get_3(buff), this is what happens:
1: temp is created
2: we call read4(temp), it puts "bbcc" into temp and returns 4
3: we move "bbc" from temp into buff
4: we return 3

So our two calls to get_3 output the strings "aaa", "bbc". This is wrong. This is why multiple calls must be considered.

Logic:
Memory Persistence: When you call read4, it might give you 4 characters, but if the user only asked for 1, 
you must "save" the other 3 for the next time the read function is called.

read(self, buf, n)
Note : n is the specific number of characters the user is asking for in the current call.

"""

from collections import deque

class Solution:
    def __init__(self):
        # The 'Tank': Persistent storage for characters read but not yet delivered
        self.cache = deque()

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        total_read = 0 # Tracks how many chars we've put into 'buf'
        
        # Keep going until we have 'n' characters or the file ends
        while total_read < n:
            # 1. REFILL LOGIC: If tank is empty, call read4 to get more data
            if not self.cache:
                buf4 = [''] * 4
                count = read4(buf4)
                # If read4 returns 0, the file is completely empty (EOF)
                if count == 0:
                    break
                # Push the newly read characters into our cache tank
                for i in range(count):
                    self.cache.append(buf4[i])
            # 2. DRAIN LOGIC: Transfer from tank to user's bucket (buf)
            # We transfer while: user still needs more AND tank isn't empty
            while total_read < n and self.cache:
                # popleft() takes the oldest character (First-In, First-Out)
                buf[total_read] = self.cache.popleft()
                total_read += 1
                
        # Return the total characters delivered in this specific call
        return total_read

# optimising the copy, Google follow ups 
# Best One
"""
What can be optimise ? => While the deque is clean, it involves creating a new list (buf4) and a new object (deque) which can be slow if read is called millions of times.
The optimization uses pointers on a single, fixed-size internal buffer. This avoids the overhead of Python's deque and list creation.

Logic:
1. Fixed Internal Buffer: Instead of a deque, use a fixed-size list of 4 elements (self.internal_buf).
2. Pointers: 
    * self.i: Points to the next character we need to read inside our internal buffer.
    self.n_chars: Tracks how many actual characters read4 put into the buffer (could be 1, 2, 3, or 4).
3. The "Drip" Logic:
    If self.i < self.n_chars, we still have "cached" data. We take it.
    If self.i == self.n_chars, our cache is empty. We call read4 to refill the buffer and reset self.i = 0.
"""
class Solution:
    def __init__(self):
        # One-time allocation: we never create another list after this
        self.internal_buf = [''] * 4
        self.i = 0       # Pointer to current char in internal_buf
        self.n_chars = 0 # Count of actual chars currently in internal_buf

    def read(self, buf, n):
        """
        Optimized Logic:
        1. Use a single pointer (self.i) to 'walk' through the 4-char internal buffer.
        2. Only refill (call read4) when the pointer reaches the end of the 4 chars.
        3. Avoids the overhead of deque objects and constant list re-allocations.
        """
        total_delivered = 0
        
        while total_delivered < n:
            # Step 1: Check if the internal buffer is empty
            if self.i == self.n_chars:
                # Refill the buffer from the file
                self.n_chars = read4(self.internal_buf)
                self.i = 0 # Reset pointer to the start of the new data
                
                # EOF: If read4 gives nothing, the file is finished
                if self.n_chars == 0:
                    break
            
            # Step 2: Transfer from internal buffer to user's 'buf'
            # We move one char at a time while data is in buffer and user needs more
            while total_delivered < n and self.i < self.n_chars:
                buf[total_delivered] = self.internal_buf[self.i]
                total_delivered += 1
                self.i += 1
                
        return total_delivered

