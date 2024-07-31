# Python

def betterCompression(compressed):
    # Array to hold frequencies of each character
    count = [0] * 26
    
    i = 0
    length = len(compressed)
    
    # Traverse the compressed string to count frequencies
    while i < length:
        # Extract the character
        current_char = compressed[i]
        i += 1
        
        # Extract the number (frequency)
        frequency = 0
        while i < length and compressed[i].isdigit():
            frequency = frequency * 10 + int(compressed[i])
            i += 1
        
        # Update the frequency for the character in the count array
        count[ord(current_char) - ord('a')] += frequency
    
    # Build the result string
    result = []
    for j in range(26):
        if count[j] > 0:
            result.append(f"{chr(j + ord('a'))}{count[j]}")
    
    return ''.join(result)


# java
""""
class Solution {
    public String betterCompression(String compressed) {
        // Array to hold frequencies of each character
        int[] count = new int[26];
        
        int i = 0;
        int length = compressed.length();
        
        // Traverse the compressed string to count frequencies
        while (i < length) {
            // Extract the character
            char currentChar = compressed.charAt(i);
            i++;
            
            // Extract the number (frequency)
            int frequency = 0;
            while (i < length && Character.isDigit(compressed.charAt(i))) {
                frequency = frequency * 10 + (compressed.charAt(i) - '0');
                i++;
            }
            
            // Update the frequency for the character in the count array
            count[currentChar - 'a'] += frequency;
        }
        
        // Build the result string
        StringBuilder result = new StringBuilder();
        for (int j = 0; j < 26; j++) {
            if (count[j] > 0) {
                result.append((char) (j + 'a')).append(count[j]);
            }
        }
        
        return result.toString();
    }
}

"""