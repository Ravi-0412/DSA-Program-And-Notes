"""
Question) You are given two lists:
i) all_files: A complete list of every file existing in a system.
ii) selected_files: A subset of files that a user has chosen.

Your goal is to represent the selected_files list as concisely as possible.
i)  The Rule: If all files within a specific directory (and its subdirectories) are selected, you must replace those individual files with the name of the directory itself.
ii) The Goal: Minimize the number of strings in the output.

Example 1
Input:
    All Files: [/a/a.txt, /a/b/a.txt, /a/b/b.txt, /a/c/z.txt]
    Selected: [/a/b/a.txt, /a/b/b.txt]
Logic:
Look at directory /a/b. It contains two files in the system (a.txt and b.txt). Since the user selected both, we don't list them individually.
Output: [/a/b]

Example 2

Input:
    All Files: [/a/1.txt, /a/2.txt]
    Selected: [/a/1.txt]
Logic:
Directory /a has two files, but only one is selected. We cannot consolidate because /a/2.txt is missing.
Output: [/a/1.txt]

Example 3: Partial Parent Consolidation (f1)

Input:
    All Files: [/a/a.txt, /a/b/a.txt, /a/b/b.txt, /a/c/z.txt, /a/c/k.txt]
    Selected: [/a/a.txt, /a/b/a.txt, /a/b/b.txt]
    
Logic:
    Check Root /a: It contains 5 files total. Only 3 are selected. Fail.
    Check /a/a.txt: It is a single file and it is selected. Keep as individual file.
    Check Directory /a/b: It contains 2 files (a.txt, b.txt). Both are selected. Consolidate to /a/b.
    Check Directory /a/c: It contains 2 files. Zero are selected. Ignore.

Output: [/a/a.txt, /a/b]

Example 4: Full System Collapse (f2)
Input:
    All Files: [/a/1.txt, /a/b/2.txt]
    Selected: [/a/1.txt, /a/b/2.txt]

Logic:
    Check Directory /a/b: It contains 1 file (2.txt). It is selected. At this moment, we could say /a/b.
    Check Directory /a: It contains 2 files total in the entire system (1.txt and the one inside /a/b). Both are selected.
    Since the parent directory /a is 100% complete, it "swallows" all children. Instead of listing the file and the subfolder, we just use the highest possible label.

Output: [/a]

Example 5: Genre-Based Consolidation (f3)

Input:
    All Files: [/movies/scifi/dune.mp4, /movies/scifi/starwars.mp4, /movies/romcom/nottinghill.mp4]
    Selected: [/movies/scifi/dune.mp4, /movies/scifi/starwars.mp4]

Logic:
    Check Directory /movies: It contains 3 movies total. Only 2 are selected. Fail.
    Check Directory /movies/scifi: It contains 2 movies (dune, starwars). Both are selected. Consolidate to /movies/scifi.
    Check Directory /movies/romcom: Contains 1 movie. Not selected. Ignore.

Output: [/movies/scifi]

Note : consolidation only happens when a directory is 100% complete. 
If even one tiny file in a deep sub-folder is missing from the selection, that directory (and all its parents) can no longer be consolidated.

Thought Process & Logic :

To solve this, we need a way to "count" how many files exist under any given path and compare it to how many were actually selected.
1. Use a Trie (Prefix Tree)
A Trie is perfect for hierarchical data. Each node represents a part of the path (e.g., a, b, a.txt).
2. Maintain Two Counts per Node
Every node in our Trie will track:
    total_count: Total number of leaf-node files that exist under this path in the entire system.
    selected_count: Total number of leaf-node files under this path that were selected.

3. The "Collapse" Condition

We perform a Pre-Order Traversal (Top-Down):
    If a node's selected_count is equal to its total_count (and it's greater than 0), it means everything under this folder is selected.
    Stop here. Add this directory path to our result. We don't need to look at the children because they are all included in this folder.
    If the counts don't match, we cannot consolidate this folder. We must go deeper into its children to see if their sub-folders can be consolidated.

Meaning of line :  parts = path.strip('/').split('/')
Operation	                            Result	                                                  Why?

Original	            "/movies/scifi/dune.mp4/"	                                            Raw input.
.strip('/')	                "movies/scifi/dune.mp4"	                              Removes the leading and trailing /.
.split('/')	          ['movies', 'scifi', 'dune.mp4']	                            Creates a clean list of "steps" for our Trie.

Time: O(N⋅L), where N is the number of files and L is the average length of the file path. We process each path three times (total count, selected count, and DFS).
Space: O(N⋅L) to store the Trie.
"""

