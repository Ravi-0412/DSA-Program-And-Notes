# Time Complexity: O(N)
# Space Complexity: O(1)

# Logic:
"""
Note:  it's  better to replace any character with 'a' from start if not 'a'.
if all 'a' in 1st half then replace last character  with 'b'.
so:
Check half of the string,
replace a non 'a' character to 'a'.

If only one character, return empty string.
Otherwise repalce the last character to 'b'
"""

def break_palindrome(palindrome: str) -> str:
    s = list(palindrome)
    n = len(s)
    
    for i in range(n // 2):
        if s[i] != 'a':
            s[i] = 'a'
            return ''.join(s)
    
    # If all characters are 'a'
    s[n - 1] = 'b'
    return "" if n < 2 else ''.join(s)


# java
"""
    public String breakPalindrome(String palindrome) {
        char[] s = palindrome.toCharArray();
        int n = s.length;

        for (int i = 0; i < n / 2; i++) {
            if (s[i] != 'a') {
                s[i] = 'a';
                return String.valueOf(s);
            }
        }
        s[n - 1] = 'b'; //if all 'a'
        return n < 2 ? "" : String.valueOf(s);
    }
"""