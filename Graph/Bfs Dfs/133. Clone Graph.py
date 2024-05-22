
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



# method 2: using BFS
# same logic as above.
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return 
        nodeCopy = Node(node.val)
        dic = {node: nodeCopy}    #  will contain the clone(copy) of each node
        queue = collections.deque([node])
        while queue:
            node = queue.popleft()
            # now go to adjacent node and add as its neighbor by copying
            for neighbor in node.neighbors:
                if neighbor not in dic: # neighbor is not visited
                    neighborCopy = Node(neighbor.val)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:  # if presen then append its value i.e as its copy is already created
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy  # return the 1st node like we were also given only the one reference node
        


# my mistakes: i got my mistake
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        Q= collections.deque()
        Q.append(node)
        copy= Node(node.val)
        clones= {}    # clone will contain the clone of each node
        clones[node]= copy
        while Q:
            curr= Q.popleft()
            clone_curr= clones[curr]
            for nei in curr.neighbors:
                if nei not in clones:
                    neiCopy= Node(nei.val)
                    clones[nei]= neiCopy
                    Q.append(nei)
                # clone_curr.neighbors.append(neiCopy)   # mistake: here we have to add clones[nei] if nei is already present but for both we are adding like this
                                                        # adding like this will only work if nei is not present in clones
                                                        # instead you can do add like the 
                clone_curr.neighbors.append(clones[nei])
        return copy


# Java
"""
// Method 1:

class Solution {
    public HashMap<Integer, Node> map = new HashMap<>();
    
    public Node cloneGraph(Node node) {
        return clone(node);
    }
    
    public Node clone(Node node) {
        if (node == null) return null;
        
        if (map.containsKey(node.val)) 
            return map.get(node.val);
        
        Node newNode = new Node(node.val, new ArrayList<Node>());
        map.put(newNode.val, newNode);
        for (Node neighbor : node.neighbors) 
            newNode.neighbors.add(clone(neighbor));
        return newNode;
    }
}
"""