# We will try to use the 1st operation as much as possible because 
# in this operation only we can increase our point && 
# if we don't have sufficient energy then we will use 2nd operation 
# to increase our energy so that later we can use this energy and apply operation1 to increase our point .
# If we can't apply any of above operation then break from loop.

# Note: If we use first operation then, we want our energy to lose as less as possible
# and if we use 2nd operation then we will want our energy to increase as much as possible.
# For this we need to keep track of enemies having minimum and maximum energy , 
# so we will sort the array. keep a pointer say 'j' that will point to 
# last element(enemy with maximum energy) and decrease 'j' when we use 2nd operation
# to mark visited and run a while loop till j >=0 && apply operation1 and operation2 in sequence.

# Note: We will apply operation1 only one the minimum ele i.e enemies[0].

# Time: O(n*logn) => TLE
class Solution:
    def maximumPoints(self, enemies: List[int], ce: int) -> int:
        # ce: currentEnergy
        n = len(enemies)
        enemies.sort()
        points = 0
        j = n - 1
        while j >= 0:
            if ce >= enemies[0]:
                points += 1
                ce -= enemies[0]
            elif points >= 1:
                ce += enemies[j]
                j -= 1
            else:
                break
        return points

# Above logic is correct. We can optimise the step 'ce -= enemies[0]'.
# Since we will apply operation1 only one the minimum ele i.e enemies[0], 
# so better use 'division' instead of '+' for incrementing 'points' &&
# '%' for updating 'ce'.

# Keep this thing in mind, will help in many problems.

class Solution:
    def maximumPoints(self, enemies: List[int], ce: int) -> int:
        n = len(enemies)
        enemies.sort()
        points = 0
        j = n - 1
        while j >= 0:
            if ce >= enemies[0]:
                points += ce // enemies[0]
                ce %= enemies[0]
            elif points >= 1:
                ce += enemies[j]
                j -= 1
            else:
                break
        return points

# Optimising to O(n)

# Observation:
# We always apply the first operation on the minimum value enemyEnergies[0], 
# extracting energy from all other values besides it.
# Why not directly find the minimum and calculate the cumulative sum?

# Note: When you will see the above code then you will observe that
# all index are contributing to 'currentEnergy' except minimum but points is only getting incremented by 'enemyEnergies[0]'

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        minEnergy = min(enemyEnergies) 
        total = currentEnergy + sum(enemyEnergies)
        if minEnergy > currentEnergy:
            return 0
        total -= minEnergy
        return total // minEnergy