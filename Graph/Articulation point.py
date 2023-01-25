
# correct only(exactly same as Striver).
# but giving errot but i am not getting why and because of what that error is coming. 
# just leave for now and treat this as correct only
class Solution:
    def articulationPoints(self, V, adj):
        self.timer= 1  # will tell the visiting time of a node. for first node it will be equal to '1'.
        visited= set()
        first_time_visited=  [0]*V  # will store the first time when a node is visited.
        lowest_visited_time= [0]*V  # will store the lowest time in which we can reach the node from any of its adjacent node except parent and already visited node.
        mark= [0]* V   # the articulation node can repeat in ans so taking a marking variable to mark that.
                            # that can repeat when two or more child traverse back to it.

        def dfs(node, parent):
            visited.add(node)
            # when we are first visiting, update the first and lowest time visited= timer
            first_time_visited[node]= lowest_visited_time[node]= self.timer
            self.timer+= 1    # incr the timer for next call
            child= 0
            for nei in adj[node]:
                if nei== parent:  
                    continue      
                if nei not in visited:
                    dfs(nei, node)
                    # update the lowest_visited_time for node
                    lowest_visited_time[node]= min(lowest_visited_time[node], lowest_visited_time[nei])
                    # check if 'node' can be the articulation point.
                    
                    # nei should be reachable to node so why ('=' so that it can reach to node) but should not reach to node before its parent.
                    # for 'nei', there should be no other path we can reach to any other component and it can reach only to its parent(i.e node).
                    # note: Here is the difference from 'Bridge'.
                    if lowest_visited_time[nei] >=first_time_visited[node] and parent!= -1:    # for parent we will check separately.
                        mark[node]= 1
                        
                    child+= 1
                    
                # if already visited. then update the lowest time as we have to get the lowest time for node from first_time_visited of all its neighbour either already visited or not except parent.
                # since nei should be reachable to node for node to be the articulation point.
                # that's why taking the 'first_time_visited' of nei instead of 'lowest' since we have to reach the node from nei.
                else:  
                    lowest_visited_time[node]= min(lowest_visited_time[node], first_time_visited[nei])  
            
            # now check if parent is an articulation point.
            # parent can only be the articulation point if it's has more than one chid
            if child > 1 and parent== -1:
                mark[node]= 1

        # code starts from here.        
        # as graph can have more than one component.
        for i in range(V):
            if i not in visited:
                dfs(i, -1)
        ans= []
        for i in range(V):
            if mark[i]== 1:
                ans.append(i)
        return ans if len(ans) > 0 else -1