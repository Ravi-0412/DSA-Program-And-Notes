# Method 1: 

"""
e.g: [1 2 3 4 5 6 7 8] = Invalid
     [1, 8, 4, 5, 2, 7, 3, 6] = valid
     matches are : (1, 8), (2, 7), (3, 6), (4, 5) so valid
Logic: Sum of both players playing with each other must be equal to current_size of deque.
 Sum Property (P_1 + P_2 = Min + Max) is the mathematical invariant of a balanced tournament.

Why? Because of below condition
1. The ranks are a perfect sequence from 1 to N.
2. The best player (smaller rank) always wins.

But this logic won't work always, it working because of above two given condition.
Imagine a "Valid Draw" where the "Best" always plays the "Worst" available in their bracket, but the "Best" isn't always rank 1.
e.g: [1, 10, 5, 6]
1. Round 1 (Size = 4):
    Pair 1: 1 + 10 = 11
    Pair 2: 5 + 6 = 11
    Both pairs sum to 11 (1+10). 
    This is a "Best vs Worst" pairing for this specific group.
2. This Code's Check: It checks player1 + player2 == 4 + 1.
    11 == 5 is False
    Result: Your code says "Invalid," even though 1 played the worst (10) and 5 played the second worst (6).

Solution : To make the code work for any set of numbers (not just $1$ to N), we shouldn't use size + 1. Instead, we should find the actual min and max of the current round.
See next method

Note : In any single-elimination tournament, to find one winner from $N$ players, you must play exactly N - 1 matches. Since each match is O(1) work, the whole process is O(N).
"""
from collections import deque

