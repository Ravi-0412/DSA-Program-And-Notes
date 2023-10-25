# logic in notes
# page: 96

# 'z' and come after 'z' so need to worry about 'z'.
# All 'z' an be utilised.

# for 'x' and 'y', they will come in pair eithex 'xy' or 'yx' of x > y and x < y respectively.

# 1) if x > y:
# then we can form 'xy' pair i.e xyxyxy...
# One more 'x' can come as last of pair so no of 'xy' pair = min(x, y)
# and one more occurence of 'x' at last.

# All 'z' can come at 1st together.
# So final string = zzzz....xyxyxy....x

# 2) if y > x:
# then we can form 'yx' pair i.e yxyxyx.....
# One more 'y' can come as last of pair so no of 'yx' pair = min(x, y)
# and one more occurence of 'y' at last.

# All 'z' can come at last together.
# So final string = yxyx....yzzzz.....

# 3) if x == y
# then any of '1' or '2' will be valid but one extra 'x' or 'y' won't come.

class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if x > y:
            return (y*2+ 1 + z) *2
        if y > x:
            return (x*2 + 1 + z)*2
        if x == y:
            return (x + y+z)*2
