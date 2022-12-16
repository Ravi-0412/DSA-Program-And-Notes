# submitted on lintcode
def findFirstBadVersion(self, n):
        low, up= 1, n
        while low < up:
            mid= low + (up- low)//2
            if SVNRepo.isBadVersion(mid):  # then search for even more smaller
                up= mid
            else:  # else we have to find the greater one.
                low= mid+ 1
        return low
