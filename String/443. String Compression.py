
class Solution:
    def compress(self, chars: List[str]) -> int:
        AnsIndex= 0
        i =0
        while i  < len(chars):
            curChar, count = chars[i], 0
            while i < len(chars) and chars[i] == curChar:
                i+= 1
                count+= 1
            # first append the char
            chars[AnsIndex] = curChar
            AnsIndex += 1 
            # now append its count if count > 1.
            if count > 1:
                # if count >= 10 then that should be written like '1', '0'.
                for c in str(count):
                    chars[AnsIndex] = c
                    AnsIndex += 1
        return AnsIndex
        # return len(chars) # will give incorrect ans as chars will be diff but compiler is automatically modifying char till our ans.


# If asked for only length of compressed string given no need to modify the original chars array.
class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0
        i = 0
        while i  < len(chars):
            curChar, count= chars[i], 0
            while i < len(chars) and chars[i] == curChar:
                i+= 1
                count+= 1
            # first incr for appending char
            ans += 1
            # now append its count if count > 1.
            if count > 1:
                ans += len(str(count))
        return ans

# Java
"""
class Solution {
    public int compress(char[] chars) {
        int ansIndex = 0;
        int i = 0;
        
        while (i < chars.length) {
            char curChar = chars[i];
            int count = 0;
            
            // Count occurrences of the current character
            while (i < chars.length && chars[i] == curChar) {
                i++;
                count++;
            }
            
            // Place the current character at the answer index
            chars[ansIndex] = curChar;
            ansIndex++;
            
            // If count is more than 1, convert it to characters and append
            if (count > 1) {
                String countStr = String.valueOf(count);
                for (char c : countStr.toCharArray()) {
                    chars[ansIndex] = c;
                    ansIndex++;
                }
            }
        }
        
        return ansIndex;
    }
}
"""