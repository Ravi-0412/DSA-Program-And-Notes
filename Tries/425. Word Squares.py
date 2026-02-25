# Basic 
"""
A "Word Square" means that if you have $k$ words, the $k$-th row must be identical to the k-th column.
(Transpose)

When you are trying to pick the next word (row $i$), you don't just pick any word. You are restricted by the words you already picked. 
Specifically, the prefix of the next word must match the characters already placed in that column.
Example: If your first word is BALL: 
i) Row 0: B A L L
ii) Column 0 must also be B A L L. 
iii) This means Row 1 must start with A, Row 2 must start with L, and Row 3 must start with L.
"""

# Method 1 :
"""
The Brute Force Logic :
Try every possible combination of words to see if they form a valid square. 
Since all words have length L, a word square must have L rows. We have N words to choose from.
i) Pick any word for Row 0.
ii) Pick any word for Row 1
iii) .... continue until you have L words.
iv) Check: Is this a valid Word Square? (Does Row $k$ == Column k for all k?)

Time : (O(N^L))
"""

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words)
        L = len(words[0])
        results = []
        
        def is_valid(square):
            # Check if Row k == Column k
            # Transpose , just same logic as: Valid word square
            for r in range(L):
                for c in range(L):
                    if square[r][c] != square[c][r]:
                        return False
            return True

        def backtrack(curr_square):
            # Base Case: We have picked L words
            if len(curr_square) == L:
                if is_valid(curr_square):
                    results.append(list(curr_square))
                return
            
            # Try every single word in the list for the next row
            for word in words:
                curr_square.append(word)
                backtrack(curr_square)
                curr_square.pop() # Backtrack

        backtrack([])
        return results
