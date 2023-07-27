# logic in notes
# page: 96

class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if y > x:
            return (x*2 + 1 + z)*2
        if x > y:
                return (y*2+ 1 + z) *2
        if x == y:
            return (x + y+z)*2
                
        