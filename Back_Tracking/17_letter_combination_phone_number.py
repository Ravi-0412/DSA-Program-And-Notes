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
        res= []
        letters= keypad[digits[0]]
        for i in range(len(letters)):
            res+= self.permutations(digits[1:],ans+ letters[i],keypad)
        return res


# to count the no of possible combinations
def PadCount(str1, ans):
    count= 0
    if not str1: # if given string is empty, then only we get one of the ans so incr count
        # count1= 0   # just to avoid error
        # count1+= 1   # will store the local ans  
        # return count1
        return 1     # simplest way of all the above three lines
    
    # convert the char integer into integer i.e '2' into 2
    digit= ord(str1[0]) - ord('0')    # will convert '2' into 2 by taking diff in ascii value
    code= pad[digit]       # will give the code word of letter 'digit' 
    ros= str1[1:] 
    for i in range(len(code)):  # now add each letter of 1st digit with code of 2nd digit
                                # just like we find no of all possible substring
        count+= PadCount(ros,ans+code[i])
    return count

pad= [" ", " ", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv","wxyz"]
print(PadCount("78",""))


# Method 2: Better one & very simple
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
                for char2 in temp:   # 'temp' empty hoga isliye temapAns bhi empty hoga ans ans bhi empty milega.
                    tempAns = char1 + char2
                    ans.append(tempAns)
            return ans
        
        return dfs(digits)
        