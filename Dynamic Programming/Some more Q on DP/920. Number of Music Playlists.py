# Logic: for filling the song at current position in current playlist there is two choice:
# 1) use any song among already used song .
# But given 'A song can only be played again only if k other songs have been played.' 
# means we can use the same song again if >= 'k' song is played in between after that song.
# so no of choices in this case = 'unique_songs -k' , 'unique_songs' = no of unique_songs used till now.

# 2) when we use new song.
# in this case no of choices = 'n-unique_songs'

# In both case no of listened songs will increase by '1' and no of 'unique_songs' will depend on cases.


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10**9 + 7

        def dfs(listened_songs, unique_songs):
            if listened_songs == goal:
                # no remaining song to listen, then we need to check whether we have used all songs or not.
                # If used all songs then it is one of the possible ways
                return unique_songs == n
            if (listened_songs, unique_songs) in dp:
                return dp[(listened_songs, unique_songs)]
            # 1) use any song among already used song 
            ans= dfs(listened_songs + 1, unique_songs) * max(0, unique_songs - k)   # to avoid negative indexinng taking max
            # 2) when we use new song
            ans += (dfs(listened_songs + 1, unique_songs + 1) * (n - unique_songs)) % mod
            dp[(listened_songs, unique_songs)] = ans
            return ans 
        dp = {}
        return dfs(0, 0)
    

# When doing using dp array with (goal +1)*(n+1), it's giving wrong ans don't know why.
# Have to ask someone

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10**9 + 7

        def dfs(listened_songs, unique_songs):
            if listened_songs == goal:
                # no remaining song to listen, then we need to check whether we have used all songs or not.
                # If used all songs then it is one of the possible ways
                return unique_songs == n
            print(listened_songs, unique_songs)
            if dp[listened_songs][unique_songs] != -1:
                return dp[listened_songs][unique_songs]
            ans= dfs(listened_songs + 1, unique_songs) * max(0, unique_songs - k)
            ans += (dfs(listened_songs + 1, unique_songs + 1) * (n - unique_songs)) % mod
            dp[listened_songs][unique_songs] = ans
            return ans 
        # dp = [[-1 for j in range(n + 1)] for i in range(goal + 1)]
        # dp = [[-1 for j in range(109)] for i in range(109)]   # this one goving correct ans
        return dfs(0, 0)


# Have to by Tabulation also after clearing the doubt of constraint



# Another way:
# if we choose the cur song based on pre one.

# the key part of this problem is to figure out what is the sub problem. 
# in this case the sub problem is to use j songs out of N songs to fill i slots (i < L). the sub problem is not using a total of j songs to fill i slots.
# realizing this, then we can start the induction process:

# for problem d[i][j] it means filling i slots, using j out of N songs:

# the last slot could either be an existing song, in this case we need to look at d[i-1][j] and we have j-k choices for the last slot
# or the last slot could be a new song from the remaining unused songs, then we need to look at d[i-1][j-1] and we have N - j + 1 choices for the last slot.
# then we get d[i][j] = d[i-1][j-1] * (N - j + 1) + d[i-1][j] * (j - k)