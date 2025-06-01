# Logic: whenever there is backspace then we have to remove the last seen char 
# i.e Last In First Out. So we can use stack.
#approach :
#1)we have to take 2 stacks for two strings s and t 
#2)for every stack upto the length of the string ,append the character into the stack if the character
# is other than '#' , if the character is '#' chack that the stack is empty or not 
# if stack is not emepty then pop the top element from the stack
#3)after running this two stack ,  the final processed strings by joining characters from each stack and checking if both resulting strings are equal.
# time = space = O(m + n)

#python code
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        for i in range(len(s)):
            if s[i] == "#":
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(s[i])
        
        stack_t = []
        for i in range(len(t)):
            if t[i] == "#":
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(t[i])
        return "".join(stack_s) == "".join(stack_t)

#C++ code
class Solution {
public:
    bool backspaceCompare(string s, string t) {
        stack<char> stack_s;
        for (char c : s) {
            if (c == '#') {
                if (!stack_s.empty()) stack_s.pop();
            } else {
                stack_s.push(c);
            }
        }

        stack<char> stack_t;
        for (char c : t) {
            if (c == '#') {
                if (!stack_t.empty()) stack_t.pop();
            } else {
                stack_t.push(c);
            }
        }

        string str_s, str_t;
        while (!stack_s.empty()) {
            str_s = stack_s.top() + str_s;
            stack_s.pop();
        }
        while (!stack_t.empty()) {
            str_t = stack_t.top() + str_t;
            stack_t.pop();
        }

        return str_s == str_t;
    }
};

#Java code
class Solution {
    public boolean backspaceCompare(String s, String t) {
        Stack<Character> stackS = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '#') {
                if (!stackS.isEmpty()) stackS.pop();
            } else {
                stackS.push(c);
            }
        }

        Stack<Character> stackT = new Stack<>();
        for (char c : t.toCharArray()) {
            if (c == '#') {
                if (!stackT.isEmpty()) stackT.pop();
            } else {
                stackT.push(c);
            }
        }

        StringBuilder strS = new StringBuilder();
        StringBuilder strT = new StringBuilder();
        for (char c : stackS) strS.append(c);
        for (char c : stackT) strT.append(c);

        return strS.toString().equals(strT.toString());
    }
}


# Method 2: Do by Two pointer approach in space = O(1)

# My mistake

# While condition in case of if 's[i] == '#' or t[j] == '#' is wrong.
# e.g: s = aab#a### . this will make s = aa
# But s = "" 

# Why giving wrong ans because we are checking consecutive '#' for cancellation in while loop.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        m , n  = len(s) , len(t)
        i , j = m - 1, n - 1
        while i >= 0 or j >= 0:
            if s[i] != '#' and t[j] != '#':
                if s[i] != t[j]:
                    return False
                i -= 1
                j -= 1
            elif s[i] == '#':
                cnt = 0
                while i >= 0 and s[i] == '#':
                    cnt += 1
                    i -= 1
                i -= cnt
            elif t[j] == '#':
                cnt = 0
                while j >= 0 and t[j] == '#':
                    cnt += 1
                    j -= 1
                j -= cnt
        print(i, j)
        # return 1
        return s[: i + 1] == t[: j + 1]


# Correcting above solution

# Above mistake can be handled using a counter.
# We need counter of '#' and till count is > 0, we can cancel and when count == 0 
# We can't cancel and then we will return the cur char at index.

#Apporach
#1)Use two pointers, i and j, to traverse strings s and t from the end to the beginning.
#2)Now define a handler function (getchar) , in this fuction Skips over characters that should be removed due to '#'
#  and Keeps track of how many characters need to be erased using 'cnt' variable after that Returns the next valid character 
# that is not erased, and the updated index.
#3) now  the while loop runs until both the pointers reach to the starting index of their strings ,by using this getchar() function 
# to fetch the next valid character from the both strings
# if the character is not matched then return false
# if no mismatches are found after processing, return True.

# time = O(m + n)
# space = O(1)

#python code: 
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        m , n  = len(s) , len(t)

        def getChar(x, k):
            c , cnt = "", 0
            while k >= 0 and not c:
                if x[k] == '#':
                    cnt += 1
                elif cnt == 0:
                    # Can't erase more so assign c= x[i]
                    c = x[k]
                    # return c, k -1   # Can't cancel more so we can return from here also directly. No need to go futher.
                else: 
                    # Means char other than '#'
                    cnt -= 1
                k -= 1
            return c, k  # 

        i , j = m - 1, n - 1
        while i >= 0 or j >= 0:
            c1 = c2 = ""  # will store the char after erasing if '#' is there.
            if i >= 0:
                c1, i = getChar(s, i)
            if j >= 0 :
                c2, j = getChar(t, j)
            if c1 != c2:
                return False
        return True


#c++ code :
class Solution {
public:
    bool backspaceCompare(string s, string t) {
        int i = s.size() - 1, j = t.size() - 1;

        auto getChar = [](const string& str, int& k) -> char {
            int cnt = 0;
            char c = '\0';
            while (k >= 0 && c == '\0') {
                if (str[k] == '#') {
                    cnt++;
                } else if (cnt == 0) {
                    c = str[k];
                } else {
                    cnt--;
                }
                k--;
            }
            return c;
        };

        while (i >= 0 || j >= 0) {
            char c1 = (i >= 0) ? getChar(s, i) : '\0';
            char c2 = (j >= 0) ? getChar(t, j) : '\0';
            if (c1 != c2) return false;
        }

        return true;
    }
};

# Java code  :       
class Solution {
    public boolean backspaceCompare(String s, String t) {
        int[] i = {s.length() - 1};
        int[] j = {t.length() - 1};

        while (i[0] >= 0 || j[0] >= 0) {
            char c1 = (i[0] >= 0) ? getChar(s, i) : '\0';
            char c2 = (j[0] >= 0) ? getChar(t, j) : '\0';
            if (c1 != c2) return false;
        }

        return true;
    }

    private char getChar(String str, int[] idxRef) {
        int cnt = 0;
        char c = '\0';
        while (idxRef[0] >= 0 && c == '\0') {
            if (str.charAt(idxRef[0]) == '#') {
                cnt++;
            } else if (cnt == 0) {
                c = str.charAt(idxRef[0]);
            } else {
                cnt--;
            }
            idxRef[0]--;
        }
        return c;
    }
}
       