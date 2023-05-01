# method 1: 
# time: O(4^n)  
def PhonePad(str1,ans):
    pad= [" ", " ", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv","wxyz"]
    if not str1:  # we get one of the ans.
        print(ans,end=" ")
        return
    # convert the char integer into integer i.e '2' into 2
    digit= ord(str1[0]) - ord('0')    # will convert '2' into 2 by taking diff in ascii value
    code= pad[digit]       # will give the code word of letter 'digit' 
    ros= str1[1:] 
    for i in range(len(code)):  # now add each letter of 1st digit with code of 2nd digit
                                # just like we find no of all possible substring
        PhonePad(ros,ans+code[i])
    print()
PhonePad("78","")
PhonePad("234","")


# method2: If you want to return 'ans' in array
# submitted on leetcode
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:  # if string is empty
            return []
        return self.PhonePad(digits,"")
    
    def PhonePad(self,digits,ans):
        res= []
        pad= [" ", " ", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv","wxyz"]
        if not digits:
            new_list= []
            new_list.append(ans)
            return new_list
        # convert the char integer into integer i.e '2' into 2
        num= ord(digits[0]) - ord('0')    # will convert '2' into 2 by taking diff in ascii value
        code= pad[num]       # will give the code word of letter 'digit' 
        ros= digits[1:] 
        for i in range(len(code)):  # now add each letter of 1st digit with code of 2nd digit
                                # just like we find no of all possible substring
            res+= Solution().PhonePad(digits[1:], ans+ code[i])   # will add each possible combination 
        return res

l1= Solution()
print(l1.letterCombinations("78"))


# better way of writing the above code. Do like this only.
# mine
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad= {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}   # made key as string as input is given in string only
        if not digits:
            return []
        return self.permutations(digits,"",keypad)
    def permutations(self,digits,ans,keypad):
        if not digits:
            local= [ans]
            return local
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
    pad= [" ", " ", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv","wxyz"]
    # convert the char integer into integer i.e '2' into 2
    digit= ord(str1[0]) - ord('0')    # will convert '2' into 2 by taking diff in ascii value
    code= pad[digit]       # will give the code word of letter 'digit' 
    ros= str1[1:] 
    for i in range(len(code)):  # now add each letter of 1st digit with code of 2nd digit
                                # just like we find no of all possible substring
        count+= PadCount(ros,ans+code[i])
    return count

print(PadCount("78",""))


# a lot of more concise soln in 'coding channel' have to look on that later
