# Brute force:
# Logic: If people time is between flower blooming time then he can see.

# Time: O(n^2) , TLE

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        ans = []
        for t in people:
            cnt = 0
            for start , end in flowers:
                if start <= t <= end:
                    cnt += 1
            ans.append(cnt)
        return ans

# Optimising
# Logic: Any person will not able to see all those flowers:
# 1) which has start bloom time > person_time.  The number of flowers that will start blooming after person_time .
# For this we need to sort the flowers acc to starting time.
# 2) which end bloom time < person_time      .  The number of flowers that have stopped blooming before person_time .
# For this we need to sort the flowers acc to ending time.

# So just find all those flowers they can't see and then to get the ans for cur people subtract with 'n'.

import bisect
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        n = len(flowers)
        start = [s for s, e in flowers]  # for getting flowers on right that cur person can't see
        end =   [e for s, e in flowers]  # for getting flowers on left that cur person can't see
        start.sort()
        end.sort()
        ans = []
        for t in people:
            can_not_see_right = n - bisect.bisect_right(start, t)
            can_not_see_left = bisect.bisect_left(end, t)
            can_see = n - can_not_see_right - can_not_see_left
            ans.append(can_see)
        return ans
    
# Do by meeting rooms logic also.
# Also try by other approaches in discusion.