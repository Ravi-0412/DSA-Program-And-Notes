# Method 1: 

#s.split() => Splits the string s by whitespaces and ignores nultiple spaces 
# [:: -1] => it reverses the list  
#" ".join(...) => finally join the string 
# The main point is the reverse the string

# Time = O(n)
# Space = O(n), excluding answer one.

class Solution:
    def reverseWords(self, s: str) -> str:
        # return " ".join(list(s.strip().split(" "))[::-1])
        # return " ".join(list(s.strip().split())[::-1])
        # return " ".join(s.strip().split()[::-1])
        return " ".join(s.split()[::-1])

'''
C++ Code :
class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s);
        string word;
        vector<string> words;
        while (ss >> word) {
            words.push_back(word);
        }
        reverse(words.begin(), words.end());
        string result;
        for (int i = 0; i < words.size(); i++) {
            if (i > 0) result += " ";
            result += words[i];
        }
        return result;
    }
};

Java Code :
class Solution {
    public String reverseWords(String s) {
        String[] words = s.trim().split("\\s+");
        StringBuilder sb = new StringBuilder();
        for (int i = words.length - 1; i >= 0; i--) {
            sb.append(words[i]);
            if (i != 0) sb.append(" ");
        }
        return sb.toString();
    }
}

'''