class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Zip the names and heights together and sort by height in descending order
        sorted_people = sorted(zip(heights, names), reverse=True)
        # Extract the names from the sorted list
        ans = [name for height, name in sorted_people]
        return ans

# java
"""
// Note: Name is of string and height is of 'int' type so we can't take inside an array
// that's why made on class 'pair' to store value of different data types.

class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        // Create a list of pairs of heights and names
        List<Pair> people = new ArrayList<>();
        for (int i = 0; i < names.length; i++) {
            people.add(new Pair(heights[i], names[i]));
        }

        // Sort the list by heights in descending order
        Collections.sort(people, (a, b) -> b.height - a.height);

        // Extract the sorted names
        String[] sortedNames = new String[names.length];
        for (int i = 0; i < people.size(); i++) {
            sortedNames[i] = people.get(i).name;
        }

        return sortedNames;
    }

    // Helper class to store the pair of height and name
    private static class Pair {
        int height;
        String name;

        Pair(int height, String name) {
            this.height = height;
            this.name = name;
        }
    }
}

// Other way of writing same code
// No need to create 'pair' class , just use 'Object' class.

class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        // Create a list of arrays to store the height and name pairs
        List<Object[]> people = new ArrayList<>();
        for (int i = 0; i < names.length; i++) {
            people.add(new Object[]{heights[i], names[i]});
        }

        // Sort the list by heights in descending order
        people.sort((a, b) -> (int)b[0] - (int)a[0]);

        // Extract the sorted names
        String[] sortedNames = new String[names.length];
        for (int i = 0; i < people.size(); i++) {
            sortedNames[i] = (String)people.get(i)[1];
        }

        return sortedNames;
    }
"""

# method 2:
# Note: This is working because 'height' is distinct otherwise won't work.
class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        n: int = len(names)
        mapping: dict[int, str] = {}  # height -> name (heights are distinct)
        for ind in range(n):
            mapping[heights[ind]] = names[ind]

        heights.sort(reverse=True)
        for ind in range(n):
            h: int = heights[ind]
            names[ind] = mapping[h]

        return names
