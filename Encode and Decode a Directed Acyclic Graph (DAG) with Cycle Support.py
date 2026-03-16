"""
Question) You are tasked with designing a mechanism to encode and decode a Directed Acyclic Graph (DAG). 
This involves representing the graph in a format that can be easily stored or transmitted, and then reconstructing it.
As a follow-up, consider how your solution would adapt to include cycles in the graph, representing the cycle information accurately during encoding and decoding.

Ans : 
1. Encoding (Flattening the Graph)
The goal is to turn a "web" of objects into a single string.
Discovery: We use BFS to find every node. To avoid getting stuck in cycles, we use the node_to_id dictionary. 
If we see a node that is already in that dictionary, we don't add it to the queue again.

ID Assignment: We assign simple integers (0, 1, 2...) as IDs. This is much cleaner than memory addresses.

Adjacency Mapping: For every node, we look at its neighbors and record their assigned IDs instead of the objects themselves.

2. Decoding (Rebuilding the Graph)
Reconstruction requires two passes because of cycles and forward references (where Node 0 points to Node 5, but Node 5 hasn't been "created" yet).

Pass 1 (The Factory): We loop through the string and create every Node object. At this stage, their neighbors lists are empty. We store them in nodes_map (e.g., {"0": NodeObject}).

Pass 2 (The Wiring): We loop through the string again. For each node, we look at the neighbor IDs, fetch the corresponding Node objects from our nodes_map, 
and append them to the current node's neighbors list.

How it Handles Cycles
Cycles are handled naturally by the Two-Pass Decoding strategy:

In a cycle (e.g., A → B → A), when you are trying to link B back to A, the object for A must already exist.

If you tried to do this in one pass, you'd be stuck: "I can't finish B because I need A, but I can't finish A because it needs B."

By creating all objects first in Pass 1, Pass 2 simply connects existing "dots."

Complexity Analysis:
Time Complexity: O(V + E)$Encoding: We visit every vertex (V) once via BFS and iterate over every edge (E) once to build the neighbor ID strings. Total: O(V + E).
Decoding: We split the string and iterate over all records to create nodes (V), then iterate again to link all edges (E). Total: O(V + E).
Space Complexity: O(V)
Encoding: We store every node in node_to_id and nodes_ordered. Total: O(V).
Decoding: We store every node in the nodes_map. Total: O(V).
"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        # Neighbors are stored as a list of Node objects
        self.neighbors = neighbors if neighbors is not None else []

class Codec:
    def encode(self, root: 'Node') -> str:
        """
        Serializes a graph into a string format: ID:Value:NeighborIDs#...
        Uses a manual counter to keep IDs clean and readable (0, 1, 2...).
        """
        if not root:
            return ""
        
        # node_to_id: Maps a Node object to a unique integer ID
        node_to_id = {}
        # nodes_ordered: Keeps a list of nodes in the order they were discovered
        nodes_ordered = []
        
        # 1. DISCOVERY PHASE: Use BFS to find all nodes and assign IDs
        queue = [root]
        node_to_id[root] = 0
        nodes_ordered.append(root)
        
        # We use a pointer (head) to iterate through the list as a queue
        head = 0
        while head < len(nodes_ordered):
            curr = nodes_ordered[head]
            head += 1
            
            for neighbor in curr.neighbors:
                # If we haven't seen this node before, assign it the next available ID
                if neighbor not in node_to_id:
                    node_to_id[neighbor] = len(node_to_id)
                    nodes_ordered.append(neighbor)
        
        # 2. SERIALIZATION PHASE: Convert the discovered nodes into a string
        serialized_nodes = []
        for node in nodes_ordered:
            curr_id = node_to_id[node]
            val = node.val
            # Convert the list of neighbor objects into a string of their assigned IDs
            neighbor_ids = " ".join(str(node_to_id[n]) for n in node.neighbors)
            
            # Format pattern: "ID:Value:SpaceSeparatedNeighborIDs"
            serialized_nodes.append(f"{curr_id}:{val}:{neighbor_ids}")
            
        # Join all node records with a '#' separator
        return "#".join(serialized_nodes)

    def decode(self, data: str) -> 'Node':
        """
        Reconstructs the graph from the serialized string.
        Uses a two-pass approach to handle forward references and cycles.
        """
        if not data:
            return None
        
        # Split the string back into individual node records
        node_records = data.split("#")
        # nodes_map: Stores {ID_String: Node_Object} for quick linking
        nodes_map = {}
        
        # PASS 1: Create all Node instances
        # We must create all nodes first so that when we link neighbors, 
        # the target node already exists in memory.
        for record in node_records:
            node_id, val, _ = record.split(":")
            nodes_map[node_id] = Node(int(val))
            
        # PASS 2: Establish the neighbor connections (Edges)
        for record in node_records:
            node_id, _, neighbors_str = record.split(":")
            # If the node has neighbors, link the objects from our map
            if neighbors_str:
                for n_id in neighbors_str.split():
                    # This correctly handles cycles because the objects already exist
                    nodes_map[node_id].neighbors.append(nodes_map[n_id])
        
        # By convention, the first node in our encoded string was the root
        first_node_id = node_records[0].split(":")[0]
        return nodes_map[first_node_id]
    
def test_graph_codec():
    codec = Codec()

    # --- Case 1: Single Node ---
    # root1 (val: 5)
    root1 = Node(5)
    
    print("Test 1: Single Node")
    encoded1 = codec.encode(root1)
    print(f"Encoded: {encoded1}")
    decoded1 = codec.decode(encoded1)
    assert decoded1.val == 5 and len(decoded1.neighbors) == 0
    print("Result: Success\n")


    # --- Case 2: Directed Acyclic Graph (DAG) ---
    # 0 (val: 1) -> 1 (val: 2), 2 (val: 3)
    # 1 (val: 2) -> 2 (val: 3)
    node_a = Node(1)
    node_b = Node(2)
    node_c = Node(3)
    node_a.neighbors = [node_b, node_c]
    node_b.neighbors = [node_c]
    
    print("Test 2: DAG (V-shape with shared child)")
    encoded2 = codec.encode(node_a)
    print(f"Encoded: {encoded2}")
    decoded2 = codec.decode(encoded2)
    # Verify structure: Node 0 has 2 neighbors, Node 1 has 1 neighbor
    assert decoded2.val == 1
    assert len(decoded2.neighbors) == 2
    assert decoded2.neighbors[0].neighbors[0] == decoded2.neighbors[1]
    print("Result: Success\n")


    # --- Case 3: Graph with Cycles ---
    # 0 (val: 10) -> 1 (val: 20)
    # 1 (val: 20) -> 0 (val: 10)
    node_x = Node(10)
    node_y = Node(20)
    node_x.neighbors = [node_y]
    node_y.neighbors = [node_x]
    
    print("Test 3: Cyclic Graph (A <-> B)")
    encoded3 = codec.encode(node_x)
    print(f"Encoded: {encoded3}")
    decoded3 = codec.decode(encoded3)
    # Verify cycle: The neighbor of the neighbor should be the root itself
    assert decoded3.val == 10
    assert decoded3.neighbors[0].val == 20
    assert decoded3.neighbors[0].neighbors[0] == decoded3
    print("Result: Success (Cycle maintained)\n")

# Run the tests
if __name__ == "__main__":
    test_graph_codec()
