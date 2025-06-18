# method 1: 
# time: O(4^n)  
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad= {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}   # made key as string as input is given in string only
        if not digits:
            return []
        return self.permutations(digits,"",keypad)
    def permutations(self,digits,ans,keypad):
        if not digits:
            return [ans]
        res = []
        letters= keypad[digits[0]]
        for i in range(len(letters)):
            res+= self.permutations(digits[1:], ans+ letters[i], keypad)
        return res


# Method 2:
# Logic: 1st digit ko lenge then iska characters and remaining digits ka characters ka cross product lena hoga. (all possible combination)

# My minor mistake
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {"2": "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def dfs(digits):
            if not digits:
                return []
            ans = []
            digit = digits[0]
            temp = dfs(digits[1 :])
            for char1 in keypad[digit]:
                for char2 in temp:   # agar 'temp' empty hoga isliye tempAns bhi empty hoga and ans bhi empty milega.
                                    # so return at 'if len(digits) ==1'
                    tempAns = char1 + char2
                    ans.append(tempAns)
            return ans
        
        return dfs(digits)
    

# Correct code

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        keypad = {"2": "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def dfs(digits):
            if len(digits) ==1:
                return keypad[digits[0]]
            ans = []
            digit = digits[0]   # 1st digit ko pick kiye then 
            temp = dfs(digits[1 :])   # Remaining char ka all possible combination find kiye
            # Ab cross product le rhe dono keypad characters ka
            for char1 in keypad[digit]:
                for char2 in temp:
                    tempAns = char1 + char2
                    # combination ko add kar rhe ans me
                    ans.append(tempAns)
            return ans
        
        return dfs(digits)


# Java Code 
"""
// Method 1:
import java.util.*;

class Solution {
    Map<Character, String> keypad = Map.of(
        '2', "abc", '3', "def", '4', "ghi", '5', "jkl",
        '6', "mno", '7', "pqrs", '8', "tuv", '9', "wxyz"
    );

    private List<String> permutations(String digits, String ans) {
        if (digits.isEmpty()) {
            return List.of(ans);
        }

        List<String> res = new ArrayList<>();
        String letters = keypad.get(digits.charAt(0));

        for (char letter : letters.toCharArray()) {
            res.addAll(permutations(digits.substring(1), ans + letter));
        }

        return res;
    }

    public List<String> letterCombinations(String digits) {
        if (digits.isEmpty()) {
            return List.of();
        }
        return permutations(digits, "");
    }
}

//Method 2
import java.util.*;

class Solution {
    Map<Character, String> keypad = Map.of(
        '2', "abc", '3', "def", '4', "ghi", '5', "jkl",
        '6', "mno", '7', "pqrs", '8', "tuv", '9', "wxyz"
    );

    private List<String> dfs(String digits) {
        if (digits.length() == 1) {
            return Arrays.asList(keypad.get(digits.charAt(0)).split(""));
        }

        List<String> ans = new ArrayList<>();
        char digit = digits.charAt(0);   // 1st digit pick kiya
        List<String> temp = dfs(digits.substring(1));   // Remaining characters ka all possible combination find kiya

        // Cross product le rhe dono keypad characters ka
        for (char char1 : keypad.get(digit).toCharArray()) {
            for (String char2 : temp) {
                ans.add(char1 + char2);
            }
        }

        return ans;
    }

    public List<String> letterCombinations(String digits) {
        if (digits.isEmpty()) {
            return List.of();
        }
        return dfs(digits);
    }
}
"""

# C++ Code 
"""
//Method 1
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    unordered_map<char, string> keypad = {
        {'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"},
        {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"}
    };

    vector<string> permutations(string digits, string ans) {
        if (digits.empty()) {
            return {ans};
        }
        
        vector<string> res;
        string letters = keypad[digits[0]];

        for (char letter : letters) {
            vector<string> temp = permutations(digits.substr(1), ans + letter);
            res.insert(res.end(), temp.begin(), temp.end());
        }
        
        return res;
    }

    vector<string> letterCombinations(string digits) {
        if (digits.empty()) {
            return {};
        }
        return permutations(digits, "");
    }
};

//Method 2
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    unordered_map<char, string> keypad = {
        {'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"},
        {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"}
    };

    vector<string> dfs(string digits) {
        if (digits.size() == 1) {
            string letters = keypad[digits[0]];
            vector<string> res;
            for (char ch : letters) {
                res.push_back(string(1, ch)); // char → string
            }
            return res;
        }

        vector<string> ans;
        char digit = digits[0];   // 1st digit pick kiya
        vector<string> temp = dfs(digits.substr(1));   // Remaining characters ka all possible combination find kiya

        // Cross product le rhe dono keypad characters ka
        for (char char1 : keypad[digit]) {
            for (const string& char2 : temp) {
                ans.push_back(string(1, char1) + char2);
            }
        }

        return ans;
    }

    vector<string> letterCombinations(string digits) {
        if (digits.empty()) {
            return {};
        }
        return dfs(digits);
    }
};

"""


# Extesnion:
# to count the no of possible combinations
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad= {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}   # made key as string as input is given in string only
        if not digits:
            return []
        return self.permutations(digits,"",keypad)
    def permutations(self,digits,ans,keypad):
        if not digits:
            # return [ans]
            return 1
        res = 0
        letters = keypad[digits[0]]
        for i in range(len(letters)):
            res+= self.permutations(digits[1:], ans + letters[i], keypad)
        return res

# Java
"""
import java.util.*;

class Solution {
    public int letterCombinations(String digits) {
        Map<Character, String> keypad = new HashMap<>();
        keypad.put('2', "abc");
        keypad.put('3', "def");
        keypad.put('4', "ghi");
        keypad.put('5', "jkl");
        keypad.put('6', "mno");
        keypad.put('7', "pqrs");
        keypad.put('8', "tuv");
        keypad.put('9', "wxyz");  // made key as char as input is string

        if (digits.isEmpty()) {
            return 0;
        }

        return permutations(digits, "", keypad);
    }

    private int permutations(String digits, String ans, Map<Character, String> keypad) {
        if (digits.isEmpty()) {
            // return 1
            return 1;
        }

        int res = 0;
        String letters = keypad.get(digits.charAt(0));
        for (int i = 0; i < letters.length(); i++) {
            res += permutations(digits.substring(1), ans + letters.charAt(i), keypad);
        }

        return res;
    }
}
""" 


# C++
"""
#include <iostream>
#include <unordered_map>
#include <string>

class Solution {
public:
    int letterCombinations(std::string digits) {
        std::unordered_map<char, std::string> keypad = {
            {'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"},
            {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"} // made key as char as input is string
        };

        if (digits.empty()) {
            return 0;
        }

        return permutations(digits, "", keypad);
    }

private:
    int permutations(std::string digits, std::string ans, std::unordered_map<char, std::string>& keypad) {
        if (digits.empty()) {
            // return 1;
            return 1;
        }

        int res = 0;
        std::string letters = keypad[digits[0]];
        for (int i = 0; i < letters.size(); ++i) {
            res += permutations(digits.substr(1), ans + letters[i], keypad);
        }

        return res;
    }
};

"""


# Extension:
# to count the no of possible combinations
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad= {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}   # made key as string as input is given in string only
        if not digits:
            return []
        return self.permutations(digits,"",keypad)
    def permutations(self,digits,ans,keypad):
        if not digits:
            # return [ans]
            return 1
        res = 0
        letters = keypad[digits[0]]
        for i in range(len(letters)):
            res+= self.permutations(digits[1:], ans + letters[i], keypad)
        return res

# Java
"""
import java.util.*;

class Solution {
    public int letterCombinations(String digits) {
        Map<Character, String> keypad = new HashMap<>();
        keypad.put('2', "abc");
        keypad.put('3', "def");
        keypad.put('4', "ghi");
        keypad.put('5', "jkl");
        keypad.put('6', "mno");
        keypad.put('7', "pqrs");
        keypad.put('8', "tuv");
        keypad.put('9', "wxyz");  // made key as char as input is string

        if (digits.isEmpty()) {
            return 0;
        }

        return permutations(digits, "", keypad);
    }

    private int permutations(String digits, String ans, Map<Character, String> keypad) {
        if (digits.isEmpty()) {
            // return 1
            return 1;
        }

        int res = 0;
        String letters = keypad.get(digits.charAt(0));
        for (int i = 0; i < letters.length(); i++) {
            res += permutations(digits.substring(1), ans + letters.charAt(i), keypad);
        }

        return res;
    }
}
""" 


# C++
"""
#include <iostream>
#include <unordered_map>
#include <string>

class Solution {
public:
    int letterCombinations(std::string digits) {
        std::unordered_map<char, std::string> keypad = {
            {'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"},
            {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"} // made key as char as input is string
        };

        if (digits.empty()) {
            return 0;
        }

        return permutations(digits, "", keypad);
    }

private:
    int permutations(std::string digits, std::string ans, std::unordered_map<char, std::string>& keypad) {
        if (digits.empty()) {
            // return 1;
            return 1;
        }

        int res = 0;
        std::string letters = keypad[digits[0]];
        for (int i = 0; i < letters.size(); ++i) {
            res += permutations(digits.substr(1), ans + letters[i], keypad);
        }

        return res;
    }
};

"""
