# time= space= O(n)

# Note: No need to check for 'left closest char other than * using while loop when we will see any *' 
# because the 'non char than * will get removed by the previous *.

# so only that char will get removed when it will be just adjacent to the current "*" directly or
# indirectly(after removing char in between).

class Solution:
    def removeStars(self, s: str) -> str:
        stack= []
        for c in s:
            if c != "*":
                stack.append(c)
            else:
                # no need to check if stack is non-empty because it's gievn that there exits a valid ans always.
                stack.pop()   
        return "".join(stack)


# Method 2: Using Two pointer
class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        cnt = 0
        i = len(s) - 1
        while i >= 0:
            if s[i] == '*':
                cnt += 1
            else:
                if cnt == 0:
                    # then we can't cancel this char
                    ans.append(s[i])
                else:
                    # We can cancel this char so don't add this char 
                    # And decrement the power of 'cnt'.
                    cnt -= 1
            i -= 1
        return "".join(ans[::-1])


# Method 3:
# could have done in O(1) space but python doesn't support string assignment.

# Approach in c++

# 1) Start with two pointers from the first element(i representing a traversal and string from 0 to j-1 represents answer till ith element)
# 2) If you find a non * element, increase j as it'll be part of answer.
# 3) But if you find * then remove the last element of our answer(i.e. decrease j).
# 4) After traversing all the elements return substring till j as answer.(refer point 1).
    
# class Solution {
# public:
#     string removeStars(string s) {
#         int i=0,j=0;
#         for(i=0;i<s.size();i++){
#             if(s[i]=='*'){
#                 j--;
#             }else{
#                 s[j++] = s[i];
#             }
#         }
#         return s.substr(0,j);
#     }
# };