def is_valid_draw(nums):
    n = len(nums)
    # Tournament must have a power of 2 players (2, 4, 8, 16...)
    # Logic: If it's not even or power of 2, the pairing logic breaks.
    if n == 0 or (n & (n - 1)) != 0:
        return False
    # Initialize queue with the starting draw
    queue = deque(nums)
    while len(queue) > 1:
        current_round_size = len(queue)
        # In each round, we process pairs
        # We use current_round_size // 2 because each match takes 2 players
        for _ in range(current_round_size // 2):
            player1 = queue.popleft()
            player2 = queue.popleft()
            # The "Valid Draw" Invariant:
            # The sum of two opponents must be (Number of players in this round + 1)
            # Example (N=8): 1+8=9, 2+7=9, 3+6=9, 4+5=9.
            if player1 + player2 != current_round_size + 1:
                return False
            # The winner (smaller rank) advances to the next level
            queue.append(min(player1, player2))
    return True

# --- Test Cases ---
print(is_valid_draw([1, 8, 4, 5, 2, 7, 3, 6])) # Expected: True
print(is_valid_draw([1, 2, 3, 4, 5, 6, 7, 8])) # Expected: False

# Method 2:
# Better one that will work always
"""
why not : current_round = next_round.copy() 
Ans: In Python, there is a big difference between mutating an object and rebinding a variable name.
The Logic: Rebinding vs. Mutating
In Python, there is a big difference between mutating an object and rebinding a variable name.
Rebinding (What you are doing): When you write current_round = next_round, you are telling the name current_round to 
stop looking at the old list and start looking at the next_round list. The old list (from the previous round) no longer has any names pointing to it, so Python's Garbage Collector eventually deletes it from memory.

Why .copy() isn't needed: You typically use .copy() if you want two different variables to point to the same data but keep them independent so that changing one doesn't affect the other.
In this loop, next_round is created fresh at the start of every while iteration (next_round = []).
Since you never touch next_round again after the assignment until it gets reset to [], there is no risk of accidental changes.

Time : N(1+ 0.5 + 0.25 + ...)  ~ O(2*N)
"""
def is_valid_draw(draw):
    current_round = draw
    
    while len(current_round) > 1:
        next_round = []
        # Find the min and max of the current remaining players to identify 'Best' and 'Worst'
        # In a valid draw, the sum of a pair should always be (min + max) of that pool.
        pool_min = min(current_round)
        pool_max = max(current_round)
        target_sum = pool_min + pool_max
        
        for i in range(0, len(current_round), 2):
            p1 = current_round[i]
            p2 = current_round[i+1]
            
            # Validation: Do these two form a Best-Worst pair?
            if p1 + p2 != target_sum:
                return False
            
            # Winner (the smaller rank) moves to the next round
            next_round.append(min(p1, p2))
            
        current_round = next_round
        
    return True

# Example 1: Valid Draw [1, 8, 4, 5, 2, 7, 3, 6]
# Round 1: (1+8=9), (4+5=9), (2+7=9), (3+6=9) -> All 9! Winners: [1, 4, 2, 3]
# Round 2: (1+4=5), (2+3=5) -> All 5! Winners: [1, 2]
# Round 3: (1+2=3) -> Valid!

# Example 2: Invalid Draw [1, 2, 3, 4, 5, 6, 7, 8]
# Round 1: (1+2=3) ... wait, target sum was 1+8=9.
# Returns False immediately.

# Method 3:
"""
To do in place to save memory
"""

def is_valid_draw_inplace(nums):
    n = len(nums)
    
    # Power of 2 check: Tournament brackets must be 2, 4, 8, 16...
    if n < 1 or (n & (n - 1)) != 0:
        return False
    
    # current_size represents how many players are still "active" in the array
    current_size = n
    
    while current_size > 1:
        # In a valid draw, the sum of paired opponents is always (Min + Max + 1)
        # For a standard 1-N tournament, this is (current_size + 1)
        target_sum = current_size + 1
        
        # We only need to iterate through half of the 'active' size to make matches
        for i in range(current_size // 2):
            # Index of the two players currently playing
            idx1 = i * 2
            idx2 = idx1 + 1
            
            p1 = nums[idx1]
            p2 = nums[idx2]
            
            # 1. Validation: Check the "Best vs Worst" invariant
            if p1 + p2 != target_sum:
                return False
            
            # 2. Promotion: Move the winner to the 'next round' section of the array
            # We overwrite nums[i] because i will always be <= idx1
            nums[i] = min(p1, p2)
        
        # 3. Update active size: The number of players is halved every round
        current_size //= 2
        
    return True

# Example Trace [1, 8, 4, 5, 2, 7, 3, 6]
# Start: size 8, target 9. Winners [1, 4, 2, 3] moved to nums[0:4]
# Next:  size 4, target 5. Winners [1, 2] moved to nums[0:2]
# Next:  size 2, target 3. Winner [1] moved to nums[0]
# Finish: returns True


# Follow ups
"""
Q) Given an integer N, find a valid draw (return a list of integers of length N). For example: the example above is not a valid draw. 
A valid draw example for N=4 would be: [1 4 2 3]

Ans : To find a Valid Draw, we need to reverse the logic we just used for validation.
Time : O(N) = 1 + 2 + 4 + 8 + 16 + .. = O(2 * N - 1)
"""
def generate_valid_draw(n):
    # Base case: The champion starts alone
    draw = [1]
    # We expand the tournament level by level (2, 4, 8... N)
    current_n = 1
    while current_n < n:
        # Every level doubles the number of players
        current_n *= 2
        new_draw = []
        # For every player already in the draw, 
        # pair them with the 'worst' player available in this new size
        for rank in draw:
            new_draw.append(rank)
            # The 'Worst' player for rank 'r' is (Total + 1 - r)
            new_draw.append(current_n + 1 - rank)
        draw = new_draw
        
    return draw

# --- Test Cases ---
print(f"N=2: {generate_valid_draw(2)}") # [1, 2]
print(f"N=4: {generate_valid_draw(4)}") # [1, 4, 2, 3]
print(f"N=8: {generate_valid_draw(8)}") # [1, 8, 4, 5, 2, 7, 3, 6]

