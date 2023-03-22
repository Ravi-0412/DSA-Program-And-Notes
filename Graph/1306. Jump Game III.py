# logic for every index we have two choice.
# but we can go into infinite loop so we have to mark the index we have already visited to avoid that path again
# for marking we can use hashmap or arr.
# but here we can do in same array itself by changing the sign since 1) all ele given is positive only
# 2) the choice we have to consider is one positive and one negative with each index so if we if change the sign.
# 'start + arr[start]' will become 'start -  arr[start]' and 'start - arr[start]' will become 'start + arr[start]' which will not affect our choice and finally ans also.

# logic: when we are at index 'i' we can check if its value is= 0 else will check for position we can reach from 'i' and so on.
# since we have to repeat the same thing for each position, it gives idea of recursion.

# time: O(n)
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if start < 0 or start >= len(arr) or arr[start] < 0:  # checking out of bound and if already visited
            return False
        arr[start]= -arr[start]  # marking already visited by changing sign. 
        return arr[start] == 0  or self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])
        # return start== 0  or self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])  # my mistake instead of checking value i was checking index


# iterative way 
# just totally same as multisource bfs i.e given a source we can take some steps with the help of curr one and so on till we find answers.
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

# in above one we are marking visited after poping.
# But we can mark visited just after we will see any index.
# Since need to traverse any index only one as every time that index will give the same result.

# 1) marking visited in array value itself.
# Here we are changing the value just when we see so opposite the chekcing condition because we have already chenged the sign of val at cur index.
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q= collections.deque([start])
        arr[start]= -arr[start]
        while q:
            cur= q.popleft()
            if arr[cur]== 0:
                return True   
            if  cur - arr[cur] < len(arr) and arr[cur - arr[cur]] >=0: # need to check upper bound in this case.
                q.append(cur - arr[cur])
                arr[cur - arr[cur]]= -arr[cur - arr[cur]]
            if  cur + arr[cur] >=0 and arr[cur + arr[cur]] >= 0:  # need to check lower bound in this case.
                q.append(cur + arr[cur])
                arr[cur + arr[cur]]= -arr[cur + arr[cur]]
        return False
    
# 2) taking set for marking visited
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q= collections.deque([start])
        visited= set()
        visited.add(start)
        while q:
            cur= q.popleft()
            if arr[cur]== 0:
                return True   
            if  cur + arr[cur] < len(arr) and (cur + arr[cur]) not in visited: # only need to check upper bound in this case.
                q.append(cur + arr[cur])
                visited.add(cur + arr[cur])
            if  cur - arr[cur] >=0 and (cur - arr[cur]) not in visited:  # only need to check lower bound in this case.
                q.append(cur - arr[cur])
                visited.add(cur + arr[cur])
        return False