import collections

class TrieNode:
    def __init__(self):
        # Maps directory/file name to its corresponding TrieNode object
        self.children = {}
        # total_count: tracks EVERY leaf-node file existing in this subtree
        self.total_count = 0
        # selected_count: tracks only SELECTED leaf-node files in this subtree
        self.selected_count = 0

class FileSystemConsolidator:
    def solve(self, all_files: list[str], selected_files: list[str]) -> list[str]:
        root = TrieNode()
        
        # 1. Build the system inventory
        self._build_inventory_trie(root, all_files)
        
        # 2. Mark the user's selections
        self._mark_selected_files(root, selected_files)
        
        # 3. Consolidate and return results
        results = []
        self._find_consolidated_paths(root, [], results)
        return results
        
    def _build_inventory_trie(self, root: TrieNode, all_files: list[str]):
        # --- PHASE 1: Build the System Inventory ---
        # We need to know the 'ground truth' of what files exist in which folders.
        for path in all_files:
            # strip('/') removes leading/trailing slashes to avoid empty string parts
            parts = path.strip('/').split('/')
            node = root
            for part in parts:
                if part not in node.children:
                    node.children[part] = TrieNode()
                node = node.children[part]
                # CRITICAL: As we move down the path to a file, every parent 
                # directory's total_count is incremented by 1.
                node.total_count += 1
    
    def _mark_selected_files(self, root: TrieNode, selected_files: list[str]):
        # --- PHASE 2: Mark User Selections ---
        # Now we overlay the user's choice onto our existing Trie.
        for path in selected_files:
            parts = path.strip('/').split('/')
            node = root
            for part in parts:
                # We move through the same nodes created in Phase 1
                node = node.children[part]
                # We increment the selected_count for every parent folder.
                # If a folder has 3 files and we pick 3, this count will eventually match total_count.
                node.selected_count += 1

    def _find_consolidated_paths(self, node: TrieNode, current_path: list[str], results: list[str]):
        """
        Recursive helper to find the highest possible consolidated directories.
        """
        # LOGIC: If the number of files we selected under this node matches
        # the total number of files that exist here, we found a "Full" folder.
        # total_count > 0 ensures we don't accidentally return empty root nodes.
        if node.total_count > 0 and node.total_count == node.selected_count:
            # We found a consolidation point! Add the path and STOP recursing.
            # Returning here prevents us from adding individual sub-files.
            results.append("/" + "/".join(current_path))
            return
        
        # If the directory is not "Full", it means some files were NOT selected.
        # We must dive deeper to see if any sub-directories within it ARE full.
        for name, child in node.children.items():
            self._find_consolidated_paths(child, current_path + [name], results)
        return results

# Verification Helper
def test_consolidation(all_files, selected_files, expected):
    sol = FileSystemConsolidator()
    actual = sorted(sol.solve(all_files, selected_files))
    print(f"All Files: {all_files}")
    print(f"Input Selected: {selected_files}")
    print(f"Output: {actual}")
    print(f"Status: {'✅ PASSED' if actual == sorted(expected) else '❌ FAILED'}")
    print("-" * 30)
    
# Case 1: The user's specific example
all_f1 = ["/a/a.txt", "/a/b/a.txt", "/a/b/b.txt", "/a/c/z.txt", "/a/c/k.txt"]
sel_f1 = ["/a/a.txt", "/a/b/a.txt", "/a/b/b.txt"]
exp_f1 = ["/a/a.txt", "/a/b"]
test_consolidation(all_f1, sel_f1, exp_f1)

# Case 2: Entire root directory selected
all_f2 = ["/a/1.txt", "/a/b/2.txt"]
sel_f2 = ["/a/1.txt", "/a/b/2.txt"]
exp_f2 = ["/a"]
test_consolidation(all_f2, sel_f2, exp_f2)

# Case 3: Nested consolidation and individual files
all_f3 = ["/movies/scifi/dune.mp4", "/movies/scifi/starwars.mp4", "/movies/romcom/nottinghill.mp4"]
sel_f3 = ["/movies/scifi/dune.mp4", "/movies/scifi/starwars.mp4"]
exp_f3 = ["/movies/scifi"]
test_consolidation(all_f3, sel_f3, exp_f3)


