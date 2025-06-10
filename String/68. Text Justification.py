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

# Java Code 
"""
import java.util.*;

class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> ans = new ArrayList<>();
        List<String> curLine = new ArrayList<>();
        int lenCurLine = 0;
        int i = 0;

        while (i < words.length) {
            // If we consider the current word, then the number of spaces should be at least 'curLine.size()'
            // i.e. '1' between each word.
            if (lenCurLine + curLine.size() + words[i].length() > maxWidth) {
                // Means line is already complete, now redistribute the spaces
                int totalSpaces = maxWidth - lenCurLine;
                // We need 'curLine.size() - 1' spaces between each word for even distribution.
                // To avoid '0' in remainder, taking max with '1'.
                int noOfEvenlyDistSpaces = totalSpaces / Math.max(1, curLine.size() - 1);
                int remainder = totalSpaces % Math.max(1, curLine.size() - 1);
                // This much space we distribute from left to right. '1' between each char from left to right.
                // Remainder must be less than 'curLine.size() - 1'.

                // Now distribute spaces between each word.
                // No need to put space after last word, so going till 'curLine.size() - 1'.
                for (int j = 0; j < Math.max(1, curLine.size() - 1); j++) {
                    curLine.set(j, curLine.get(j) + " ".repeat(noOfEvenlyDistSpaces));
                    // Keep distributing the extra spaces
                    if (remainder > 0) {
                        curLine.set(j, curLine.get(j) + " ");
                        remainder--;
                    }
                }

                // Add the curLine to 'ans' and reset variables for next line
                ans.add(String.join("", curLine));
                curLine.clear();
                lenCurLine = 0;
            }

            // Add the current word to the line
            curLine.add(words[i]);
            lenCurLine += words[i].length();
            i++;
        }

        // Last line is not covered in loop, handle separately.
        // Last line should have only '1' spaces between words, and extra spaces at the end.
        String lastLine = String.join(" ", curLine);
        int remainingSpace = maxWidth - lastLine.length();  // Fill remaining spaces
        lastLine += " ".repeat(remainingSpace);
        ans.add(lastLine);

        return ans;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> ans;
        vector<string> curLine;
        int lenCurLine = 0;
        int i = 0;

        while (i < words.size()) {
            // If we consider the current word, then the number of spaces should be at least 'len(curLine)'
            // i.e. '1' between each word.
            if (lenCurLine + curLine.size() + words[i].size() > maxWidth) {
                // Means line is already complete, now redistribute the spaces
                int totalSpaces = maxWidth - lenCurLine;
                // We need 'curLine.size() - 1' spaces between each word for even distribution.
                // To avoid '0' in remainder, taking max with '1'.
                int noOfEvenlyDistSpaces = totalSpaces / max(1, (int)curLine.size() - 1);
                int remainder = totalSpaces % max(1, (int)curLine.size() - 1);
                // This much space we distribute from left to right. '1' between each char from left to right.
                // Remainder must be less than 'curLine.size() - 1'.

                // Now distribute spaces between each word.
                // No need to put space after last word, so going till 'curLine.size() - 1'.
                for (int j = 0; j < max(1, (int)curLine.size() - 1); j++) {
                    curLine[j] += string(noOfEvenlyDistSpaces, ' ');
                    // Keep distributing the extra spaces
                    if (remainder) {
                        curLine[j] += " ";
                        remainder--;
                    }
                }

                // Add the curLine to 'ans' and reset variables for next line
                string line = "";
                for (const string& word : curLine) {
                    line += word;
                }
                ans.push_back(line);
                curLine.clear();
                lenCurLine = 0;
            }

            // Add the current word to the line
            curLine.push_back(words[i]);
            lenCurLine += words[i].size();
            i++;
        }

        // Last line is not covered in loop, handle separately.
        // Last line should have only '1' spaces between words, and extra spaces at the end.
        string lastLine = "";
        for (size_t j = 0; j < curLine.size(); j++) {
            lastLine += curLine[j] + (j != curLine.size() - 1 ? " " : "");
        }
        int remainingSpace = maxWidth - lastLine.size();  // Fill remaining spaces
        lastLine += string(remainingSpace, ' ');
        ans.push_back(lastLine);

        return ans;
    }
};
"""