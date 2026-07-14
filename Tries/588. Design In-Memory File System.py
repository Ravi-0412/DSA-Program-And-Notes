"""
Complexity Analysis:

Let K be the number of components (tokens) in the path, and $L$ be the length of a component name string.
1) mkdir / addContentToFile / readContentFromFile: O(K * L)
2) ls : O(K * L + N *log N)
"""

# Just a TrieNode with suitable variables
class FileNode:
    def __init__(self):
        # map: string (name) -> FileNode (child)
        self.children = {}
        # Flag to distinguish between a directory node and a file node
        self.is_file = False
        # Holds file contents; remains empty string for directories
        self.content = ""

class FileSystem:
    def __init__(self):
        # Initialize the file system with a root directory node
        self.root = FileNode()

    def _parse_path(self, path: str) -> list:
        # Helper to split absolute path into individual directory/file tokens
        # e.g., "/a/b/c" -> ["a", "b", "c"]
        if path == "/":
            return []
        return [token for token in path.split("/") if token]

    def _traverse_to_node(self, path: str) -> FileNode:
        # Helper to navigate from root to the destination node specified by the path
        curr = self.root
        tokens = self._parse_path(path)
        for token in tokens:
            curr = curr.children[token]
        return curr

    def ls(self, path: str) -> list:
        # Step 1: Navigate to the specified target node
        curr = self._traverse_to_node(path)
        
        # Condition A: If the target is a file, return a list containing only its name
        if curr.is_file:
            # The file name is the last token of our absolute path
            return [path.split("/")[-1]]
            
        # Condition B: If target is a directory, return all child names sorted lexicographically
        return sorted(curr.children.keys())

    def mkdir(self, path: str) -> None:
        curr = self.root
        tokens = self._parse_path(path)
        
        # Step down through tokens, creating missing directory nodes along the way
        for token in tokens:
            if token not in curr.children:
                curr.children[token] = FileNode()
            curr = curr.children[token]

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.root
        tokens = self._parse_path(filePath)
        
        # Traverse up to the parent directory of the file
        for token in tokens[:-1]:
            curr = curr.children[token]
            
        # The final token is our file name
        file_name = tokens[-1]
        
        # If the file node doesn't exist under this directory yet, create it
        if file_name not in curr.children:
            curr.children[file_name] = FileNode()
            curr.children[file_name].is_file = True
            
        # Move into the file node and append the text content
        curr = curr.children[file_name]
        curr.content += content

    def readContentFromFile(self, filePath: str) -> str:
        # Navigate directly to the file node and extract its text content
        node = self._traverse_to_node(filePath)
        return node.content