# Follow ups:
"""
Q) How to  optimized for a streaming input where you don't have the all_files list upfront? 

If we handle this as a stream, we change our strategy from a "Trie Construction" to a "Two-Pass Hash Counting" approach. 
This is much more memory-efficient and fits perfectly into a MapReduce or large-scale data processing pipeline.

🧠 Logic: The Hash-Prefix Strategy

Instead of building a physical tree of objects, we treat every file path as a series of prefixes.
    Pass 1 (The Inventory): Stream through all_files. For every file, generate all its parent directory prefixes (e.g., /a/b/c.txt → /a, /a/b). 
    Store the count of how many files exist under each prefix in a Hash Map.
    Pass 2 (The Selection): Stream through selected_files. Do the exact same thing—count how many selected files fall under each prefix.
    Pass 3 (The Consolidation): Iterate through the selected_files one last time. For each file, check its parent prefixes from the top down. 
    The first parent prefix where Selected Count == Total Count is your consolidated output.

Short: 
Prefix Generation: By using range(len(parts) - 1), we correctly identify that /a/b/c.txt has two parent directories: /a and /a/b.
Top-Down Search: In Pass 3, checking prefixes from shortest to longest ensures that if the whole system is selected, we return /a instead of /a/b, /a/c, etc.

Memory Efficiency: We are storing counts in a flat hash map rather than nested objects. For a huge file system with deep nesting, this is significantly lighter on memory.

Time and sapce same as above 
"""


import collections

class StreamingConsolidator:
    def consolidate(self, all_files_stream, selected_files_stream):
        """
        Main entry point that orchestrates the three-pass consolidation.
        """
        # Maps directory prefixes (e.g., "/a/b") to the number of files they contain.
        total_counts = collections.defaultdict(int)
        selected_counts = collections.defaultdict(int)
        
        # 1. Map out the entire system's directory structure
        self._count_all_files(all_files_stream, total_counts)
        
        # 2. Map out the user's selected files and keep a copy to iterate over
        selected_list = self._count_selected_files(selected_files_stream, selected_counts)
        
        # 3. Determine the most shrunken version of the output
        return self._generate_shrunken_paths(selected_list, total_counts, selected_counts)

    def _count_all_files(self, stream, total_counts):
        """Pass 1: Counts how many total files exist in every possible directory."""
        for path in stream:
            parts = path.strip('/').split('/')
            prefix = ""
            # We iterate through all parts except the last one (the file itself)
            # to build directory prefixes.
            for i in range(len(parts) - 1):
                prefix += "/" + parts[i]
                total_counts[prefix] += 1

    def _count_selected_files(self, stream, selected_counts):
        """Pass 2: Counts how many selected files fall into each directory."""
        selected_list = []
        for path in stream:
            selected_list.append(path)
            parts = path.strip('/').split('/')
            prefix = ""
            for i in range(len(parts) - 1):
                prefix += "/" + parts[i]
                selected_counts[prefix] += 1
        return selected_list

    def _generate_shrunken_paths(self, selected_list, total_counts, selected_counts):
        """Pass 3: Finds the highest 'Full' directory for each selected file."""
        results = set()
        
        for path in selected_list:
            parts = path.strip('/').split('/')
            prefix = ""
            consolidated = False
            
            # Check prefixes from the TOP-DOWN (e.g., check '/a' before '/a/b')
            # This ensures we find the highest possible consolidation point first.
            for i in range(len(parts) - 1):
                prefix += "/" + parts[i]
                
                # If total files in the system matches user's selected files at this prefix
                if total_counts[prefix] > 0 and total_counts[prefix] == selected_counts[prefix]:
                    results.add(prefix)
                    consolidated = True
                    break # Stop looking deeper; this folder covers everything below it
            
            # If no parent directory was 100% full, we must include the individual file
            if not consolidated:
                results.add(path)
                
        return sorted(list(results))

# --- Verification ---
all_f = ["/a/a.txt", "/a/b/a.txt", "/a/b/b.txt", "/a/c/z.txt", "/a/c/k.txt"]
sel_f = ["/a/a.txt", "/a/b/a.txt", "/a/b/b.txt"]

sol = StreamingConsolidator()
print(sol.consolidate(all_f, sel_f))
# Logic Trace:
# '/a/a.txt' -> parent '/a' is 3/5 (Not Full). Result adds: '/a/a.txt'
# '/a/b/a.txt' -> parent '/a' (Not Full), parent '/a/b' is 2/2 (FULL). Result adds: '/a/b'
# Output: ['/a/a.txt', '/a/b']
