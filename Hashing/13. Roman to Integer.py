
# method 1:
# logic: just replace all the special two digit character(like for 4,9 ect..) with normal one
# so that we can apply the logic directly

class Solution:
    def romanToInt(self, s: str) -> int:
        special= {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4,'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        if s in special:
            return special[s]
        n= len(s)
        s = s.replace("IV", "IIII")
        s=  s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s=  s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s=  s.replace("CM", "DCCCC")
        number= 0
        for c in s:
            number+= special[c]
        return number


# method 2:
# mine approach and better one.

# Why we are able to do like this?
# Roman numerals are usually written largest to smallest from left to right i.e s[i] > s[i + 1].
# But if s[i] < s[i + 1] then it means s[i] & s[i + 1] together forming 4, 9, 40,90, 400, 90.

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(len(s) -1):
            # for handling the cases like 4,9 etc...
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:  # for normal case
                z += roman[s[i]]
        return z + roman[s[-1]]   # last one will be left

# Java Code
"""
import java.util.HashMap;

// Method 1: Using replacements for special Roman numeral cases
class Solution {
    public int romanToInt(String s) {
        HashMap<String, Integer> special = new HashMap<>();
        special.put("I", 1); special.put("V", 5); special.put("X", 10);
        special.put("L", 50); special.put("C", 100); special.put("D", 500); special.put("M", 1000);
        special.put("IV", 4); special.put("IX", 9); special.put("XL", 40); special.put("XC", 90);
        special.put("CD", 400); special.put("CM", 900);

        if (special.containsKey(s)) return special.get(s);

        s = s.replace("IV", "IIII");
        s = s.replace("IX", "VIIII");
        s = s.replace("XL", "XXXX");
        s = s.replace("XC", "LXXXX");
        s = s.replace("CD", "CCCC");
        s = s.replace("CM", "DCCCC");

        int number = 0;
        for (char c : s.toCharArray()) number += special.get(String.valueOf(c));

        return number;
    }
}

// Method 2: More optimized approach based on numeral ordering rules
class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> roman = new HashMap<>();
        roman.put('M', 1000); roman.put('D', 500); roman.put('C', 100);
        roman.put('L', 50); roman.put('X', 10); roman.put('V', 5); roman.put('I', 1);
        
        int result = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            if (roman.get(s.charAt(i)) < roman.get(s.charAt(i + 1))) {
                result -= roman.get(s.charAt(i));
            } else {
                result += roman.get(s.charAt(i));
            }
        }
        return result + roman.get(s.charAt(s.length() - 1));
    }
}
"""

# C++ Code
"""
#include <string>
#include <unordered_map>
using namespace std;

// Method 1: Using replacements for special Roman numeral cases
class Solution {
public:
    int romanToInt(string s) {
        unordered_map<string, int> special = {
            {"I", 1}, {"V", 5}, {"X", 10}, {"L", 50}, {"C", 100}, {"D", 500}, {"M", 1000},
            {"IV", 4}, {"IX", 9}, {"XL", 40}, {"XC", 90}, {"CD", 400}, {"CM", 900}
        };

        if (special.find(s) != special.end()) return special[s];

        s = replaceAll(s, "IV", "IIII");
        s = replaceAll(s, "IX", "VIIII");
        s = replaceAll(s, "XL", "XXXX");
        s = replaceAll(s, "XC", "LXXXX");
        s = replaceAll(s, "CD", "CCCC");
        s = replaceAll(s, "CM", "DCCCC");

        int number = 0;
        for (char c : s) number += special[string(1, c)];

        return number;
    }

private:
    string replaceAll(string s, const string& from, const string& to) {
        size_t pos = 0;
        while ((pos = s.find(from, pos)) != string::npos) {
            s.replace(pos, from.length(), to);
            pos += to.length();
        }
        return s;
    }
};

// Method 2: More optimized approach based on numeral ordering rules
class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> roman = {{'M', 1000}, {'D', 500}, {'C', 100},
                                          {'L', 50},  {'X', 10},  {'V', 5}, {'I', 1}};
        int result = 0;

        for (size_t i = 0; i < s.length() - 1; i++) {
            if (roman[s[i]] < roman[s[i + 1]]) {
                result -= roman[s[i]];
            } else {
                result += roman[s[i]];
            }
        }
        return result + roman[s.back()];
    }
};
"""