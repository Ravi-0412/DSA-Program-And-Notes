# how to think of bfs?
# Ans: we have given a source node and initial step (0) and we have to reach the destination with the help of the these fixed nodes.
# And also we will encounter diff diff states(numbers) and every time we have to check for these states now.

# Note: we will get the ans for generating number at 1st time we will get that number.

# for visited set: we only need to mark the generating num(curr_num) as visited at 1st time 
# since that will be minimum no of steps for that number.

import collections
class Solution:
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        q= collections.deque()
        mod= 100000
        q.append((start, 0))
        visited= set()
        visited.add(start)
        while q:
            n, steps= q.popleft()
            for num in arr:
                cur_num= (num * n) % 100000
                if cur_num== end:
                    return steps + 1
                if cur_num not in visited:
                    visited.add(cur_num)
                    q.append((cur_num, steps + 1))
        return -1