# Methoe 1: Better

"""
Logic: for given point, find if there exist any diagonal.
Note: we can say two points (x1, y1) & (x2, y2) are diagonal of a square if:
abs(x1 - x2) == abs(y1 - y2). Just checking diff between values of 'x' and 'y' coordinate should be same for equal length.
If they are diagonal then:
1) length of square we can form taking these two points as diagonals = abs(x1 - x2) or abs(y1- y2).
2) Other two sides of square will be '(x1, y2)' and '(x2, y1)'.

so for finding the total count , multiply the occurences of other diagonal and other two points.
Time: add: O(1)
count: O(T), where T <= 5000 is total number of points after calling add.
Space: O(T)

Note: in same way you can form rectangle.
In case of rectangle any two points can be diagonal, won't follow property like square 'abs(x1 - x2) == abs(y1 - y2)'.
So consider each possible diagonal pair then other two points will be same as square i.e '(x1, y2)' and '(x2, y1)'.
Do Q: '939. Minimum Area Rectangle' based on rectangle.
"""

from collections import defaultdict
class DetectSquares:
    def __init__(self):
        # self.ptsCount= Counter()  # store the no of occurence of each point
        self.ptsCount = {}
        
    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] = 1 + self.ptsCount.get(tuple(point), 0)
        
    def count(self, point: List[int]) -> int:
        res= 0 
        px, py= point
        # find if there any diagonal exist for this point.
        # diagonal will be only present if abs(px -x)== abs(py -y) i.e horizontal and vertical length should be equal.
        for (x, y), cnt in self.ptsCount.items():
            if (abs(px -x)!= abs(py - y)) or px== x or py==y :  # 2nd case for +ve area. it can form square with its duplictes but area will be '0'.
                continue
            # now we have found the diagonal, now search if other two points exists.
            # if exists then add the count of those in the result(after multiplying).
            # coordinates of other two points will be (x, py) and (px, y),
            # if they will form square with the these two points(diagonal one) i.e (x, y) and (px, py)
            res += cnt * self.ptsCount.get((x, py), 0) * self.ptsCount.get((px, y), 0)
        return res

# Java
"""
import java.util.*;

class DetectSquares {
    Map<List<Integer>, Integer> ptsCount;

    public DetectSquares() {
        // self.ptsCount = {}  -> store the no of occurrence of each point
        ptsCount = new HashMap<>();
    }

    public void add(int[] point) {
        List<Integer> key = Arrays.asList(point[0], point[1]);
        ptsCount.put(key, ptsCount.getOrDefault(key, 0) + 1);
    }

    public int count(int[] point) {
        int res = 0;
        int px = point[0], py = point[1];

        // find if there any diagonal exist for this point.
        // diagonal will be only present if abs(px - x) == abs(py - y) i.e. horizontal and vertical length should be equal.
        for (Map.Entry<List<Integer>, Integer> entry : ptsCount.entrySet()) {
            int x = entry.getKey().get(0);
            int y = entry.getKey().get(1);
            int cnt = entry.getValue();

            if (Math.abs(px - x) != Math.abs(py - y) || px == x || py == y) {
                // 2nd case for +ve area. it can form square with its duplicates but area will be '0'.
                continue;
            }

            // now we have found the diagonal, now search if other two points exist.
            // if exists then add the count of those in the result (after multiplying).
            // coordinates of other two points will be (x, py) and (px, y),
            // if they will form square with these two points(diagonal one) i.e. (x, y) and (px, py)
            res += cnt *
                   ptsCount.getOrDefault(Arrays.asList(x, py), 0) *
                   ptsCount.getOrDefault(Arrays.asList(px, y), 0);
        }

        return res;
    }
}
"""

# C++
"""
#include <vector>
#include <map>
using namespace std;

class DetectSquares {
    map<pair<int, int>, int> ptsCount;

public:
    DetectSquares() {
        // ptsCount = {}  -> store the no of occurrence of each point
    }

    void add(vector<int> point) {
        pair<int, int> p = {point[0], point[1]};
        ptsCount[p]++;
    }

    int count(vector<int> point) {
        int res = 0;
        int px = point[0], py = point[1];

        // find if there any diagonal exist for this point.
        // diagonal will be only present if abs(px - x) == abs(py - y) i.e. horizontal and vertical length should be equal.
        for (auto& [p, cnt] : ptsCount) {
            int x = p.first;
            int y = p.second;

            if (abs(px - x) != abs(py - y) || px == x || py == y) {
                // 2nd case for +ve area. it can form square with its duplicates but area will be '0'.
                continue;
            }

            // now we have found the diagonal, now search if other two points exist.
            // if exists then add the count of those in the result (after multiplying).
            // coordinates of other two points will be (x, py) and (px, y),
            // if they will form square with these two points(diagonal one) i.e. (x, y) and (px, py)
            res += cnt *
                   ptsCount[{x, py}] *
                   ptsCount[{px, y}];
        }

        return res;
    }
};
"""

