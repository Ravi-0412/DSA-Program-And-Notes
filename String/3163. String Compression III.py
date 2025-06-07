# Just do what question is telling to do.

class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        comp = ""
        i = 0
        while i < n:
            j = i + 1
            while j < n and word[j] == word[j -1]:
                j += 1
            cnt = j - i
            if cnt <= 9:
                comp += str(cnt) + word[i]
            else:   
                q, r = divmod(cnt, 9)
                comp += q *(str(9) + word[i])
                # for k in range(q):
                #     comp += str(9) + word[i]
                if r != 0:
                    comp += str(r) + word[i]
            i = j
        return comp


# Better way to write.
# Run the inside while loop maximum '9' times for same chosen character.
class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        comp = ""
        i = 0
        while i < n:
            cnt = 0
            c = word[i]
            while i < n and word[i] == c and cnt < 9:
                i += 1
                cnt += 1
            comp += str(cnt) + c 
        return comp

# Java Code 
"""
//Method 1
class Solution {
    public String compressedString(String word) {
        int n = word.length();
        StringBuilder comp = new StringBuilder();
        int i = 0;

        while (i < n) {
            int j = i + 1;
            while (j < n && word.charAt(j) == word.charAt(j - 1)) {
                j++;
            }
            int cnt = j - i;
            if (cnt <= 9) {
                comp.append(cnt).append(word.charAt(i));
            } else {
                int q = cnt / 9, r = cnt % 9;
                comp.append("9".repeat(q)).append(word.charAt(i));
                if (r != 0) {
                    comp.append(r).append(word.charAt(i));
                }
            }
            i = j;
        }
        return comp.toString();
    }
}
//Method 2
class Solution {
    public String compressedString(String word) {
        int n = word.length();
        StringBuilder comp = new StringBuilder();
        int i = 0;

        while (i < n) {
            int cnt = 0;
            char c = word.charAt(i);
            while (i < n && word.charAt(i) == c && cnt < 9) {
                i++;
                cnt++;
            }
            comp.append(cnt).append(c);
        }
        return comp.toString();
    }
}
"""

# C++ Code 
"""
//Method 1
#include <string>

using namespace std;

class Solution {
public:
    string compressedString(string word) {
        int n = word.size();
        string comp = "";
        int i = 0;

        while (i < n) {
            int j = i + 1;
            while (j < n && word[j] == word[j - 1]) {
                j++;
            }
            int cnt = j - i;
            if (cnt <= 9) {
                comp += to_string(cnt) + word[i];
            } else {
                int q = cnt / 9, r = cnt % 9;
                comp += string(q, '9') + word[i];  
                if (r != 0) {
                    comp += to_string(r) + word[i];
                }
            }
            i = j;
        }
        return comp;
    }
};
//Method 2
class Solution {
public:
    string compressedString(string word) {
        int n = word.size();
        string comp = "";
        int i = 0;

        while (i < n) {
            int cnt = 0;
            char c = word[i];
            while (i < n && word[i] == c && cnt < 9) {
                i++;
                cnt++;
            }
            comp += to_string(cnt) + c;
        }
        return comp;
    }
};
"""