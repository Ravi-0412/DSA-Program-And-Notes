# Time= space = O(n)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        list_s = list(s)
        stack = []
        for i in range(len(list_s)):
            if list_s[i] == '(':
                stack.append(i)
            elif list_s[i] == ')':
                # pop if stack is not empty. Means we have required pair for this one.
                if stack:
                    stack.pop()
                # For cur char ')' there is no pair. so we have make value at this index = "".
                # Means extra char, so we will remove this.
                else:
                    list_s[i] = ""
        # Now if our stack is not empty then we will have to make all those index value = "".
        # Because these have no matching pair
        for i in stack:
            list_s[i] = ""
        # Now return the ans as string
        return  "".join(list_s)
