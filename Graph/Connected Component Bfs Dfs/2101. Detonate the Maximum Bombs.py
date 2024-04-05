# Just same as:"695. Max Area of Island". Just we have to think and reduce into this q.

# Intitution: Just we have to find the "max no of node in connected comopnents".

# Howe we will connect ?
# if detonating bomb 'i' will detonate the bomb 'j' then we will add 'j' in adj list of 'i'.

# Note: it may happen that 'i' detonate 'j' but 'j' won't detonate 'i'.

# VVi: How we will find the detonating bombs?
# say we have to find whether detonating 'i' will detonate 'j' or not?
# if distance between their location is <= radius of 'i' then 'i' will detonate 'j'.


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # make adjacency list i.e connect bomb which can detonate each other
        adj= collections.defaultdict(list)  # [node: bombs that will get detonate after detonating 'node']
        n= len(bombs)
        for i in range(n):
            x1, y1, r1= bombs[i]
            for j in range(n):
                if i== j:
                    continue
                x2, y2, r2= bombs[j]
                # check if denotating 'i' can denotate 'j'.
                x_diff, y_diff= abs(x1 - x2), abs(y1 - y2)
                # if distance between their location is <= radius of 'i' then 'i' will detonate 'j'.
                if x_diff * x_diff + y_diff * y_diff <= r1*r1:
                    adj[i].append(j)

        def dfs(node, visited):
            count = 1
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                   count += dfs(nei, visited)
            return count

        # now just find the maximum no of nodes in a connected components
        ans= 1
        for i in range(n):
            visited= set()
            ans= max(ans, dfs(i, visited))
        return ans


# my mistake
# 1) I was taking 'visited' as global but it won't work.
# because: it may happen that 'i' detonate 'j' but 'j' won't detonate 'i'.

# 2) was finding the count in wrong way.
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # make adjacency list i.e connect bomb which can detonate each other
        adj= collections.defaultdict(list)  # [node: bombs that will get detonate after detonating 'node']
        n= len(bombs)
        for i in range(n):
            x1, y1, r1= bombs[i]
            for j in range(n):
                if i== j:
                    continue
                x2, y2, r2= bombs[j]
                # check if denotating 'i' can denotate 'j'.
                x_diff, y_diff= abs(x1 - x2), abs(y1 - y2)
                if x_diff * x_diff + y_diff * y_diff <= r1*r1:
                    adj[i].append(j)

        def dfs(node):
            count= 1
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                   count = 1 +  dfs(nei, visited)
                #   count += dfs(nei)
            return count

        # now just find the maximum no of nodes in a connected components
        visited= set()   
        ans= 1
        for i in range(n):
            if i not in visited:
                ans= max(ans, dfs(i))
        return ans


