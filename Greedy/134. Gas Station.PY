# how we can think this is a greedy based problem.
# we can only start from station whose gas capacity- cost to reach another station is >=0. 
# we are greedy about above diff only.
# if we find any such station just keep on adding the difference and if you find total< '0' at any time then 
# it means from starting gas station you can't travel a circle so just make total= 0 and start= i+1.

# Q here is: why we don't need to check in circular way i.e why only we are checking till 'n' and not only going in circle.
# because since there is only solution and if we are able to reach the end then it means we have found the ans.
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
            if total <0:  # means from this gas station we can't complete a circle
                start= i+1
                total= 0
        return start