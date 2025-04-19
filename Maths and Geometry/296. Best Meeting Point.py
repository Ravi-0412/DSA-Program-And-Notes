# just same logic as :" 462. Minimum Moves to Equal Array Elements II".

# Point should be median point of all 'x' and all 'y' coordinates where house is present respectively.

def findBestMeetingPoint(mat):
    n, m= len(mat), len(mat[0])
    # first store all 'x' and 'y' coordinates where house is present in separate arrays.
    x, y = [], []
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                x.append(i)
                y.append(j)
    # Get the median of 'x' and 'y' coordiantes.
    # sort both x and y coordinates of all houses
    x.sort()
    y.sort()
    lx, ly= len(x), len(y)
    median_x= x[lx//2] if lx % 2 else (x[lx//2] + x[lx//2 -1]) //2
    median_y= y[ly//2] if ly % 2 else (y[ly//2] + y[ly//2 -1]) //2
    median = (median_x, median_y)   # our meeting point
    # Now calculate the cost of all houses from median point
    cost = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                cost += abs(median_x - i) + abs(median_y - j)
    return cost

# Java
"""
import java.util.*;

public class MeetingPointFinder {

    public static int findBestMeetingPoint(int[][] mat) {
        int n = mat.length;
        int m = mat[0].length;

        List<Integer> x = new ArrayList<>();
        List<Integer> y = new ArrayList<>();

        // Collect coordinates of all the houses
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (mat[i][j] == 1) {
                    x.add(i);
                    y.add(j);
                }
            }
        }

        // Sort the coordinates
        Collections.sort(x);
        Collections.sort(y);

        int medianX = getMedian(x);
        int medianY = getMedian(y);

        int cost = 0;

        // Calculate total distance to the meeting point
        for (int i = 0; i < x.size(); i++) {
            cost += Math.abs(x.get(i) - medianX) + Math.abs(y.get(i) - medianY);
        }

        return cost;
    }

    private static int getMedian(List<Integer> list) {
        int size = list.size();
        if (size % 2 == 1) {
            return list.get(size / 2);
        } else {
            return (list.get(size / 2) + list.get(size / 2 - 1)) / 2;
        }
    }
"""
