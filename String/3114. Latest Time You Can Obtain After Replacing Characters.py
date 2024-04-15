# Logic: Just think how can you make maximum

class Solution:
    def findLatestTime(self, s: str) -> str:
        first , second, third, fourth =  s[0] , s[1], s[3], s[4]
        # Handling the hour case
        if first == "?" and second == "?":
            first = second = "1"
        elif second == "?":
            if first == "0":
                second = "9"
            else:
                second = "1"
        elif first == "?":
            if second == "1" or second == "0":
                first = "1"
            else:
                first = "0"

        # Handling minute case
        if third == "?" and fourth == "?":
            third = "5"
            fourth = "9"
        elif fourth == "?":
            fourth = "9"
        elif third == "?":
            third = "5"
        return first + second + ":" + third + fourth
    
# Shortcut of above
class Solution:
    def findLatestTime(self, s: str) -> str:
        s = list(s)
        if s[0] == '?': 
            s[0] = '1' if s[1] == '?' or s[1] <= '1' else '0'
        if s[1] == '?': 
            s[1] = '1' if s[0] == '1' else '9'
        if s[3] == '?': s[3] = '5'
        if s[4] == '?': s[4] = '9'
        return ''.join(s)