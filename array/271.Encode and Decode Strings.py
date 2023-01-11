# logic :1)we can append any special value say '#' after each char .
# But this will not work in case, this special char is also a part of string.

# 2) we can add the length of each word with special symbol for encoding.
# this only we did . 
# we can use any encoding method or symbol.

class Solution:
    # encoding
    def encode(self, strs):
        res= ""
        for s in strs:   # adding the len(word) + special symbol.
            res+= str(len(s)) + '#' + s
        return res

    def decode(self, str):
        res= []
        i= 0  # when we will start searching to the next word
        while i < len(str):
            j= i   # find the number before '#'
            while str[j] != '#':
                j+= 1
            # now we have found one word.
            length= int(str[i:j])   # will give the length of curr word because that can be mpre than one digit.
            res.append(str[j+1: j+1+length])   # curr word will lie between these.
            i= j+1+length    # searchinh for next word will start from here.
        return res
