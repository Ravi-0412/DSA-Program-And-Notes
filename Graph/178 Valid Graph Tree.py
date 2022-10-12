# i was trying to do by 'union-find' but not able to do in case of more than one components 
# cycle is getting detected easily but for checking we have to use bfs or dfs. not able to do this by 'union find'

class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # handling the corner cases
        # for one node, there can't be any edge
        if n==1:
            if not edges:
                return True
            return False
        if n>1 and not edges:
            return False
    
        parent= [i for i in range(n)]  
        rank= [0] *(n)  # initally rank of all will be '0' since all are at height '0' (single node)
        
        # finding the root parent and the 1st level parent
        # for root level parent, compress the path till parent[p]!= p as root will parent as root only
        def find(n):
            p= parent[n]
            while p!= parent[p]:
                parent[p]= parent[parent[p]]  
                p= parent[p]
            return p
        
        def union(n1,n2):
            p1,p2= find(n1), find(n2)
            if p1== p2:            
                return False  
            
            if rank[p1]> rank[p2]:
                parent[p2]= p1
                
            else:
                parent[p1]= p2
                if rank[p2]== rank[p1]:
                    rank[p2]+= 1

            # return True    # without this it is also fine as we have to check when we can't add any more edges(False condition)
        
        # code starts from here
        for n1,n2 in edges:
            if union(n1,n2)== False:
                return False

        # returning the 'False' in above condition ,doesn't mean this is a tree for sure. it only means that there is no cycle

        # now check for single component. this was my misatke..
        # it is only valid if there is only one component


        # and we have to check whether there is only one component or more than one. if only one component then it means it is tree for sure
        # for checking this just compare the parent of each node, if any of the pair have different parent means more than one component else one_component(means tree)
        for i in range(n-1):
            for j in range(i+1,n):
                if parent[i]!= parent[j]:
                    return False
        return True

        # or 
        # unique_parent= set(parent)
        # print(unique_parent)
        # if len(unique_parent)!= 1:
        #     return False
        # return True


# method 2: using DFS
class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # first convert into adjacency list say 'graph'
        graph= collections.defaultdict(list)
        for s,d in edges:
            graph[s].append(d)
            graph[d].append(s)

        # handling the corner cases
        # for one node, there can't be any edge
        if n==1:
            if not edges:
                return True
            return False
        if n>1 and not edges:
            return False

        visited= set()
        # this will check cycle or not using DFS
        def isCycle(src,parent):
            visited.add(src)
            for u in graph[src]:
                if u not in visited:
                    if isCycle(u,src):
                        return True
                elif u != parent:  # means cycle
                    return True

        # code starts from here
        # for tree it shoule be connected and should not have a cycle
        # so we only need to call dfs once, if conneceted all node will get visited 
        if isCycle(0,-1):   # means cycle  
            return False
        if len(visited)== n:  # this will check connected or not
            return True
        return False

