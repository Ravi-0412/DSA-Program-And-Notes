
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
    public Node cloneGraph(Node node) {
        if (node == null) {
            return node;
        }

        Queue<Node> Q = new LinkedList<>();
        Q.add(node);
        Node copy = new Node(node.val);

        // clones will contain the clone of each node
        Map<Node, Node> clones = new HashMap<>();
        clones.put(node, copy);

        while (!Q.isEmpty()) {
            Node curr = Q.poll();
            Node clone_curr = clones.get(curr);

            for (Node nei : curr.neighbors) {
                if (!clones.containsKey(nei)) {
                    Node neiCopy = new Node(nei.val);
                    clones.put(nei, neiCopy);
                    Q.add(nei);
                }
                // clone_curr.neighbors.append(neiCopy)   // mistake: here we have to add clones[nei] if nei is already present but for both we are adding like this
                // adding like this will only work if nei is not present in clones
                // instead you can do add like the 
                clone_curr.neighbors.add(clones.get(nei));
            }
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
        if (!node) return node;

        queue<Node*> Q;
        Q.push(node);

        // clone will contain the clone of each node
        unordered_map<Node*, Node*> clones;

        Node* copy = new Node(node->val);
        clones[node] = copy;

        while (!Q.empty()) {
            Node* curr = Q.front();
            Q.pop();

            Node* clone_curr = clones[curr];

            for (Node* nei : curr->neighbors) {
                if (clones.find(nei) == clones.end()) {
                    Node* neiCopy = new Node(nei->val);
                    clones[nei] = neiCopy;
                    Q.push(nei);
                }

                // clone_curr->neighbors.push_back(neiCopy); // mistake: this only works when neiCopy was just created
                clone_curr->neighbors.push_back(clones[nei]);  // correct: always use clones[nei]
            }
        }

        return copy;
    }
};

"""