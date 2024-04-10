# Note: just normal multisource bfs.
# we can also do by single source by storing minSteps also with coordinate in q.

#  1st time when we will see any cell that will be the minimum no of steps required to reach that cell

# time: O(n*n)

from collections import deque

class Solution:
	def minStepToReachTarget(self, KnightPos, TargetPos, N):
	    if KnightPos== TargetPos:
	        return 0
	    q= deque([])
	    visited= set()
	    minSteps= 0
	    r1,c1 = KnightPos
	    q.append((r1,c1))
	    visited.add((r1,c1))
	    while q:
	        for i in range(len(q)):
    	        r, c= q.popleft()
    	        directions= [[r-1, c+2], [r+1, c+2],[r-1, c-2], [r+1, c-2],[r-2, c+1], [r-2, c-1],[r+2, c+1], [r+2, c-1]]
    	        # right-up, right-left, left-up, left-down, up-right, up-left, down-right, down-left
    	        for nr, nc in directions:
    	            if 1<= nr <= N and 1<= nc <= N and (nr, nc) not in visited:
    	                if nr== TargetPos[0] and nc== TargetPos[1]:
    	                    return minSteps +1
    	                q.append((nr, nc))
    	                visited.add((nr, nc))
	        minSteps+= 1
	    return -1
