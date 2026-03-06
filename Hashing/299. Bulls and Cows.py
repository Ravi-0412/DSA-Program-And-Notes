"""
First understand the Question properly.

secret code :      "1807".
player guesses :   "7810".

1. What is a BULL?
A Bull is a Perfect Match. The digit is the right number AND in the right house (position).
Look at index 1: Secret has 8, Guess has 8.
They are in the exact same spot. That is 1 Bull.

2. What is a COW?
A Cow is a Right Digit, Wrong House. The digit exists in the secret code, but it's sitting in the wrong spot in the guess.
The player guessed 7. There is a 7 in the secret, but it's at the end, not the beginning.
The player guessed 1. There is a 1 in the secret, but it's at the beginning, not the third spot.
The player guessed 0. There is a 0 in the secret, but it's in the middle, not the end.
That is 3 Cows.

Note : Don't Double Count
A digit cannot be both a Bull and a Cow at the same time. If the secret is 11 and the guess is 10:
The first 1 is a Bull.
Even though there is a 1 in the guess and a second 1 in the secret, you can't count that as a Cow because
you've already "used up" the 1 from the guess to make the Bull.
"""

# Method 1: 
"""
1. First Pass (The Easy Part): We compare secret[i] and guess[i]. If they match, it's a Bull. 
We don't need to do anything in this case.
2. The "Buckets" (Counting): For all the indices that weren't bulls, 
we count how many times each digit (0-9) appears in the secret and how many times it appears in the guess.
3. The "Overlap" (Cows): For each digit from 0 to 9, the number of Cows is the minimum of its count in the secret bucket
and its count in the guess bucket.
Example: if the secret has three 5s left and the guess has two 5s left, you can only pair up two of them as Cows.

Time : O(n)
space : O(10) = O(1)
"""

from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        # Buckets to count digits that are NOT bulls
        secret_bucket = [0] * 10
        guess_bucket = [0] * 10
      
        # Step 1: First Pass to find Bulls
        for i in range(len(secret)):
            s_char = secret[i]
            g_char = guess[i]
            
            if s_char == g_char:
                bulls += 1
            else:
                # If it's not a bull, put the digits into their respective buckets
                # Converting char to int to use as an index (0-9)
                secret_bucket[int(s_char)] += 1
                guess_bucket[int(g_char)] += 1
        
        # Step 2: Second Pass to find Cows
        cows = 0
        for i in range(10):
            # The number of misplaced matches for a digit is the 
            # smaller value between the two buckets.
            cows += min(secret_bucket[i], guess_bucket[i])
        return f"{bulls}A{cows}B"

# Method 2:
"""
In one pass and using one array
Crux : Somehow we need to update the digits not matching so that later we can know that we have already seen them in both
at some different position.

1. The Balance Array: 
  Create an array count of size 10 (initialized to 0) to track the "balance" of each digit.
    A positive value means the secret has "offered" this digit, but the guess hasn't "taken" it yet.
    A negative value means the guess has "requested" this digit, but the secret hasn't "offered" it yet.
    
2.Iterate Once: For each index i:
  If secret[i] == guess[i], it's a Bull. Easy.
  If they don't match:
    Check Secret's digit (s): If the balance for s is currently negative, 
    it means the guess was already looking for this digit. We just found a match! → cows += 1.
    Check Guess's digit (g): If the balance for g is currently positive, 
    it means the secret already offered this digit earlier. We found a match! → cows += 1.

3. Update Balance:
Increment count[s] (secret offers a digit).
Decrement count[g] (guess requests a digit).
"""

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        # Balance tracker for digits 0-9
        # Positive = Secret has extra, Negative = Guess has extra
        count = [0] * 10
        
        for i in range(len(secret)):
            s = int(secret[i])
            g = int(guess[i])
            
            if s == g:
                bulls += 1
            else:
                # If secret's current digit was previously requested by guess
                if count[s] < 0:
                    cows += 1
                # If guess's current digit was previously offered by secret
                if count[g] > 0:
                    cows += 1
                
                # Update counts: Secret digit adds, Guess digit subtracts
                count[s] += 1
                count[g] -= 1
                
        return f"{bulls}A{cows}B"

# Follow ups
"""
Q ) Interviewer: "If I give you a list of 1,000 guesses for the same secret, how would you optimize the process?"

The Problem: Re-calculating the secret frequency map 1,000 times is wasteful.
The Optimal Shift: 
1. Pre-calculate the frequency of all digits in the secret once.
2. For each guess, calculate Bulls first.
3. Subtract the Bull digits from your pre-calculated frequency map to find the available characters for Cows.

Google Logic: Tests Pre-processing and Caching.
"""
from collections import Counter

class BullsAndCowsSystem:
    def __init__(self, secret: str):
        self.secret = secret
        # Pre-calculate and cache the frequency of the secret
        # This happens once, regardless of how many guesses follow.
        self.secret_cache = Counter(secret)

    def calculate_hint(self, guess: str) -> str:
        bulls = 0
        cows = 0
        
        # We work on a copy of the cache so we don't ruin it for the next guess
        current_secret_map = self.secret_cache.copy()
        
        # List of indices that are not bulls to process in phase 2
        non_bull_indices = []

        # Phase 1: Identify Bulls and remove them from available Cow candidates
        for i in range(len(guess)):
            if guess[i] == self.secret[i]:
                bulls += 1
                current_secret_map[guess[i]] -= 1
            else:
                non_bull_indices.append(i)

        # Phase 2: Identify Cows from the remaining digits
        for i in non_bull_indices:
            char = guess[i]
            if current_secret_map[char] > 0:
                cows += 1
                current_secret_map[char] -= 1
                
        return f"{bulls}A{cows}B"

# Example of how Google would expect the usage:
# system = BullsAndCowsSystem("1123")
# print(system.calculate_hint("0111")) # 1 Bull, 1 Cow
# print(system.calculate_hint("1123")) # 4 Bulls, 0 Cows
