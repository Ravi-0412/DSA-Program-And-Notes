# method 1: using dfs
# time: O(ElogE +(V+E))= O(ElogE)
# space: O(E)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dept_to_dest= collections.defaultdict(list)
        # to get the edges in ascending order just sort the edges in descending order
        # now add the adjacent vertices into hashmap. Edges bigger in lexographic order will come first so we can take the last one just by poping and that will be lexographically small
        for dept,dest in sorted(tickets,reverse= True):
            dept_to_dest[dept].append(dest)
        route= []
        
        def dfs(airport):
            while dept_to_dest[airport]:  # go till it get stuck and traverse back
                dfs(dept_to_dest[airport].pop())  # it will always take the path with less lexographical order in case of more than one path
            route.append(airport)  # if got stuck then append it to the ans
        
        dfs('JFK')
        return route[::-1]


# method 2: converted the above code into iterative form
# time: O(ElogE +(V+E))= O(ElogE)
# space: O(E)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dept_to_dest= collections.defaultdict(list)
        # to get the edges in ascending order just sort the edges in descending order
        # now add the adjacent vertices into hashmap. Edges bigger in lexographic order will come first so we can take the last one just by poping 
        for dept,dest in sorted(tickets,reverse= True):  # will get sorted according to the 1st item, if tie then according to the 2nd item
            dept_to_dest[dept].append(dest)
        stack,ans= [],[]
        stack.append('JFK')
        while stack:
            while dept_to_dest[stack[-1]]:
                dest= dept_to_dest[stack[-1]].pop()  # if more than two paths are possible then it will take the path with lesser lexographic order 
                stack.append(dest)
            # when you get stuck then pop and add to the ans
            ans.append(stack.pop())
        return ans[::-1]