# Method 2: 
# Given p1, try all points p2 (same x-axis) then compute the positions of 2 remain points p3, p4.

# To compute count(p1):
# We try all the points p2 which has the same x-axis with p1, it means p2.x = p1.x
# Since we have 2 points p1 and p2, we can form a square by computing the positions of 2 remain points p3, p4.
# Calculate sideLen = abs(p1.y - p2.y)
# Case 1: p3, p4 points are in the left side of line p1p2
# p3 = (p1.x - sideLen, p2.y)
# p4 = (p1.x - sideLen, p1.y)
# Case 2: p3, p4 points are in the right side of line p1p2
# p3 = (p1.x + sideLen, p2.y)
# p4 = (p1.x + sideLen, p1.y)

# Time: add: O(1)
# count: O(T), where T <= 5000 is total number of points after calling add.
# Space: O(T)

class DetectSquares:
    def __init__(self):
        self.xPoints = defaultdict(list)
        self.cnt = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.xPoints[x].append(y)
        self.cnt[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        ans = 0
        for y2 in self.xPoints[x1]:
            if y2 == y1: continue  # Skip empty square
            sideLen = abs(y2 - y1)

            # Case: p3, p4 points are in the left side
            x3, y3 = x1 - sideLen, y2
            x4, y4 = x1 - sideLen, y1
            ans += self.cnt[(x3, y3)] * self.cnt[(x4, y4)]

            # Case 2: p3, p4 points are in the left side
            x3, y3 = x1 + sideLen, y2
            x4, y4 = x1 + sideLen, y1
            ans += self.cnt[(x3, y3)] * self.cnt[(x4, y4)]
        return ans

# Java
"""
import java.util.*;

class DetectSquares {
    private Map<Integer, List<Integer>> xPoints = new HashMap<>();
    private Map<List<Integer>, Integer> cnt = new HashMap<>();

    public void add(int[] point) {
        int x = point[0], y = point[1];
        xPoints.computeIfAbsent(x, k -> new ArrayList<>()).add(y);
        List<Integer> key = Arrays.asList(x, y);
        cnt.put(key, cnt.getOrDefault(key, 0) + 1);
    }

    public int count(int[] point) {
        int x1 = point[0], y1 = point[1], ans = 0;
        List<Integer> yList = xPoints.getOrDefault(x1, new ArrayList<>());
        for (int y2 : yList) {
            if (y2 == y1) continue; // Skip empty square
            int sideLen = Math.abs(y2 - y1);

            // Case: p3, p4 points are in the left side
            int x3 = x1 - sideLen, y3 = y2;
            int x4 = x1 - sideLen, y4 = y1;
            ans += cnt.getOrDefault(Arrays.asList(x3, y3), 0) *
                   cnt.getOrDefault(Arrays.asList(x4, y4), 0);

            // Case: p3, p4 points are in the right side
            x3 = x1 + sideLen;
            x4 = x1 + sideLen;
            ans += cnt.getOrDefault(Arrays.asList(x3, y3), 0) *
                   cnt.getOrDefault(Arrays.asList(x4, y4), 0);
        }
        return ans;
    }
}
"""

# C++
"""
#include <unordered_map>
#include <vector>
#include <utility>
#include <cmath>

using namespace std;

class DetectSquares {
public:
    unordered_map<int, vector<int>> xPoints;
    unordered_map<long long, int> cnt;

    void add(vector<int> point) {
        int x = point[0], y = point[1];
        xPoints[x].push_back(y);
        long long key = ((long long)x << 32) | y;
        cnt[key]++;
    }

    int count(vector<int> point) {
        int x1 = point[0], y1 = point[1], ans = 0;
        for (int y2 : xPoints[x1]) {
            if (y2 == y1) continue; // Skip empty square
            int sideLen = abs(y2 - y1);

            // Case: p3, p4 points are in the left side
            int x3 = x1 - sideLen, y3 = y2;
            int x4 = x1 - sideLen, y4 = y1;
            ans += cnt[((long long)x3 << 32) | y3] * cnt[((long long)x4 << 32) | y4];

            // Case: p3, p4 points are in the right side
            x3 = x1 + sideLen;
            x4 = x1 + sideLen;
            ans += cnt[((long long)x3 << 32) | y3] * cnt[((long long)x4 << 32) | y4];
        }
        return ans;
    }
};
"""
