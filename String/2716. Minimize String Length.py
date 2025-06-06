# logic: All duplicate will get discarded, only distinct char will left.
# time: O(n)

class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))

# java
"""
class Solution {
    public int minimizedStringLength(String s) {
        return new HashSet<Character>() {{
            for (char c : s.toCharArray()) add(c);
        }}.size();
    }
}
"""

"""
class Solution {
    public int minimizedStringLength(String s) {
        HashSet<Character> uniqueChars = new HashSet<>();
        for (char c : s.toCharArray()) {
            uniqueChars.add(c);
        }
        return uniqueChars.size();
    }

"""

# C++ Code 
"""
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int minimizedStringLength(string s) {
        return unordered_set<char>(s.begin(), s.end()).size();
    }
};
"""