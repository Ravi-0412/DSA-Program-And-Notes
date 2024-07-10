# Logic: Ans will be equal to 'depth of stack'.

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == "./":
                # No need to do anything
                continue
            if log == "../":
                # then move to parent means move to just previous folder. So pop to move to previous folder if stack is not empty.
                if stack:
                    stack.pop()
            else:
                # Move to given new folder so add the folder in stack.
                folder = log[: -1]
                stack.append(folder)
        return len(stack)

# Java
class Solution {
    public int minOperations(String[] logs) {
        Stack<String> stack = new Stack<>();
        for(String log: logs){
            if(log.equals("./"))
                continue ;
            if(log.equals("../")){
                if(!stack.isEmpty())
                    stack.pop();
            }
            else {
                String folder = log.substring(0, log.length());
                stack.push(folder);
            }
        }
        return stack.size(); 
    }
}

# Method 2: Best one without extra space
# time = O(n), space = O(1)

# logic: No need of stack as we are not comparing anything with stack elements.
# we are only pushing(incrementing length) and poping(decrementing length), 
# so just keep a variable and increment and decrement that.

class Solution {
    public int minOperations(String[] logs) {
        int ans = 0 ;
        for(String log: logs){
            if(log.equals("./"))
                continue ;
            if(log.equals("../")){
                if(ans > 0)
                    ans -= 1;
            }
            else {
                ans += 1;
            }
        }
        return ans;
    }
}