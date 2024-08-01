# Logic: Find the overall shift/move that will have to make.
# if left shift: reduce by '1' , if right shift: increase by '1'.
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        move = 0
        for x, y in shift:
            if x == 0:
                move -= y
            else:
                move += y
        move %= len(s)  # in case of python, if 'move' is negative then, it will get converted to positive 
        return s[-move:] + s[:-move]   # we always do right shift to get the ans and to handle when move is negative in case of other lang after '%'.