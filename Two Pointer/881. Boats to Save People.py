# Logic: Since each boat carries at most two people at the same time.
# so for minimum we will try to take one person having maximum value and one person having minimum value.

# For taking like this sort the person and apply two pointer from start and end.

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        ans = 0
        i, j = 0 , n -1
        while i <= j :
            if people[i] + people[j] > limit:
                # Take only larger person i.e 'j'th person on the boat
                j -= 1
            else:
                # Take both person on the boat
                i += 1
                j -= 1
            ans += 1
        return ans