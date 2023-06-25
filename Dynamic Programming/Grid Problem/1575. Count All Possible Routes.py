# Logic: We will only stop when our fuel will becom empty 

# Steps:
# Start from the start index, and visit all cities except start.
# Continue this process recursively.
# If you reach end index, do:
# Now, we have atleast 1 way of reaching end so add this 1 possible way to the answer.
# Continue recursion, since there might be more ways to get back from end to end using other cities.
# If fuel < 0, there is no further way left.

# time: O(n^2 * fuel)
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n= len(locations)
        mod = 10**9 + 7

        @lru_cache(None)
        def solve(curCity, fuel): # number of ways to reach finish, when we are at city `curCity` with fuel `fuel`
            if fuel < 0:   # <= 0 will give the wrong ans as we are checking after reducing the fuel in function call.
                return 0
            # If we have reached the destination ans= 1 else 0 but don't return from here.
            # Because we may again come back to destination taking other paths in current route.
            ans = 1 if curCity == finish else 0
            # Now traverse each possible city from the curCity except curCity.
            for nextCity in range(n):
                if nextCity != curCity:
                    ans = ans + solve(nextCity , fuel - abs(locations[nextCity] - locations[curCity]))
            return ans % mod

        return solve(start, fuel)