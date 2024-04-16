# Just simple multisource bfs (can do using single source using extra parameter).
# But multisource will help in avoiding 'memory limit exceeded'.

# Note vvi: Whenever you are give some fixed no of operations for each state(step) and telling to find the 
# Minimum no of steps/days (or something) then think of multisource bfs and Dynamic Programming.

class Solution:
    def minDays(self, n: int) -> int:
        q = deque()
        q.append(n)
        steps=0
        visited=set()    
        
        while q:
            for _ in range(len(q)):
                x = q.popleft()
                if x == 0:
                    return steps
                if x % 3 == 0 and x//3 not in visited:
                    q.append(x//3)
                    visited.add(x//3)
                if x % 2== 0 and x//2 not in visited:
                    visited.add(x//2)
                    q.append(x//2)
                if x - 1 not in visited:
                    visited.add(x -1)
                    q.append(x -1)
            
            steps += 1

# Did by DP also.
# THis is best solution


# Related q:
# 1) 2998. Minimum Number of Operations to Make X and Y Equal
# 2) 