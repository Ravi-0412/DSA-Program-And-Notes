# logic for every index we have two choice.
# but we can go into infinite loop so we have to mark the index we have already viisted to avoid that path again
# for marking we can use hashmap or arr.
# but here we can do in same array itself by changing the sign since 1) all ele given is positive only
# 2) the choice we have to consider is one positive and one negative with each index so if we if change the sign.
# 'start + arr[start]' will become 'start -  arr[start]' and 'start - arr[start]' will become 'start + arr[start]' which will not affect our choice and finally ans also.

# time: O(n)
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if start < 0 or start >= len(arr) or arr[start] < 0:  # checking out of bound and if already visited
            return False
        arr[start]= -arr[start]  # marking already visited by changing sign. 
        return arr[start] == 0  or self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])
        # return start== 0  or self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])  # my mistake instead of checking value i was checking index


# iterative way 
# we can also mark the node visited when we see first time i.e while appending only. it will also work but code will be lengthy and not much concise and clear.
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q= collections.deque([start])
        while q:
            cur= q.popleft()
            if arr[cur]== 0:
                return True   
            if arr[cur] < 0:  # if already visited
                continue         
            # now traverse the possible choice if not out of bound
            if  cur + arr[cur] < len(arr) : # only need to check upper bound in this case.
                q.append(cur + arr[cur])
            if  cur - arr[cur] >=0:  # only need to check lower bound in this case.
                q.append(cur - arr[cur])
            arr[cur]= -arr[cur]   # marking as visited when we have checked all possibility at any node.
        return False