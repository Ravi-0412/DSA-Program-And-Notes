# logic: Two node can be a part of a bridge if there is no any other path possible between those except the parent and nei path.
# steps and logic in comments.

# time: O(V+ E)
# space: O(V + 2E) for making the adjacncy list and O(3*n) for other arrays.

from collections import defaultdict 
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # First create the adjacency list
        adj= defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        print(adj)
        self.timer= 1  # will tell the visiting time of a node. for first node it will be equal to '1'.
        visited= set()
        first_time_visited=  [0]*n  # will store the first time when a node is visited.
        lowest_visited_time= [0]*n  # will store the lowest time in which we can reach the node from any of its adjacent node except parent.
        ans= []

        def dfs(node, parent):
            visited.add(node)
            # when we are first visiting, update the first and lowest time visited= timer
            first_time_visited[node]= lowest_visited_time[node]= self.timer
            self.timer+= 1    # incr the timer for next call
            # print(self.timer)
            # now check for its adjacent node
            for nei in adj[node]:
                if nei== parent:  # if we only take two cases one for visited and one for not visited then,we will get wrong ans.
                    continue      # as while updating the lowest time, we don't need time of parent and in  case'not' visited parent time will also get included. and we have to update the lowest time in both visited and not visited case.
                # if it is not visited then only chance is that , we may get bridge between node and its neigh while traversing back.
                # Because if already visited then we can reach that node through other path since we are not including parent.
                if nei not in visited:
                    dfs(nei, node)
                    # update the lowest_visited_time for node
                    lowest_visited_time[node]= min(lowest_visited_time[node], lowest_visited_time[nei])
                    # check if node---> nei can be part of bridge.
                    if lowest_visited_time[nei] > first_time_visited[node]:  # there was no other path we can reach (node-->nei).
                        ans.append([node, nei])                              # so they will form bridge.
                else:  # if already visited. then update the lowest time as we have to get the lowest time for node from all its neighbour either already visited or not except parent.
                    lowest_visited_time[node]= min(lowest_visited_time[node], lowest_visited_time[nei])
                     
        dfs(0, -1)  # starting from node '0' and parent= -1.
        print(lowest_visited_time, first_time_visited)  
        return ans

