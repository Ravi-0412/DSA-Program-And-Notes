# very nice Q.
# logic: overall, there are totally 4 scenarios will happen: 1.(+,+) 2.(-,-) 3.(+,-) 4.(-,+)
# But collision will hapen in 3rd case only.(not in 4th case)
# i.e if we traverse from left to right in array then for collision 1st asteroid (left one) must be moveing towards right,
# and 2nd one must be moving towards left. (+, -)
# why? => just draw on paper .

# How to do ?
# just store the 1st asteroid into stack and for next check if it can collide with the previous asteroid.
# so we will put the +ve asteroid into stack and if there is any -ve asteroid then there is chance of collision.
# But when they can collide?
# 1) when stack is not empty and there is +ve ball on stack.
# a) curr -ve ball can cancel when abs(curr) > stack[-1] so keep on poping until abs(curr) > stack[-1].
# b) see the explanation in coding
# why stack?
# ANs: we have to comapre with previous one and after operation we have to add the result and then this curr result will be comapred with next one and so on.

# time: o(n)

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack= []
        for num in asteroids:
            if num > 0:
                stack.append(num)
            else:
                # keep on poping as the curr one will cancel the stack top.
                while stack and stack[-1] > 0 and stack[-1] < abs(num):
                    stack.pop()
                #stack can be empty only or have become empty after poping(curr -ve have cancel all ball due to high magnitude) or
                # stack top is of same sign i.e -ve only, so append in stack
                if not stack or stack[-1] < 0:  
                    stack.append(num)
                # if magnitude of both equal then both will get cancelled, so pop from stack.
                elif stack[-1]== abs(num):
                    stack.pop()
        return stack

# https://leetcode.com/problems/asteroid-collision/solutions/109666/python-o-n-stack-based-with-explanation/
# https://leetcode.com/problems/asteroid-collision/solutions/109694/java-c-clean-code/