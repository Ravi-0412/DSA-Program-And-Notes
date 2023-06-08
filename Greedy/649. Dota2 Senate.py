# logic: 
# Each senate R must ban its next closest senate D who is from another party, or else D will ban its next senate from R's party.

# The idea is to use two queues to save the index of each senate from R's and D's parties, respectively. 
# During each round, we delete the banned senate's index; and plus the remainning senate's index
# with n(the length of the input string senate), then move it to the back of its respective queue.

# VVI: Since the voting is done such that both sides perform the most optimal strategy, 
# the senators who have already voted will not be a problem to the other team for that round.
# So, instead of eliminating a senator who has already moved, the best move for each team is to eliminate the next senator who has the power to vote.
# This works perfectly with the queue approach since we can just place the senators who have voted at the end.

# Note: why greedy?
#  The game keeps going in loop until all people from single party is left. (e.g: "RRDDD")
# Otherwise people at alst of array will not get removed.

# Note: Opponent will want to remove the closest one in opposition first because after that other party will get the right to vote later
# which will result in removing more opponents.
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        qr, qd= collections.deque(), collections.deque()
        for i, c in enumerate(senate):
            if c== "R":
                qr.append(i)
            else:
                qd.append(i)
        while qr and qd:
            r, d= qr.popleft(), qd.popleft()
            if r < d:
                # means 'r'(Radiant) will ban 'd' but this 'r' should not ban any other 'd' before we traverse all the unbanned ele that has come before him
                # but this can be banned from other 'r' having lesser index so we will have
                # to increase its index value as lower index will ban only the greater one. so just add in queue with 'n + r'.
                qr.append(n + r)
            else:
                qd.append(n + r)
        return 'Radiant' if qr else "Dire"


# my mistakes and approaches
# 1) One people was banning more than one
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        Rcount, Dcount= 0, 0  # will store the count of people from 'Radiant' and 'Dire' respectively.
        for c in senate:
            if c== 'R':
                Rcount += 1
            else:
                Dcount += 1
        for c in senate:
            if c== 'R':
                # it will ban one of the opponent from 'D'
                Dcount -= 1
                if Dcount <= 0:
                    return "Radiant"
            else: # if people frm 'Dire'
                # it will ban one of the opponent from 'R'
                Rcount -= 1
                if Rcount <= 0:
                    return "Dire"
                
# 2) tried using 2 queue same problem
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        qr, qd= collections.deque(), collections.deque()
        for i, c in enumerate(senate):
            if c== "R":
                qr.append(i)
            else:
                qd.append(i)
        for c in senate:
            if not qr or not qd:
                break
            if c == "R":
                qd.popleft()
            else:
                qr.popleft()
        return "Radiant" if qr else "Dire"