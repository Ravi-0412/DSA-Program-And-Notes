# how we can think this is a greedy based problem.
# we can only start from station whose gas capacity- cost to reach another station is >=0. 
# we are greedy about above diff only.

# start from '0'th gas station and 
# if we run out of fuel say at some ith gas station. All the gas station between ith and starting point are bad starting point as well.
# So, this means we can start trying at next gas station on the i + 1 station.
# i.e If we are not able to reach 'B' from "A" the, no station that is in between 'A' and 'B' can reach 'B'.\

# Proof?
# suppose there are c1,c2,...,ck station between 'A' and 'B'.
# A --- C1 --- C2  --- ... Ck --- B

# Facts:
# i)   A cannot reach B
# ii)  There are C1,C2, ..., Ck between A and B
# iii) A can reach C1, C2, ..., Ck

# Proof by contradiction:
# Assume: C1 can reach B
# A can reach C1 (by Fact3) & C1 can reach B => A can reach B (Contradict with Fact1 !)
# => assumption is wrong, C1 cannot reach B
# Same proof could be applied to C2 ~ Ck
# => any station between A and B that A can reach cannot reach B

# Note: we don't need to check in circular way because of above reason only.

# time: O(n)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):  # not possible from any gas station
            return -1
        start= 0  # our ans
        total= 0  # store the total gas present
        # checking each gas station one by one, we can only choose any gas station if difference of gas[i] and cost[i]>= 0.
        for i in range(len(gas)):
            total+= gas[i]- cost[i]   # we are just taking diff
            if total < 0:  # means from this gas station 'start' we can't complete a circle
                start = i+1
                total = 0
        return start