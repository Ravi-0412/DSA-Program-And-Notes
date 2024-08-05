# Just sam elogic as :" 387. First Unique Character in a String"

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        m = {}
        for s in arr:
            if s in m:
                m[s] += 1
            else:
                m[s] = 1
        
        for s in arr:
            if m[s] == 1:
                k -= 1
                if k == 0:
                    return s
        
        return ""