# logic: when we form tree according the hierarchy then ans= "max cost from root to leaf" where cost= time
# i.e Max path sum from root to leaf.
# Just similar to 2nd approach of q: "2050. Parallel Courses III".

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
                q.append((time + informTime[direct_emp], direct_emp))   # informTime[i] == 0 if employee i has no subordinates. This restriction will handle automatcally
                                                                        # if 'direct_emp' has no subordinate.
        return ans

# method 2:  using dfs

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

# Other way of writing this
# Better one. Just same as ""2050. Parallel Courses III"." 2nd method.

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        hierarchy= collections.defaultdict(list)  # just forming adjacency list, directed graph
        for i in range(len(manager)):
            if manager[i]== -1:
                continue
            hierarchy[manager[i]].append(i)  # manager[i] will pass info to these employee
    
        def dfs(u):
            max_time = 0
            for v in hierarchy[u]:
                max_time = max(max_time, dfs(v))
            return informTime[u] + max_time

        return dfs(headID)
    

# my mistake in dfs code
# it will give ' sum of time of all inform time'.
# e.g: n = 15, head = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6] , time = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
    # it will give ans = 7 but actual ans = 3

# Note vvi: Understand the difference between these two mathod properly.
# Understand this why giving incorrect ans later.
    
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
