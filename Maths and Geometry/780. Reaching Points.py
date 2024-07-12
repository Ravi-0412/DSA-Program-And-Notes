# Brute force: For every points we have two choice to go.

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        dq = collections.deque()
        dq.append((sx, sy))
        while dq:
            for i in range(len(dq)):
                x, y = dq.popleft()
                if x == tx and y == ty:
                    return True
                if x + y <= ty:
                    dq.append((x, x + y))
                if x + y <= tx:
                    dq.append((x + y, y))
        return False

# Method 2: Optimisation 
# Go reverse i.e from (tx, ty) -> (sx, sy).
# while going reverse the operation also like : '+' -> '-'
# Logic: 1) We can reach every point through one way only (if '0' is not allowed).
# 2) so we can go bottom up and and try to reduce (tx, ty) to some nearby points (sx, sy).
# i.e we can start from (tx,ty) and go up till you hit one of the condition like sx >= tx or sy>= ty.
# 3) After reducing we can directy check if it is possible to reach or not.
# How?
# after reducing we will have two case:
# i) sx == tx and sy <= ty.
# In this case we need to verify if we can reach 'ty' from '(sx, sy)' or not.
# for this ' (ty-sy)%sx == 0', why?
# sy will translate to ty only by (sx+sy), if they translate then (sx, sy+k*sx) = ty for some k
# sy+k*sx = ty => (ty-sy) / sx = k.

# ii) sy == ty and sx <= tx
# in this case , (ty-sy)%sx == 0

# time: O(log(n)) where n = Max(tx,ty)

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx and sy < ty:
            if ty > tx:
                ty %= tx   # '%' is same as mutiple '-' operation.
            else:
                tx %= ty
        return (sx == tx and sy <= ty and (ty - sy) % sx == 0) or (sy == ty and sx <= tx and (tx - sx) % sy == 0)
