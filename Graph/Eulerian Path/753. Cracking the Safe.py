# Logic: https://1drv.ms/o/c/2e0ac565ff6aeb82/IgC20s4qd35MTaU9V9Tzi1u0AYecoT4d1-sYC5x2BOWNfh8

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        # The number of edges (passwords) we need to visit is k^n
        visited = set()
        result = []
        
        # We start with a node of length n-1
        start_node = "0" * (n - 1)
        
        def dfs(node):
            # Iterating in reverse (k-1 to 0) is a common trick for 
            # Hierholzer's to ensure the path builds correctly in post-order
            for i in range(k - 1, -1, -1):
                digit = str(i)
                # The full 'password' is the current node + the new digit
                edge = node + digit
                if edge not in visited:
                    visited.add(edge)
                    # The next node is the last n-1 characters of the edge
                    # If n=1, the next node is just an empty string ""
                    dfs(edge[1:] if n > 1 else "")
                    # Append to result in post-order
                    result.append(digit)

        dfs(start_node)
        
        # The result is the starting node prefix + the sequence of edges visited
        return "".join(result) + start_node   # adding start node at last because in result node are added in postorder 
                                              # add at last only to get the correct sequence


# My mistake and very important thing to keep in mind :
"""
Always traverse in reverse way in case of 'Eulerian cycle' otherwise you will get wrong answer.

Mine approach that didn't work;
n = 3, k = 2
output : "0000111010" , expected : "0011101000"

Reason: 
for x in map(str, range(k)):

We were traversing from start but in Eulerin always traverse in reverse order.

code:

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        # This set keeps track of which length-n combinations (edges)
        # we have already used in our traversal.
        visited = set()
        
        # This will store digits in reverse order (due to postorder DFS).
        result = []
        
        # Starting node: string of length (n-1)
        # Example: if n=3 -> start = "00"
        # This represents our initial graph node.
        start = "0" * (n - 1)
        
        # DFS function to perform Hierholzer's algorithm
        def dfs(node):
            # Try appending every possible digit (0 to k-1), traversing each digit in range(k) as string.
            for x in map(str, range(k)):
                
                # Create a candidate edge (length n string)
                # Example: node="00", x="1" -> edge="001"
                edge = node + x
                a
                # If this password (edge) is not used yet
                if edge not in visited:
                    
                    # Mark this length-n combination as used
                    visited.add(edge)
                    
                    # Move to next node:
                    # Drop first char and keep last (n-1) chars
                    # Example: "001" -> next node = "01"
                    dfs(edge[1:])
                    
                    # Append digit AFTER exploring deeper
                    # This is postorder — crucial for Eulerian cycle
                    result.append(x)
        
        # Start DFS from initial node
        dfs(start)
        
        # Final string = starting node + collected digits
        return start + ''.join(result)
"""

