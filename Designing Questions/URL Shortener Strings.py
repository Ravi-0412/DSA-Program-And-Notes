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
