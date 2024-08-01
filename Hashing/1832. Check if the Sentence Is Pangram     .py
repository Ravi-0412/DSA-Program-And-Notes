# using set
# logic: Add each eleemnt you see into set. Then at last length of set must be = 26

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(s)) == 26

# java
"""
class Solution {
    public boolean checkIfPangram(String sentence) {
        Set<Character> s = new HashSet<>();
        for (int i = 0; i < sentence.length(); ++i)
            s.add(sentence.charAt(i));
        return s.size() == 26;
        
    }
}
"""

# Method 2: Best one
# without set or map

# Logic: for each char you see make bit_value = 1 in 'seen'
# e.g: char = e then make 'bit_value' = 1 at 4th position ('e' - 'a')

# Then 'seen' value at must be equal to '(1 << 26) - 1' if all 26 characters are present.

"""
class Solution {
    public boolean checkIfPangram(String sentence) {
        int seen = 0;
        for(char c : sentence.toCharArray()) {
            int ci = c - 'a';
            seen = seen | (1 << ci);
        }
        return seen == ((1 << 26) - 1);
    }
}
"""

