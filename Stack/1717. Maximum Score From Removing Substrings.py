# Logic: First remove the string having maximum value.
# Then from remaining string remove staring having minimum value.

# Note: In Python, variables defined inside an if or else block 
# are accessible outside of the block as long as they are assigned a value within the block. 
# In Python, the scope of a variable defined within an if or else block is the entire function.


# python
class Solution:
    def findScore(self, s: str, sub: str, x: int, stack: list) -> int:
        ans = 0
        for c in s:
            if stack and (stack[-1] + c) == sub:
                stack.pop()
                ans += x
            else:
                stack.append(c)
        return ans

    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            first_to_remove = "ab"    # created under 'if' but can access in entire function.
            bigger = x
            last_to_remove = "ba"
            smaller = y
        else:
            first_to_remove = "ba"
            bigger = y
            last_to_remove = "ab"
            smaller = x

        stack = []
        ans = self.findScore(s, first_to_remove, bigger, stack)
        
        # Create a new string from the remaining characters in the stack
        t = ''.join(stack)
        
        # Clear the stack for reuse
        stack.clear()
        
        ans += self.findScore(t, last_to_remove, smaller, stack)
        
        return ans

"""
class Solution {

    public int findScore(String s, String sub, int x, Stack<Character> stack){
        int ans = 0;
        for(int i = 0; i < s.length(); i++){
            Character c = s.charAt(i);
            if(!stack.isEmpty() && ("" + stack.peek() + c).equals(sub)){
                stack.pop();
                ans += x;
            }
            else{
                stack.push(c);
            }
        }
        return ans;
    }

    public int maximumGain(String s, int x, int y) {
        String first_to_remove;
        String last_to_remove;
        int bigger;
        int smaller;
        if(x > y) {
            first_to_remove = "ab" ;
            bigger = x;
            last_to_remove = "ba" ;
            smaller = y;
        }
        else{
            first_to_remove = "ba" ;
            bigger = y;
            last_to_remove = "ab" ;
            smaller = x;
        }
        Stack<Character> stack = new Stack<>();
        int ans = findScore(s, first_to_remove, bigger, stack);
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        String t = sb.reverse().toString();
        ans += findScore(t, last_to_remove, smaller, stack);
        return ans;
    }
}

"""