# Just simple multisource bfs (can do using single source using extra parameter).
# But multisource will help in avoiding 'memory limit exceeded'.

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