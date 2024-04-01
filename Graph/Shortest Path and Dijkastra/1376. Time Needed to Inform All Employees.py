# logic: when we form tree according the hierarchy then ans= "max cost from root to leaf" where cost= time
# i.e find all cost from root to leaf then take maximum of all.

# Just converted the above one into graph and solved.

# How to form adjacency list? (here hierarchy)
# Just see who will pass inform to all other.
# say if 'i' will pass info to 'j' then add 'j' adjacent to 'i'.
# It will be a directed graph + no_cyclic. so no need of visited set.


# time: O(n)
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        hierarchy= collections.defaultdict(list)  # just forming adjacency list, directed graph
        for i in range(len(manager)):
            if manager[i]== -1:
                continue
            hierarchy[manager[i]].append(i)  # manager[i] will pass info to these employee 
        # now apply multisource bfs , with source as head.
        q= collections.deque()
        q.append((informTime[headID], headID))   # [time_to_pass_info, person_who_wil_pass_info]
        ans= 0  # minimum time taken can be 'zero'
        while q:
            time, id= q.popleft()
            ans= max(ans, time)
            for direct_emp in hierarchy[id]:
                # keep on adding time since it is passing from one person to another just like minimum spanning Tree
                q.append((time + informTime[direct_emp], direct_emp))   
        return ans

# method 2:  using dfs
# Note: Keep this method in mind, will help in lot of problems.
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        hierarchy= collections.defaultdict(list)  # just forming adjacency list, directed graph
        for i in range(len(manager)):
            if manager[i]== -1:
                continue
            hierarchy[manager[i]].append(i)  # manager[i] will pass info to these employee
    
        def dfs(u):
            ans= 0
            for v in hierarchy[u]:
                ans= max(informTime[u] + dfs(v), ans)
            return ans

        return dfs(headID)
    

# my mistake in dfs code
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        hierarchy= collections.defaultdict(list)  # just forming adjacency list, directed graph
        for i in range(len(manager)):
            if manager[i]== -1:
                continue
            hierarchy[manager[i]].append(i)  # manager[i] will pass info to these employee
    
        def dfs(u):
            ans= informTime[u]
            for v in hierarchy[u]:
                ans= max(ans + dfs(v), ans)
            return ans

        return dfs(headID)
