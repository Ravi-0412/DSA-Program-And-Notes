# Brute force. Just do what question is saying us to do.

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        cnt = 0
        dir =  1
        pos = 0
        while True:
            if dir == 1:
                pos += 1
            else:
                pos -= 1
            cnt += 1
            if cnt == k:
                return pos
            if pos == n - 1 or pos == 0:
                dir *= -1

# Method 2: Using math
# for each back and forth, time taken = (n - 1) i.e time to go from '0' to 'n-1' = n - 1 & time to return from 'n -1' to '0' = n -1
# so just find the rounds we can completed back and forth &&
# remainder 'k' which will tell how much time left after this much round.
# Then just return the 'k' based on rounds completed is even or odd.

# Note: In this type of questions apply same logic

class Solution:
    def numberOfChild(self, n: int, time: int) -> int:
        rounds = time // (n - 1)  how many rounds have we passed back and forth
        k = time % (n -1)  # index starting from left or right at the last round
        return k if rounds % 2 == 0 else n - k - 1   # 'n-k-1' to convert into '0' based indexing in case of reverse


# Similar Q:
# Only diff: here '1- based indexing'

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        rounds = time // (n - 1)
        k = time % (n -1)  # index starting from left or right at the last round
        return k + 1 if rounds % 2 == 0 else n - k  # 'k_+1' to convert to 1-indexing in case of even rounds
