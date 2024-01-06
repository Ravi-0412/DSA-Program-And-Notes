# Just we have to find the 'Next greater right'

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n, stack, ans= len(temperatures), [], []
        for i in range(n-1,-1,-1):
            while stack and temperatures[stack[-1]]<= temperatures[i]:
                    stack.pop()
            if stack== []:  
                ans.append(0)
            else:  # means stack top is greater than arr[i]
                ans.append(stack[-1] -i)
            stack.append(i)
        return ans[::-1]
