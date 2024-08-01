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


# Method 2:
# Logic: 1st digit ko lenge then iska characters and remaining digits ka characters ka cross product lena hoga. (all possible combination)

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

# My minor mistake in above logic
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

# java
"""
// Method 1:

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public List<String> letterCombinations(String digits) {
        Map<Character, String> keypad = new HashMap<>();
        keypad.put('2', "abc");
        keypad.put('3', "def");
        keypad.put('4', "ghi");
        keypad.put('5', "jkl");
        keypad.put('6', "mno");
        keypad.put('7', "pqrs");
        keypad.put('8', "tuv");
        keypad.put('9', "wxyz");

        List<String> result = new ArrayList<>();
        if (digits == null || digits.isEmpty()) {
            return result;
        }
        permutations(digits, 0, "", result, keypad);
        return result;
    }
    
    private void permutations(String digits, int index, String current, List<String> result, Map<Character, String> keypad) {
        if (index == digits.length()) {
            result.add(current);
            return;
        }
        
        String letters = keypad.get(digits.charAt(index));
        for (char letter : letters.toCharArray()) {
            permutations(digits, index + 1, current + letter, result, keypad);
        }
    }
    
}
"""

# Related Q:
# 1) 2266. Count Number of Texts
