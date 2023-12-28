# How is it different from Q :"2943. Maximize Area of Square Hole in Grid".

# in q "2943. Maximize Area of Square Hole in Grid":
# Already bars are present so for max area we will have to remove max possible consecutive bars
# Otherwise bars will come in between reducing our area.
# So in that q we were checking max consecutive bars we can remove.

# But  here we don't need to care whether it will form square or not after removing fences 
# Because at every unit distance there is fences and they will form square for sure.

# Now come to this Q.

# Here fences are not from before , here only given fences are present.
# Here fences will not come in between automatically like "2943". 

# But here after removing fences we have to care whether it will form square or not
# Because here fences are not present in both direction at unit distance that will form square for sure.

# so here we have to check every possible combination.
# i.e remove all the fences between two fixed fences and check this much length of square 
# we can get in other direction and take maximum of that.

# Time = O(n^2)

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        side = 0
        mod = 10 ** 9 + 7
        diff = set()
        hFences.append(1)
        hFences.append(m)
        for i in range(len(hFences)):
            for j in range(len(hFences)):
                # means we are removing all fences between 'i' and 'j' 
                # 'i' and 'j' will act at end point for horizontal direction.
                if i != j:
                    diff.add(abs(hFences[i] - hFences[j]))
        
        vFences.append(1)
        vFences.append(n)
        for i in range(len(vFences)):
            for j in range(len(vFences)):
                if i != j and abs(vFences[i] - vFences[j]) in diff:
                    side = max(side , abs(vFences[i] - vFences[j]))
        
        if side == 0:
            return -1
        return (side * side) % mod


# Related Q:
# 2943. Maximize Area of Square Hole in Grid