# Easy -medium level Q only.

# Read the comments inside code.

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        curLine = []
        lenCurLine = 0
        i = 0
        while i < len(words):
            # if we consider the cur word then no of spaces should be atleast 'len(curLine)'
            # i.e '1' between each word.
            if lenCurLine + len(curLine) + len(words[i]) > maxWidth:
                # means is already complete
                # so now we need to redistribute the spaces
                totalSpaces = maxWidth - lenCurLine
                # we need 'len(curLine) - 1' between each word for even distribution.
                # To avoid '0' in remainder , taking max with '1'.
                noOfEvenlyDistSpaces = totalSpaces // max(1, len(curLine) - 1)
                remainder = totalSpaces % max(1, len(curLine) - 1) 
                # this much space we have to distribute from left to right. '1' between each char from left to right.
                # remainder must be less than 'len(curLine) - 1'.
                
                # Now distribiute the char between each word.
                # No need to put space after last word so going till 'len(curLine) - 1'.
                for j in range(max(1, len(curLine) - 1)):
                    curLine[j] += " " * noOfEvenlyDistSpaces
                    # keep distributing the extra char 
                    if remainder:
                        curLine[j] += " "
                        remainder -= 1
                
                # Add the curLine to 'ans' and reset the variable for next Line
                ans.append("".join(curLine))
                curLine, lenCurLine = [], 0
            
            # add the cur word to line 
            curLine.append(words[i])
            lenCurLine += len(words[i])
            i += 1

        # Last line will be not covered in loop, we will have to handle separately.
        # last line we need to put only '1' spaces between each char and at last put all spaces to make up length = maxWidth
        lastLine = " ".join(curLine)   # this will put '1' space automatically between each word.
        remainingSpace = maxWidth - len(lastLine)  # this much char we have to put at last
        lastLine += " " * remainingSpace
        ans.append(lastLine)
        return ans