# Method 1: 

# Logic: Person who will know the secret will tell all his connected persons.
# Person who come to know the secret at less time will tell more person.

# Hmko max person ko include karna h answer me isliye hm chahenge ki koi person
# jitna kam time me secret jane taki aage wale ko kam time me bta sake ans so on & finally mera ans me maximum log 
# include ho jayega.

# For this we need to pop person according to lesser time.
# we want as lesser time for every person to include max person in our ans. => minHeap

# Note: But when any person will come the secret that may not be the least time for that person,
# that person can know the secret at more lesser time by other person.
# Just same as Dijkastra. mark visited only after poping.

# Note: So when you will mark any person visited, when you will see them for 1st time like bfs then,
# You will get wrong ans. You will get less no of people than expected. 

# Time: Same as Dijkastra

# My mistakes
# 1) Sorting acc to time and checking all the meetings and adding in ans according to them.
# Error why? 
# say there are meetings like : [11, 1, 2] , [11, 3, 2] : [t, x, y] and suppose person 0 and person 3 knows the secret till now.
# Then for [11, 1, 2] we won't add in ans but it should be because at time = 11, person 2 will know the secret from peron 3 
# i.e [11, 3, 2]  and can tell person '1' at the same time.
# So we will get less answer in this case. This is happeining because of many meeting at the same time.
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings = [[t, x, y] for x, y, t in meetings]
        meetings.sort()
        knows = set()
        knows.add(0)
        knows.add(firstPerson)

        for t, x, y in meetings:
            if x in knows or y in knows:
                knows.add(x)
                knows.add(y)
        return list(set(knows))]
    
# 2) To solve above problem, i thought to add perosn [time: all_person_that_can_know_secret_at_this_time]

# Why wrong:
# Suppose there is lot of meeting going at same time and here we are adding all the persons that are involved in 
# any meeting at that time.
# But not all person can come to know the secret in all possible meetings.
    
# so in this case we will get the more number than expected.

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meeting = collections.defaultdict(set)
        knows = {0, firstPerson}
        maxTime = 0
        for x,y, t in meetings:
            meeting[t].add(x)
            meeting[t].add(y)
            maxTime = max(maxTime, t)
        time = 0
        while time <= maxTime :
            time += 1
            if time not in meeting :
                continue
            for p in meeting[time]:
                if p in knows:
                    knows.update(meeting[time])
                    break
        return list(knows)


# 3) Marking visited when we will see any person for first time.


# Correct method 

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = collections.defaultdict(list)  # list of person with time with whome he can share the secret.
        for x, y, t in meetings:
            graph[x].append((y, t))
            graph[y].append((x, t))
        
        minHeap = []
        heapq.heappush(minHeap, (0, 0))    # (time_at_which_person_knows_secret, person
                    # this person can tell secret to other person having >= this time.
        heapq.heappush(minHeap, (0, firstPerson))
        knows = set()   # will only add once that person will share secret with all the possible person
        while minHeap :
            time, person = heapq.heappop(minHeap)
            if person in knows:
                continue
            # This person knows the secret and now share with other person
            knows.add(person)
            for p, t in graph[person]:
                if p not in knows and t >= time:   # because of time condition a lot of meeting will be get discarded
                    # will only tell if timing 't' will be >= time
                    heapq.heappush(minHeap, (t, p))
        return list(knows)


# Java
"""
import java.util.*;

class Solution {
    public List<Integer> findAllPeople(int n, int[][] meetings, int firstPerson) {
        Map<Integer, List<int[]>> graph = new HashMap<>(); // list of person with time with whom he can share the secret.
        for (int[] meet : meetings) {
            int x = meet[0], y = meet[1], t = meet[2];
            graph.computeIfAbsent(x, k -> new ArrayList<>()).add(new int[]{y, t});
            graph.computeIfAbsent(y, k -> new ArrayList<>()).add(new int[]{x, t});
        }

        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        minHeap.offer(new int[]{0, 0});          // (time_at_which_person_knows_secret, person)
        minHeap.offer(new int[]{0, firstPerson});

        Set<Integer> knows = new HashSet<>();   // will only add once that person will share secret with all the possible person

        while (!minHeap.isEmpty()) {
            int[] curr = minHeap.poll();
            int time = curr[0], person = curr[1];

            if (knows.contains(person)) continue;

            // This person knows the secret and now share with other person
            knows.add(person);

            if (!graph.containsKey(person)) continue;

            for (int[] neighbor : graph.get(person)) {
                int p = neighbor[0], t = neighbor[1];
                if (!knows.contains(p) && t >= time) {   // because of time condition a lot of meeting will be discarded
                    minHeap.offer(new int[]{t, p});
                }
            }
        }

        return new ArrayList<>(knows);
    }
}


"""


# C++
"""
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        unordered_map<int, vector<pair<int, int>>> graph; // list of person with time with whom he can share the secret.
        for (auto& meet : meetings) {
            int x = meet[0], y = meet[1], t = meet[2];
            graph[x].emplace_back(y, t);
            graph[y].emplace_back(x, t);
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> minHeap;
        minHeap.emplace(0, 0);          // (time_at_which_person_knows_secret, person)
        minHeap.emplace(0, firstPerson);

        unordered_set<int> knows;       // will only add once that person will share secret with all the possible person

        while (!minHeap.empty()) {
            auto [time, person] = minHeap.top(); minHeap.pop();

            if (knows.count(person)) continue;

            // This person knows the secret and now share with other person
            knows.insert(person);

            for (auto& [p, t] : graph[person]) {
                if (!knows.count(p) && t >= time) {   // because of time condition a lot of meeting will be discarded
                    minHeap.emplace(t, p);
                }
            }
        }

        return vector<int>(knows.begin(), knows.end());
    }
};

"""


