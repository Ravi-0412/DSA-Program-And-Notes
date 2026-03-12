""""
To optimize for shorter strings, we use an approach similar to counting in base-26, but with a "validator" for the threshold T.
1. State Tracking: We need to keep track of the "current" string being generated.
2. Incremental Logic:
    Start with string a.
    For each new request, try to "increment" the last character (e.g., a -> b).
    If a character reaches z, it "carries over" to the left, similar to how 9→10 in decimal.
    If we can't increment any further (e.g., zz), we increase the length (e.g., aaa).
3. Constraint Validation: Before returning a string, we check if any character count exceeds T. If it does, we skip that string and move to the next one.

Complexity Analysis
    Time Complexity (per call):
        Average: O(L), where L is the length of the string.
        Worst Case: If many strings are invalid, we might skip several candidates. However, with the "Skip Logic" mentioned above, we can guarantee finding the next valid string in nearly O(L) time.
    Space Complexity: O(L) to store the current character array. This is extremely efficient as we don't store previously generated strings.
"""

from collections import Counter

class URLShortener:
    def __init__(self, threshold: int):
        """
        Thought Process:
        We treat the string generation like a base-26 counter (a-z).
        To ensure we return shorter strings first, we start with length 1
        and only increase length once all permutations of the current length 
        are exhausted.
        """
        self.threshold = threshold
        # Using a list of chars allows O(1) modification of specific indices
        self.current_chars = ['a'] 

    def _is_valid(self, s_list: list) -> bool:
        """
        Validation Logic:
        Frequency check: No character can appear more than 'threshold' times.
        O(L) time complexity where L is the current string length.
        """
        counts = Counter(s_list)
        return all(count <= self.threshold for count in counts.values())

    def getNext(self) -> str:
        """
        Main Generator Loop:
        Lazily finds the next valid string. If a string fails the threshold 
        check, it increments and tries the next one immediately.
        """
        while True:
            candidate = "".join(self.current_chars)
            
            # 1. Capture the current string if it satisfies constraints
            valid_to_return = None
            if self._is_valid(self.current_chars):
                valid_to_return = candidate
            
            # 2. Always prepare the state for the 'next' call
            # This moves the pointer forward like a clock: 'aba' -> 'abb'
            self._increment()
            
            # 3. If the captured candidate was valid, return it.
            # Otherwise, the 'while True' loop continues to the next increment.
            if valid_to_return:
                return valid_to_return

    def _increment(self):
        """
        State Transition Logic (Base-26 Increment):
        1. Start from the rightmost character.
        2. If it's less than 'z', increment it and we are done.
        3. If it's 'z', reset it to 'a' and carry the +1 to the left (loop).
        4. If all positions were 'z', increase the total length (e.g., 'zz' -> 'aaa').
        """
        n = len(self.current_chars)
        # Iterate backwards to handle the 'carry over' logic
        for i in range(n - 1, -1, -1):
            if self.current_chars[i] < 'z':
                self.current_chars[i] = chr(ord(self.current_chars[i]) + 1)
                return
            else:
                self.current_chars[i] = 'a'
        
        # Triggered only if the loop completes (all chars were 'z')
        # Reset and increase length: e.g., 'z' -> 'aa', 'zz' -> 'aaa'
        self.current_chars = ['a'] * (n + 1)


# follow ups:
"""
 Optimized _increment Strategy:
If self._is_valid fails at a specific prefix, we should increment the character at the index that caused the failure and reset everything to its right to a.

Ans : Instead of generating a string and then checking if it's valid, we check for validity as we build it. 
If a prefix like aaa is already invalid (when T=2), there is no point in checking aaaa, aaab, etc. We skip all of them.

The Logic: Pruning the Search Tree
    Prefix Check: We iterate from left to right.
    Detection: The moment we find a character that breaks the threshold, we know every string starting with this prefix is "dead."
    The Skip: We increment the character at that failure position and reset everything to the right to a.
    Efficiency: This turns an exponential search into a much more linear one.

Q) Why this is "Drastically" faster
Imagine T=2 and our current string is aaazzz.
    Old Strategy: It would check aaazzz, then aabaaa, then aabaab... it would check every single combination of the last 4 characters (263 combinations) before finally changing the third a.
    New Strategy:
        _find_violation_index sees that the third a (index 2) is the problem.
        It calls _increment_at_index(2).
        Index 2 becomes b, and all zs to the right become a.
        Next string checked: aabaaa.
        Result: We skipped 17,576 invalid strings in a single step.

Complexity Analysis
    Time per getNext(): O(L), where L is the length of the string. We only scan the string a few times. Because we skip invalid sub-trees, we rarely "loop" many times in the while True.
    Space: O(L) to store the character list.
"""

from collections import Counter

class URLShortener:
    def __init__(self, threshold: int):
        """
        Thought Process:
        We use an 'incremental jump' strategy. If a prefix is invalid,
        we skip all possible suffixes of that prefix.
        """
        self.threshold = threshold
        self.current_chars = ['a']

    def getNext(self) -> str:
        while True:
            # 1. Identify the first index that violates the threshold
            violation_idx = self._find_violation_index()
            
            if violation_idx == -1:
                # No violation found! The current string is valid.
                res = "".join(self.current_chars)
                # Prepare for the next call by doing a standard +1 increment
                self._increment_at_index(len(self.current_chars) - 1)
                return res
            else:
                # Violation found at violation_idx (e.g., 'aaa' when T=2)
                # Skip all strings starting with this prefix by incrementing 
                # at the violation index and resetting everything to the right.
                self._increment_at_index(violation_idx)

    def _find_violation_index(self) -> int:
        """
        Scans the current string from left to right.
        Returns the first index where the character frequency exceeds threshold.
        Example: If s='aaab' and T=2, it returns 2 (the index of the third 'a').
        """
        counts = {}
        for i, char in enumerate(self.current_chars):
            counts[char] = counts.get(char, 0) + 1
            if counts[char] > self.threshold:
                return i
        return -1 # Valid string

    def _increment_at_index(self, idx: int):
        """
        Logic:
        1. Increment the character at 'idx'.
        2. Reset everything to the right of 'idx' to 'a'.
        3. If 'idx' itself was 'z', carry the increment to the left.
        4. If the carry goes past index 0, increase the total length.
        """
        # Reset everything to the right of the target index
        for j in range(idx + 1, len(self.current_chars)):
            self.current_chars[j] = 'a'
            
        # Standard carry-over increment starting from 'idx'
        for i in range(idx, -1, -1):
            if self.current_chars[i] < 'z':
                self.current_chars[i] = chr(ord(self.current_chars[i]) + 1)
                return
            else:
                self.current_chars[i] = 'a'
        
        # If we reached here, we had 'zz...z', so increase length
        self.current_chars = ['a'] * (len(self.current_chars) + 1)
