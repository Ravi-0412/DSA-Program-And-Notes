# Note Q summary: The goal is to arrange the items in a way that groups are maintained, 
# item orders within groups are respected, and item relationships are satisfied."

# Here we have to keep track of two things:
# 1) order of items within gr 
# This we can get with normal topological sort as we do.
# After getting the topo order , just traverse the topo order and check the gr of every ele 
# and keep adding to the respective gr wise  somewhere(dictionary or 2d array)

# 2) we need to keep track of group order as well because we have to keep the items of same group together.
# And after getting the 1st(getting ele gr wise), how will know which gr items to keep first and so on.

# For this just apply the same topological sort on group as well like we do for nodes.

# Note vvi: No need to worry abou the relative order of items with other items in different group.
# That will get covered automatically in 1st case only.

# e.g:  say we have group1 : [1,2,3] and group2: [4,5,6] and we have dependencies say:
# 1->5 & 3->4 because the topological order of the groups will always have group1 before group2 these dependencies are always satisfied.


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # Helper function: returns topological order of a graph, if it exists.
        def get_top_order(graph, indegree):
            count, top_order = 0, []
            Q  = collections.deque()
            for i in range(len(graph)):
                if indegree[i]==0: 
                    Q.append(i)
        
            while Q:
                count+= 1  
                u= Q.popleft()
                top_order.append(u)
                # after poping decrease the indegree of all node adjacent to 'u'
                for j in graph[u]:
                    indegree[j] -= 1   
                    if indegree[j]== 0: 
                        Q.append(j)
            return top_order if len(top_order) == len(graph) else []
            # return top_order if count == n else []   # this will wrong ans in case of 'group ordering' so used like above.
                    
        # STEP 1: Create a new group for each item that belongs to no group. 
        # Note: if you will add all such items to same extra group then, you will get wrong ans.
        # Because you don't know how they are related so you can't add them to same gr.
        # That' why add each of them in separate new gr.
        for u in range(len(group)):
            if group[u] == -1:
                group[u] = m
                m+=1  # incraesing the gr no

        # STEP 2: Build directed graphs for items and groups.
        # Note: if you will take 'defaultdict(list)' for creating garph then same above function will not work for both.
        # We will have to make separate function for both.
        # But if we do like this then we can use same function for both.

        graph_items = [[] for _ in range(n)]           # for keeping track of items within same gr , just normal topological sort.
        indegree_items = [0] * n                       # for keeping track of items within same gr
        graph_groups = [[] for _ in range(m)]          # for keeping track of order of groups
        indegree_groups = [0] * m                      # for keeping track of order of groups
        # In graph gr we will only update if they belong to different group 
        for u in range(n):
            for v in beforeItems[u]:                
                graph_items[v].append(u)
                indegree_items[u] += 1
                if group[u]!= group[v]:
                    graph_groups[group[v]].append(group[u])
                    indegree_groups[group[u]] += 1                    

        # STEP 3: Find topological orders of items and groups.
        item_order = get_top_order(graph_items, indegree_items)  # getting order of all items as a whole
        group_order = get_top_order(graph_groups, indegree_groups)  # getting order of group.
        if not item_order or not group_order: return []   # means cycle so simply return []

        # STEP 4: Find order of items within each group.
        order_within_group = collections.defaultdict(list)   # will store items of a group together
        # the item that will come first in 'item_order' will be first to come in his group and so on.
        for v in item_order:
            order_within_group[group[v]].append(v) 

        # STEP 5. Combine ordered groups.
        # Add the items gr wise i.e acc to group order.
        res = []
        for group in group_order:
            res += order_within_group[group]
        return res


# Mine mistake:
# i had tried a lot but didn't get the ans.
# Not to the point solution.
# I was trying with one calling of topo sort.
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        itemsGroup = [set() for i in range(m + 1)]
        for i, gr in enumerate(group):
            if gr == -1:
                itemsGroup[m].add(i)
            else:
                itemsGroup[gr].add(i)
        # print(itemsGroup)


        AdjList= defaultdict(list)
        indegree= [0]*n
        # first convert into adjacency list(edges) i.e  directed graph for beforeItems and find the indegree of any nodes.
        for i , items in enumerate(beforeItems):
            for item in items:
                AdjList[item].append(i)
                indegree[i] += 1
        # print(AdjList, indegree)
        
        ansGroupWiseAndOrderWise = [[] for i in range(m + 1)]
        lastTimeOfGroup = [0 for i in range(m + 1)]
        # now applying the BFS to get the topological order
        count= 0
        Q  = collections.deque()
        for i in range(n):
            if indegree[i]==0: 
                Q.append(i)
    
        while Q:
            count+= 1  
            u= Q.popleft()
            u_gr = group[u]
            if u_gr != -1:
                itemsGroup[u_gr].remove(u)
                ansGroupWiseAndOrderWise[u_gr].append(u)
                lastTimeOfGroup[u_gr] = [count, u_gr]   
            else:
                itemsGroup[m].remove(u)
                ansGroupWiseAndOrderWise[m].append(u)
                lastTimeOfGroup[m] = [count, m]
            # after poping decrease the indegree of all node adjacent to 'u'
            for j in AdjList[u]:
                indegree[j] -= 1   
                if indegree[j]== 0: 
                    Q.append(j)
        if count != n:
            return []
        ans = []
        lastTimeOfGroup.sort()
        for i in range(m + 1):
            time, gr = lastTimeOfGroup[i]
            if gr != m:
                for j in range(len(ansGroupWiseAndOrderWise[gr])):
                    ans.append(ansGroupWiseAndOrderWise[gr][j])

        for j in range(len(ansGroupWiseAndOrderWise[m])):
                    ans.append(ansGroupWiseAndOrderWise[m][j])
        # print(itemsGroup, ansGroupWiseAndOrderWise,lastTimeOfGroup, "groups")
        # return [6, 3, 4,5, 2,0, 7, 1]
        return ans
        # return [5,2,6,3,4,0,7,1]