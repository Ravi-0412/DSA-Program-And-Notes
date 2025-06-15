# method 1: 
# using DFS+ hashmap
# logic: since we have to copy the node so we have to store somewhere so that we can use that again and again
# and for this only one data structure comes into mind 'hashmap'
# and for traversal, we have to use either BFS or DFS

"""
Stepwise
1. We must create a new copy of every node and all its neighbors.
2. Graphs can have cycles or shared neighbors, so we need to avoid cloning the same node more than once.
3. To handle this, we use a hashmap:
   - It keeps track of already cloned nodes.
   - It prevents re-cloning and avoids infinite loops.
# and for traversal, we have to use either BFS or DFS

We use Depth-First Search (DFS) to go through the graph:
- If a node hasn’t been cloned:
  - Clone it and store it in the hashmap.
  - Recursively clone all of its neighbors.
- If it’s already cloned, just return it from the hashmap.
"""
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

# Java Code 
"""
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;

    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }

    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }

    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    // to store the copy of the node
    private Map<Node, Node> oldToNew = new HashMap<>();

    public Node cloneGraph(Node node) {
        return node != null ? clone(node) : null;
    }

    // go to each node and create its copy if not present and then add all its neighbors
    // to the 'neighbors list of copied node' seeing its adjacent from the original node
    private Node clone(Node node) {
        // base case
        if (oldToNew.containsKey(node)) {
            return oldToNew.get(node);
        }

        // if not present then create the copy 
        Node copy = new Node(node.val);
        oldToNew.put(node, copy);

        // now add all its neighbors to the 'neighbors' list
        for (Node nei : node.neighbors) {
            copy.neighbors.add(clone(nei));
        }

        return copy;
    }
}

"""

# C++ Code 
"""
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        unordered_map<Node*, Node*> oldToNew;  // to store the copy of the node

        // go to each node and create its copy if not present and then add all its neighbors
        // to the 'neighbors list of copied node' seeing its adjacent from the original node
        function<Node*(Node*)> clone = [&](Node* node) -> Node* {
            // base case
            if (oldToNew.count(node)) {
                return oldToNew[node];
            }
            // if not present then create the copy 
            Node* copy = new Node(node->val);
            oldToNew[node] = copy;
            // now add all its neighbors to the 'neighbors' list
            for (Node* nei : node->neighbors) {
                copy->neighbors.push_back(clone(nei));
            }
            return copy;
        };

        return node ? clone(node) : nullptr;
    }
};

"""
# method 2: 
# using BFS , same logic as DFS

# my mistakes: 
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
    

    
# Corrected solution 
"""
We make a copy of every node once and rebuild all its
connections using BFS and a dictionary to avoid repeating work.

Steps:
1) If the input node a is None:
 → Return None (empty graph case).
2) Create a copy of node a, name it aCopy.
3) Initialize a dictionary copyMap to store original → cloned node:
 → copyMap[a] = aCopy
4) Create a queue q for BFS, and enqueue node a.
5) While the queue q is not empty:
    a. Remove the front node from q, call it curr.
    b. For each neighbor nei of curr:
     i. If nei is not in copyMap:
         → This means nei hasn't been visited (copied) yet.
         ii. Create a copy of nei, name it neiCopy.
         iii. Add neiCopy to copyMap:
             → copyMap[nei] = neiCopy
         iv. Connect neiCopy to the clone of curr:
             → copyMap[curr].neighbors.append(neiCopy)
         v. Enqueue original neighbor nei to visit later.
     vi. Else (if nei is already in copyMap):
         → Just connect its copy to curr's copy:
         → copyMap[curr].neighbors.append(copyMap[nei])
6) After the BFS is done:
 → Return aCopy (the clone of the starting node).


Time Complexity: O(N + E)
Space Complexity: O(N)
N = number of nodes
E = number of edges
Each node and edge is processed once, because it's a normal bfs
"""
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
        

# Java
"""
class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) return null;
        
        Map<Node, Node> map = new HashMap<>();
        Node nodeCopy = new Node(node.val);
        map.put(node, nodeCopy);

        Queue<Node> queue = new LinkedList<>();
        queue.offer(node);

        while (!queue.isEmpty()) {
            Node curr = queue.poll();
            for (Node neighbor : curr.neighbors) {
                if (!map.containsKey(neighbor)) {
                    Node neighborCopy = new Node(neighbor.val);
                    map.put(neighbor, neighborCopy);
                    queue.offer(neighbor);
                }
                map.get(curr).neighbors.add(map.get(neighbor));
            }
        }

        return nodeCopy;
    }
}
"""



# Java Code 
"""
class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) return null;

        Node nodeCopy = new Node(node.val);
        Map<Node, Node> map = new HashMap<>(); // will contain the clone(copy) of each node
        map.put(node, nodeCopy);

        Queue<Node> queue = new LinkedList<>();
        queue.add(node);

        while (!queue.isEmpty()) {
            Node curr = queue.poll();
            // now go to adjacent node and add as its neighbor by copying
            for (Node neighbor : curr.neighbors) {
                if (!map.containsKey(neighbor)) { // neighbor is not visited
                    Node neighborCopy = new Node(neighbor.val);
                    map.put(neighbor, neighborCopy);
                    map.get(curr).neighbors.add(neighborCopy);
                    queue.add(neighbor);
                } else { // if present then append its value i.e. as its copy is already created
                    map.get(curr).neighbors.add(map.get(neighbor));
                }
            }
        }

        return nodeCopy; // return the 1st node like we were also given only the one reference node
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node == nullptr) return nullptr;

        Node* nodeCopy = new Node(node->val);
        unordered_map<Node*, Node*> map; // will contain the clone(copy) of each node
        map[node] = nodeCopy;

        queue<Node*> q;
        q.push(node);

        while (!q.empty()) {
            Node* curr = q.front();
            q.pop();

            // now go to adjacent node and add as its neighbor by copying
            for (Node* neighbor : curr->neighbors) {
                if (map.find(neighbor) == map.end()) { // neighbor is not visited
                    Node* neighborCopy = new Node(neighbor->val);
                    map[neighbor] = neighborCopy;
                    map[curr]->neighbors.push_back(neighborCopy);
                    q.push(neighbor);
                } else { // if present then append its value i.e. as its copy is already created
                    map[curr]->neighbors.push_back(map[neighbor]);
                }
            }
        }

        return nodeCopy; // return the 1st node like we were also given only the one reference node
    }
};
"""