# logic: 
"""
When you see that given a source/index , you can go to some other point/ index &&
using those enext points you can go some other point and so on.
Then must think of bfs / multisource bfs or dfs.
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        dq = deque()
        visited = set()
        dq.append(0)
        visited.add(0)
        while dq:
            key = dq.popleft()
            for room in rooms[key]:
                if room not in visited:
                    dq.append(room)
                    visited.add(room)
        return len(visited) == n   # if len(visited) == n then, we can enter all rooms.
