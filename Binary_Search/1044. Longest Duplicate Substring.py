# This is exactly same as "1062. Longest Repeating Substring", only difference is
# we need to solve this questiob in better time complexity than O(n^2) either in O(n*logn) or O(n).

# Optimised one : Using Binary Search + Robin-Karp rolling hash method 
# Time: O(n*logn)
"""
Complexity Analysis:

Binary Search in range 1 and N, so it's O(logN)
Rolling hash : O(N)

Overall Time: O(NlogN)
Space: O(N)
"""

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        
        # Base value for the rolling hash
        base = 26  # As we're dealing with lowercase English letters
        mod = 2**63 - 1  # Large prime modulus to prevent overflow
        
        def search(L):
            """
            Search for a duplicate substring of length L using the Rabin-Karp rolling hash method.
            If a duplicate substring of length L is found, return that substring.
            If no duplicate is found, return None.
            """
            
            current_hash = 0  # Initialize the rolling hash for the current substring
            baseL = pow(base, L, mod)  # Precompute base^L % mod to use for rolling hash updates

            # Dictionary to store the hashes of substrings we've seen along with their starting indices
            seen_hashes = {}
            
            # Step 1: Compute the hash for the first substring of length L
            for i in range(L):
                # Update the current hash based on the character at position i
                current_hash = (current_hash * base + ord(s[i]) - ord('a')) % mod
            
            # Store the hash of the first substring along with its starting index (0)
            seen_hashes[current_hash] = [0]  # The first substring starts at index 0

            # Step 2: Use a sliding window to compute the hash for all subsequent substrings of length L
            for i in range(1, n - L + 1):
                # Update the rolling hash:
                # 1. Remove the effect of the character that is sliding out of the window
                # 2. Add the effect of the new character that is entering the window
                current_hash = (current_hash * base + ord(s[i + L - 1]) - ord('a')) % mod  # Add the new character
                current_hash = (current_hash - (ord(s[i - 1]) - ord('a')) * baseL) % mod  # Remove the old character

                # Step 3: Check if this hash has been seen before
                if current_hash in seen_hashes:
                    # If the hash is found, check the actual substrings to avoid collisions
                    for start_index in seen_hashes[current_hash]:
                        # Compare the actual substrings to confirm a duplicate
                        if s[start_index:start_index + L] == s[i:i + L]:
                            # If they match, we've found a duplicate substring
                            return s[i:i + L]
                
                # If this hash has not been seen, store it along with the starting index
                seen_hashes.setdefault(current_hash, []).append(i)
            
            # If no duplicate substring of length L is found, return None
            return None
        
        # Binary search for the length of the longest duplicate substring
        low, high = 1, n
        result = ""
        
        while low <= high:
            mid = (low + high) // 2
            dup_substr = search(mid)
            
            if dup_substr:
                result = dup_substr  # Found a valid duplicate substring of length mid
                low = mid + 1  # Try for longer length
            else:
                high = mid - 1  # Try for shorter length
        
        return result

