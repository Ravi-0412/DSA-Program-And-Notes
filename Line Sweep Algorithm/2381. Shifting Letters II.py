# Just similar to : "2381. Shifting Letters II"

# Logic: Find the resultant shift for each index using 'Line Sweep' algo.

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        line = [0] * (n + 1)
        
        # Apply the shifts
        for start, end, direction in shifts:
            if direction == 1:  # Forward shift
                line[start] += 1
                line[end + 1] -= 1
            else:  # Backward shift
                line[start] -= 1
                line[end + 1] += 1
        
        # Calculate the cumulative shifts
        for i in range(1, n):
            line[i] += line[i - 1]  # Now Line[i]: will represent the net shift of index 'i'
        
        # Apply shifts to the string
        result = []
        for i in range(n):
            shift = (ord(s[i]) - ord('a') + line[i]) % 26
            shift = (shift + 26) % 26  # Ensure non-negative modulo
            result.append(chr(ord('a') + shift))
        
        return ''.join(result)


# Java
"""
class Solution {
    public String shiftingLetters(String s, int[][] shifts) {
        int n = s.length();
        int[] line = new int[n + 1];
        
        // Apply the shifts
        for (int[] shift : shifts) {
            int start = shift[0], end = shift[1], direction = shift[2];
            if (direction == 1) { // Forward shift
                line[start] += 1;
                line[end + 1] -= 1;
            } else { // Backward shift
                line[start] -= 1;
                line[end + 1] += 1;
            }
        }
        
        // Compute cumulative shifts
        for (int i = 1; i < n; i++) {
            line[i] += line[i - 1];
        }
        
        // Apply the shifts to the string
        char[] result = new char[n];
        for (int i = 0; i < n; i++) {
            int shift = (s.charAt(i) - 'a' + line[i]) % 26;
            if (shift < 0) shift += 26; // Ensure positive modulo
            result[i] = (char) ('a' + shift);
        }
        
        return new String(result);
    }
}
"""
