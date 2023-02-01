# how to think about Dijkastra?
# Ans: we have given a source node and initial step (0) and we have to reach the destination with the help of the node distances.
# no of node will be from '0' to '9999' .
# And also we will encounter diff diff path while finding the ans.
# These things are same as Dijkastra.

# here there is no need of priority Q, a simple Q will also work.
# since we can get same num with same steps so used visited so that the num doesn't repeat and get added to Q.


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