# first approach make a new string and add only alpha numeric char in this
# using the function 'char.isalnum() and return s==s[::-1]


# for checking alpha numeric just make a function and check whether the ascii value of curr char
# lies between ascii value of 'A-Z' or 'a-z' or '0-9' using ord(char)-> this gives the ascii value

# method 2: 
def isPalindrome(self, s):
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l <r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l +=1; r -= 1
    return True


# method 3: just shortcut of above method 1
class Solution:
    def isPalindrome(self, s):
        s= ''.join(e for e in s if e.isalnum()).lower()
        return s== s[::-1]

        

