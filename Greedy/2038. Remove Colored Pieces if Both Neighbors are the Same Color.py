# If we calculate the frequency of consective length of 'A' or "B" if length >=3
# i.e s= "AAABBBAAABBBBAAAAABAAA" 
# for alice=> 3: 3, 5: 1  . freq of consective "A" having length = 3 is '3' , for length 5 is '1'.
# for bob => 3: 1 , 4:1   . freq of consective "B" having length = 3 is '3' , for length 4 is '1'.

# Note: One can take 'length -2' turn where length = consecutive same no i.e 'AAAA' turn= 2 (4-2)
# if freq of that length say 'x' then total turn = 'length -2' * x.

# Time = O(n) = space

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = collections.defaultdict(int)
        cnt = 0
        for i in range(len(colors)):
            if colors[i] == "B":
                if cnt >= 3:
                    # incr the freq of that length
                    alice[cnt] += 1
                cnt = 0
            else:
                cnt += 1
        # last one is not calculated in above loop.
        # In python 'i' value will be equal to last valid one after loop.
        if colors[i] == "A":
            if cnt >= 3:
                alice[cnt] += 1
        
        bob = collections.defaultdict(int)
        cnt = 0
        for i in range(len(colors)):
            if colors[i] == "A":
                if cnt >= 3:
                    bob[cnt] += 1
                cnt = 0
            else:
                cnt += 1
        if colors[i] == "B":
            if cnt >= 3:
                bob[cnt] += 1

        alice_turn_cnt = 0
        for key, val in alice.items():
            alice_turn_cnt += (key - 2)*val
        bob_turn_cnt = 0
        for key, val in bob.items():
            bob_turn_cnt += (key - 2)*val
        return alice_turn_cnt > bob_turn_cnt  # even in case of equal bob will win because 'alice' won't be able to take step in his turn.


# Method 2: 
# Very simple

# Logic: Count "AAA" and "BBB" and compare them
# You can only remove an A that is surrounded by two other A's and for "B".

# so there must be substring 'AAA' or "BBB" for removal.

# Time = O(n), space = O(1)

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        a_turn = b_turn = 0
        for i in range(1, n -1):
            if colors[i -1] == colors[i] == colors[i + 1]:
                # means we can remove 
                if colors[i] == "A":
                    a_turn += 1
                else:
                    b_turn += 1
        return a_turn > b_turn 