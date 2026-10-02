"""
What the problem asks, in plain words

You get several ranges, all of the same length d. Pick one number from each range. 
The score is the smallest distance between any two of your picked numbers. Make that score as large as possible.

start = [0, 3, 6], d = 2  → ranges [0,2], [3,5], [6,8]

pick 0, 4, 8 → distances 4, 4, 8 → score = smallest = 4
pick 2, 3, 6 → distances 1, 3, 4 → score = 1   (worse)
"""

"""
Ask : 
Turn the question around. Instead of "which numbers give the best score?", ask "for a given gap g, can I choose numbers that are all at least g apart?"
That yes/no check is easy, and its answers form T T T … F F F. So you can binary search over g.

1. Sort start. Every range has the same length d, so sorting by start also sorts by end. The chosen numbers can then be taken in the same left-to-right order as the ranges.

2. Greedy: in each range, pick the smallest number that is still at least gap away from the previous pick. Picking as far left as possible leaves the most room for the ranges that come after.
pick = max(prev + gap, start[i])     # at least gap after prev, and inside the range
if pick > start[i] + d → it doesn't fit in the range → False

Dry run: start = [6, 0, 3], d = 2

sorted start = [0, 3, 6] → ranges [0,2], [3,5], [6,8]

gap 4:  pick 0 → max(0+4, 3) = 4 ≤ 5 ✓ → max(4+4, 6) = 8 ≤ 8 ✓   → T
gap 5:  pick 0 → max(0+5, 3) = 5 ≤ 5 ✓ → max(5+5, 6) = 10 > 8 ✗  → F

Template 4 over gaps 0 … 8 (= 6 + 2 − 0):
low=0, high=8 → mid=4: T → low=5
low=5, high=8 → mid=6: F → high=5
low=5, high=5 → mid=5: F → high=4
low=5 > high=4 → stop → return high = 4 ✓

pick = max(prev + gap, start[i]), how ?
it finds the leftmost number you're allowed to take.
1. pick ≥ prev + gap      (far enough from the previous pick)
2. pick ≥ start[i]        (not left of the range)
3. pick ≤ start[i] + d    (not right of the range)
- max(prev + gap, start[i]) is the smallest number that satisfies both 1 and 2.

Time : O(n * logn + n * log(Range))
"""

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()                                   # equal-length ranges → sorted by start = sorted by end

        """Checks whether we can pick one number from each range so every two picks are at least `gap` apart.
            Returns True if possible, else False."""
        def can_achieve(gap):
            prev = start[0]                            # take the leftmost number of the first range
            for i in range(1, len(start)):
                pick = max(prev + gap, start[i])       # smallest number ≥ prev + gap inside this range
                if pick > start[i] + d:                # it falls past the range → this gap is impossible
                    return False
                prev = pick
            return True

        low, high = 0, start[-1] + d - start[0]        # widest possible gap: first left end to last right end
        while low <= high:                             # Template 4: find the LAST gap that works
            mid = low + (high - low) // 2
            if can_achieve(mid):
                low = mid + 1                          # works → try a bigger gap
            else:
                high = mid - 1                         # fails → the gap must be smaller
        return high                                    # Template 4 returns end (high)
