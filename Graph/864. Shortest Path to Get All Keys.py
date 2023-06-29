# Note vvi: It is asking the minimum moves not the shortest path.


# My approach:
# vvi: will wrong ans when there is lock and their key is adjacent to any cell.
# ["@.a..","###.#","b.A.c",".C.B."]

# This will give the shortest path(shortest distance) from start till when we will get the last key.
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        # find the starting point and count the no of key
        start , keyCount = None , 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = [i, j]
                if grid[i][j].islower():
                    keyCount += 1
        print(start, keyCount)
        q = collections.deque()
        q.append((0, start[0], start[1]))  # [move, cell]
        keyAcquired = set()
        visited = set()
        visited.add((start[0], start[1]))
        directions = [[0, -1] ,[0, 1], [-1, 0], [1, 0]]   # left, right, up ,down
        while q :
            print(q)
            move, r, c = q.popleft()
            if grid[r][c].islower():
                keyAcquired.add(grid[r][c])
                if len(keyAcquired) == keyCount:
                            return move
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] != '#':
                    # if key 
                    if grid[nr][nc].islower():
                        # if len(keyAcquired) == keyCount - 1:
                        #     return move + 1
                        q.append((move + 1 , nr, nc))
                        visited.add((nr, nc))
                    elif grid[nr][nc].isupper():
                        if grid[nr][nc].lower() in keyAcquired:
                            q.append((move + 1 , nr, nc))
                            visited.add((nr, nc))
                    else:
                        q.append((move + 1 , nr, nc))
                        visited.add((nr, nc))
        return -1


# Method 1:
# working one and easier one

# Logic: To solve the above problem, we need to travsere the same cell again i.e first get the key and then get the respective lock.
# so here to mark visited we will add the path also because when it will go to that cell again to get the key &
#  again come back then path will be differnt and should be allowed.

# When we will find any key then we will add their lock into the path(i.e keys variable).

#Time complexity: O(mn2^k) or O(m*n*k!). Have to ask someone

# Note: if asked for shortest distance between start and cell where we will get the last key 
# then the above method will work.
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        # find the starting point and count the no of key
        start , keyCount = None , 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = [i, j]
                if grid[i][j].islower():
                    keyCount += 1
        directions = [[0, -1] ,[0, 1], [-1, 0], [1, 0]]   # left, right, up ,down
        q = collections.deque()
        q.append((start[0], start[1], 0, ".@abcdef", 0))  # (r, c, moves , keys , acquiredKey)
                        # key contain the possible move we can take i.e except wall and lock
        visited = set()
        while q :
            r, c, moves , keys , acquiredKey = q.popleft()
            # check if this is a new key we found
            if grid[r][c] in "abcdef" and grid[r][c].upper() not in keys:
                keys += grid[r][c].upper()   # Add the lock into keys
                acquiredKey += 1
            if acquiredKey == keyCount:
                return moves
            # now traverse 4 directions
            for dr, dc in directions:
                nr , nc = r + dr, c + dc
                # check if we can visit this cell
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] in keys and (nr, nc, keys) not in visited:
                    visited.add((nr, nc, keys))
                    q.append((nr, nc, moves + 1, keys, acquiredKey))

        return -1


# Note: chekcing if it is a new key at first time, will give the wrong ans.
# same reason as above
# If we will do like this.

# while q :
#     print(q)
#     r, c, moves , keys , acquiredKey = q.popleft()
#     # check if this is a new key we found
            
#     # now traverse the other 4 directions
#     for dr, dc in direc:
#         nr , nc = r + dr, c + dc
#         if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] in keys and (nr, nc, keys) not in visited:
#             if grid[r][c] in "abcdef" and grid[i][j].upper() not in keys:
#                 keys += grid[r][c].upper()
#                 acquiredKey += 1
#                 if acquiredKey == numOfKeys:
#                     return moves
#             visited.add((nr, nc, keys))
#             q.append((nr, nc, moves + 1, keys, acquiredKey))
#         return -1


# Method 2: Try to do by Bfs + bitmasking


