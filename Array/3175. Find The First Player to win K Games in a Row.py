# method 1:
# just do whatever telling to do.
# for this we will need a deque.

# Time : O(n), little > O(n)
# space = O(n)
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        if n == 2:
            return 0 if skills[0] > skills[1] else 1
        if k >= n:
            # index having max value will be our ans
            return skills.index(max(skills))
        consecutive_wins = 0
        current_winner = 10 ** 6
        q = deque([[skills[i], i ] for i in range(n)])
        while True:
            num1, i1 = q.popleft()
            num2, i2 = q.popleft()
            if num1 > num2:
                if current_winner == i1:
                    consecutive_wins += 1
                else:
                    consecutive_wins = 1
                    current_winner = i1
                if consecutive_wins == k:
                    return i1
                q.appendleft([num1, i1])
                q.append([num2, i2])
            else:
                if current_winner == i2:
                    consecutive_wins += 1
                else:
                    consecutive_wins = 1
                    current_winner = i2
                if consecutive_wins == k:
                    return i2
                q.appendleft([num2, i2])
                q.append([num1, i1])


# method 2: Best and concise
# Logic: If we don't find the winner after one pass,
# the winner will be max(A), bacause no one will beats him anymore.

# just do operation for one pass on paper then you will get clear visualization of it.

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        consecutive_wins = 0
        current_winner = 0
        for i in range(1, n):
            if skills[i] > skills[current_winner]:
                current_winner  = i   # change the winner
                consecutive_wins = 0
            consecutive_wins += 1
            if consecutive_wins == k:
                return current_winner
        # if not able to find ans in one pass then return index of maximum element.
        return skills.index(max(skills))


# Similar q:
# 1) 1535. Find the Winner of an Array Game
# exactly same question.
# only diff: In this we have to return number directly not index.
