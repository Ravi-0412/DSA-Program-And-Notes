# Method 1:
"""
Since the first group is the only one allowed to be shorter than k, 
starting from the end ensures that every group we build (except potentially the last one we process) satisfies the length k requirement.
"""

def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Remove dashes and uppercase everything
        s = s.replace("-", "").upper()
        n = len(s)
        res = []
        
        # Iterate backwards through the cleaned string
        # Using reversed() or slicing s[::-1]
        for i in range(len(s) - 1, -1, -1):
            res.append(s[i])
            # After every k characters, if we aren't at the very start, add a dash
            if (n - i) % k == 0 and i != 0:
                res.append("-")
                
        # Reverse the result back to the correct order
        return "".join(res[::-1])

# Method 2:
def licenseKeyFormatting(s: str, k: int) -> str:
    # Step 1: Remove existing dashes and convert to uppercase
    # We only care about the alphanumeric characters
    clean_s = s.replace("-", "").upper()
    
    n = len(clean_s)
    if n == 0:
        return ""
    
    # Step 2: Determine the length of the first group
    # The first group's length is n % k. If n % k == 0, the first group is k.
    first_group_len = n % k if n % k != 0 else k
    
    res = []
    
    # Add the first group
    res.append(clean_s[:first_group_len])
    
    # Add subsequent groups of size k
    for i in range(first_group_len, n, k):
        res.append(clean_s[i:i + k])
        
    # Join groups with dashes
    return "-".join(res)
