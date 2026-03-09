"""
To understand the logic, translate the string components into Graph Theory terms:
    Nodes (Vertices): Each unique key in your map (e.g., USER, HOME, ROOT).
    Edges (Connections): If the value of %ROOT% contains %HOME%, there is a directed edge from ROOT to HOME.
    Leaf Nodes: Keys that have no placeholders in their values (e.g., USER: "admin"). These are your stopping points.

 The Logic: DFS with Memoization
 The code uses Recursion, which is simply a Depth-First Search (DFS) traversal of this graph.
 1. Traversal (The Search):
     When you encounter %ROOT%, you can't solve it yet. You must "visit" its neighbor, %HOME%.
     From %HOME%, you see you need %USER%.You keep going deeper until you hit a Leaf Node (admin).
2. Backtracking (The Resolution): Once USER is resolved to admin, you carry that value back up to HOME.
    Now HOME can finish its own resolution (/admin/home) and pass it up to ROOT.
3. Memoization (The Shortcut):
    In a graph, multiple nodes might point to the same child.
    Instead of re-traversing the same "sub-graph" every time, we store the result in a memo dictionary. 
    This turns an exponential problem into a linear O(V + E) one.
⚠️ 3. Cycle Detection (The Guardrail)
In a graph, if A points to B and B points back to A, a simple DFS will spin forever (Infinite Loop).
The visiting set: This tracks the "current path."If you are currently trying to solve A, and while doing so you are asked to solve A again, you’ve detected a Cycle.
The code immediately returns CIRCULAR_ERROR to prevent a crash.
"""

# --- Implementation 1: Regex Version ---

import re
import collections

def transform_regex(input_str, mapping):
    """
    Main function to replace placeholders like %KEY% with values from a map.
    Handles nested placeholders and prevents infinite loops.
    """
    # memo: Stores results of keys we've already solved (e.g., %HOME% -> /admin/home)
    # This ensures we don't re-process the same key multiple times (Efficiency).
    memo = {}
    
    # visiting: Tracks the keys we are currently resolving in the recursion stack.
    # If we encounter a key already in 'visiting', we found a loop (Safety).
    visiting = set()

    def resolve_key(key):
        # 1. If we solved this key before, return the saved result immediately
        if key in memo:
            return memo[key]
        
        # 2. Cycle Detection: If key is already in our 'visiting' path, it's a loop
        if key in visiting:
            return "CIRCULAR_ERROR"
        
        # Mark this key as "being processed"
        visiting.add(key)
        
        # 3. Look up the value in the map. 
        # mapping.get(key, default) returns the value if it exists, 
        # else it keeps the placeholder as is (e.g., %MISSING_KEY%).
        raw_val = mapping.get(key, f"%{key}%")
        
        # 4. RECURSIVE ENGINE:
        # Search inside the 'raw_val' for nested placeholders.
        # Example: if raw_val is "/%USER%/home", this finds "%USER%".
        # Lambda 'm' is the match found; m.group(1) is the inner text 'USER'.
        resolved_val = re.sub(
            r'%(.*?)%', 
            lambda m: resolve_key(m.group(1)), 
            raw_val
        )
        
        # 5. Cleanup and Cache:
        # Remove from 'visiting' (backtracking) and save result in 'memo'.
        visiting.remove(key)
        memo[key] = resolved_val
        return resolved_val

    # STARTING POINT:
    # Scan the main input string for any placeholders and trigger the resolution
    return re.sub(
    r'%(.*?)%',                         # 1. The Pattern
    lambda m: resolve_key(m.group(1)),  # 2. The Logic
    input_str                           # 3. The Target
)

# Time Complexity: O(N + M) where N is input length, M is map content.
# Space Complexity: O(M) for memoization and recursion stack depth.

# --- Implementation 2: Non-Regex Version ---
def transform_no_regex(input_str, mapping):
    # memo: Cache for fully resolved strings to avoid redundant work
    memo = {}
    
    def resolve(val, visiting):
        # Base Case: If string contains no placeholders, it's already resolved
        if "%" not in val:
            return val
        
        result = [] # List to build the final string efficiently
        i = 0
        while i < len(val):
            # Check for the start of a placeholder
            if val[i] == "%":
                start = i
                # Look for the closing '%'
                end = val.find("%", start + 1)
                
                # If a pair of '%' is found, try to resolve the key inside
                if end != -1:
                    key = val[start + 1 : end]
                    
                    # 1. Cycle Detection: Check if we are currently resolving this key
                    if key in visiting:
                        return "CIRCULAR_ERROR"
                    
                    # 2. Memoization: If not already solved, resolve it now
                    if key not in memo:
                        visiting.add(key)
                        # Get raw value from map; if missing, keep placeholder text
                        raw_val = mapping.get(key, f"%{key}%")
                        # Recursively resolve any nested placeholders in the value
                        memo[key] = resolve(raw_val, visiting)
                        visiting.remove(key) # Backtrack: remove from visiting set
                    
                    # Append the fully resolved value to our result
                    result.append(memo[key])
                    # Jump pointer past the closing '%'
                    i = end + 1
                    continue
            
            # If current character is not part of a valid %...%, append as is
            result.append(val[i])
            i += 1
            
        return "".join(result)

    # Start the recursive process with an empty 'visiting' set
    return resolve(input_str, set())

# --- Test Runner ---
test_cases = [
    {
        "name": "Basic Case",
        "map": {"USER": "admin"},
        "input": "Hello %USER%!"
    },
    {
        "name": "Nested Dependencies",
        "map": {"USER": "admin", "HOME": "/%USER%/home", "ROOT": "%HOME%/bin"},
        "input": "Path: %ROOT%"
    },
    {
        "name": "Multiple Different Keys",
        "map": {"A": "1", "B": "2", "C": "3"},
        "input": "%A%+%B%=%C%"
    },
    {
        "name": "Missing Key (Keep Placeholder)",
        "map": {"EXIST": "found"},
        "input": "%EXIST% and %MISSING%"
    },
    {
        "name": "Circular Dependency (Cycle)",
        "map": {"A": "%B%", "B": "%A%"},
        "input": "Infinite %A%"
    },
    {
        "name": "Deeply Nested",
        "map": {"A": "%B%", "B": "%C%", "C": "%D%", "D": "DeepValue"},
        "input": "Result: %A%"
    },
    {
        "name": "Text Touching Placeholder",
        "map": {"FILE": "report"},
        "input": "See_/%FILE%_now.doc"
    }
]

# This line prints the top labels of our table.
# <25 and <30 are "Format Specifiers". 
# They mean: "Reserve 25 (or 30) spaces and align the text to the left (<)".
# This ensures the columns stay perfectly lined up.
print(f"{'Test Name':<25} | {'Regex Output':<30} | {'Non-Regex Output'}")

# Prints a dashed line to separate the header from the actual data rows.
print("-" * 85)

# We loop through each 'test case' dictionary in our list.
for case in test_cases:
    
    # Run the Regex version of the logic using the input and map from the test case.
    res_reg = transform_regex(case["input"], case["map"])
    
    # Run the Non-Regex version with the same data to compare the results.
    res_no_reg = transform_no_regex(case["input"], case["map"])
    
    # Print the results in the same aligned format as the header.
    # case['name'] fits in the 25-space slot, res_reg fits in the 30-space slot.
    print(f"{case['name']:<25} | {res_reg:<30} | {res_no_reg}")
