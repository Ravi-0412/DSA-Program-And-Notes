# Logic: Find the overall shift/move that will have to make.
# if left shift: reduce by '1' , if right shift: increase by '1'.
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        move = 0
        for x, y in shift:
            if x == 0:
                move -= y
            else:
                move += y
        move %= len(s)  # in case of python, if 'move' is negative then, it will get converted to positive 
        return s[-move:] + s[:-move]   # we always do right shift to get the ans and to handle when move is negative in case of other lang after '%'.

# java
"""
import java.util.List;

class Solution {
    public String stringShift(String s, List<int[]> shift) {
        int move = 0;
        
        // Calculate the total shift
        for (int[] sh : shift) {
            if (sh[0] == 0) {
                move -= sh[1]; // Left shift
            } else {
                move += sh[1]; // Right shift
            }
        }
        
        int n = s.length();
        move %= n; // In case the move is greater than the length of the string

        // Handle negative move by converting to equivalent positive move
        if (move < 0) {
            move += n;
        }

        // Perform the right shift
        return s.substring(n - move) + s.substring(0, n - move);
    }
}

"""