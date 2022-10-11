# my mistake ,I didn't get the Q at all.. This mistake i am making again and again

# method 1: using DFS+ hashmap
# logic: since we have to copy the node so we have to store somewhere so that we can use that again and again
# and for this only one data structure comes into mind 'hashmap'
# and for traversal, we have to use either BFS or DFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew= {}  # to store the copy of the node
        
        # go to each node and create its copy if not present and then add all its neigbors
        #  to the 'neighbors list of copied node' seeing its adjacent from the original node
        def clone(node):
            # base case
            if node in oldToNew:
                return oldToNew[node]
            # if not present then create the copy 
            copy= Node(node.val)
            oldToNew[node]= copy
            # now add all its neighbors to the 'neighbors' list
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy
        return clone(node) if node else None


# another way of writing the above code: simpler one
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dic = {}
        def dfs(node):
            if not node:
                return
            else:
                node_copy = Node(node.val, [])
                dic[node] = node_copy
                for nei in node.neighbors:
                    if nei in dic:
                        node_copy.neighbors.append(dic[nei])
                    else:   
                        node_copy.neighbors.append(dfs(nei))
                return node_copy
        return dfs(node)


# method 2: using BFS
# same logic as above. working corectly (found from submissions)
def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return 
        nodeCopy = Node(node.val, [])
        dic = {node: nodeCopy}
        queue = collections.deque([node])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in dic: # neighbor is not visited
                    neighborCopy = Node(neighbor.val, [])
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy


# this same thing i am writing by understanding the above one is not working. not getting why
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        Q= collections.deque()
        Q.append(node)
        copy= Node(node.val)
        clones= {}
        clones[node]= copy
        while Q:
            curr= Q.popleft()
            clone_curr= clones[curr]
            for nei in curr.neighbors:
                if nei not in clones:
                    neiCopy= Node(nei.val)
                    clones[nei]= neiCopy
                    Q.append(nei)
                clone_curr.neighbors.append(neiCopy)
        return copy


# this i don't know why its giving correct ans by returning 'clones' at last. same logic only
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        clones= {}
        Q= collections.deque()
        Q.append(node)
        clones[node]= Node(node.val)
        while Q:
            curr= Q.popleft()
            clone_curr= clones[curr]
            for nei in curr.neighbors:
                if nei not in clones:
                    copy= Node(nei.val)
                    clones[nei]= copy
                    Q.append(nei)
                clone_curr.neighbors.append(clones[nei])
        return clones[node]