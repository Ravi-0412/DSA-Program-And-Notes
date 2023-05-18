# method 1: Assigning different people different hats.

# Brute force: TLE

# Time: O(n * 2^40 * 40)
# Explain: There are total i * assignedHats - 10 * 2^40 states in dfs(..i, assignedHats) function, 
# each state needs a loop up to 40 times (for (int hat : hats.get(i))) to calculate the result.
# Space: O(n * 2^40)

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n= len(hats)
        mod= 10**9 + 7

        def dp(person, assignedHats):
            if person== n:
                # means assigned different hats to 'n' people
                return 1
            ans= 0
            for hat in hats[person]:
                # check if this hat is already assigned to any other people
                if (assignedHats >> hat) & 1 == 1:
                    # if already assigned then simply skip
                    continue
                # otherwise assign this hat to 
                ans+= dp(person + 1, assignedHats | (1 << hat))
                ans%= mod
            return ans

        return dp(0, 0)
    

# method 2: Assign different hats to n people
# Note: The time complexity in Approach 1 is so big. Since n <= 10 is less then number of different hats <= 40.
# We can assign up to 40 different hats to n people and use dp to calculate number of ways.

# dp + memoisation

# Time: O(40 * 2^n * n), where n is the number of people, n <= 10
# Explain: There are total hat*assignedPeople = 40*2^n states in dfs(..hat, assignedPeople...) function, 
# each state needs a loop up to n times (int p : h2p[hat]) to calculate the result.
# Space: O(40 * 2^n)

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n= len(hats)
        mod= 10**9 + 7
        allPeopleAssigned= (1 << n) -1  # when assignedpeople will be equal to this then we have found one answer.
        # first find the list of people who wear ith hat
        hatsWithPeople= collections.defaultdict(list)
        for i in range(n):
            for hat in hats[i]:
                hatsWithPeople[hat].append(i)
                
        @lru_cache(None)
        def dp(hat, assignedPeople):
            # means we have assigned hats to all people
            if assignedPeople== allPeopleAssigned:
                return 1
            # no more hats to assign / process
            if hat > 40:
                return 0
            # when we don't want to assign the current hat to anyone
            # since no of hat > people so some hats may not be assigned to anyone.
            ans= dp(hat + 1, assignedPeople)
            # assign this hat
            for person in hatsWithPeople[hat]:
                # check if person is already assigned any hat.
                if (assignedPeople >> person) & 1== 1: # if assigned skip
                    continue
                # otherwise assign hat to the this 'person'.
                ans+= dp(hat + 1, assignedPeople | (1 << person))
                ans%= mod
            return ans

        return dp(0, 0)
