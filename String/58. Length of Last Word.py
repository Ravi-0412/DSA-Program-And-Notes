"""
start from the end of the string. Since we only care about the last word, scanning backward allows us to skip any trailing spaces and 
immediately find the length of the final word without processing the entire string.

Logic Thought Process :
Skip Trailing Spaces: Start a pointer at the end of the string. Move backward as long as you see spaces.
Count Word Characters: Once you hit a non-space character, you've found the end of the last word. Start counting until you hit another space or the beginning of the string.
Return the Count: That count is your result.

Time : O(N), space : O(1)
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Step 1: Initialize pointer at the end of the string
        p = len(s) - 1
        length = 0

        # Step 2: Skip trailing spaces (e.g., "moon  " -> "moon")
        while p >= 0 and s[p] == ' ':
            p -= 1

        # Step 3: Count the characters of the last word
        while p >= 0 and s[p] != ' ':
            length += 1
            p -= 1

        return length

  # Java
  """
  class Solution {
    public int lengthOfLastWord(String s) {
        // Step 1: Initialize pointer at the end of the string
        int p = s.length() - 1;
        int length = 0;

        // Step 2: Skip trailing spaces
        // We check 'p >= 0' first to avoid IndexOutOfBoundsException
        while (p >= 0 && s.charAt(p) == ' ') {
            p--;
        }

        // Step 3: Count the characters of the last word 
        // until we hit another space or the start of the string
        while (p >= 0 && s.charAt(p) != ' ') {
            length++;
            p--;
        }

        return length;
    }
}
  """
