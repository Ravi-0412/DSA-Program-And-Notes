# how to think about Dijkastra?
# Ans: we have given a source node and initial step (0) and we have to reach the destination with the help of the these fixed nodes.
# And also we will encounter diff diff states(numbers) and every time we have to min from them and check for ans.
# These things are same as Dijkastra.

# Note: Here we don't need heap because:
# 1) Since we will get the ans for generating number at 1st time we will get that number.
# 2) There is nothing like diff diff distance/time/cost associated with each operation that can change the ans(minimum steps) for genearting number later.
# so we don't heap heap to keep track of minimum steps.

# Note: we can return the steps by checking at first time itself.

# for visited set: we only need to mark the generating num(curr_num) as visited at 1st time since that will be minimum no of steps for that number.


import collections
class Solution:
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        q= collections.deque()
        mod= 100000
        q.append((start, 0))
        visited= set()
        visited.add(start)
        while q:
            n, steps= q.popleft()
            for num in arr:
                cur_num= (num * n) % 100000
                if cur_num== end:
                    return steps + 1
                if cur_num not in visited:
                    visited.add(cur_num)
                    q.append((cur_num, steps + 1))
        return -1
    



# Striver one but mine one(above one) is very very good.
class Solution:
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        q= collections.deque()
        mod= 100000
        distance= [9999] *100000
        distance[start]= 0
        q.append((start, 0))
        visited= set()
        visited.add((start, 0))
        while q:
            n, steps= q.popleft()
            if n== end:
                return steps
            # now check the poped ele with all ele in the array.
            for num in arr:
                cur_num= (num * n) % 100000
                if distance[cur_num] > 1 + steps and (cur_num, steps +1) not in visited:
                    distance[cur_num]= 1 + steps
                    q.append((cur_num, steps + 1))
                    visited.add((cur_num, steps + 1))
        return -1