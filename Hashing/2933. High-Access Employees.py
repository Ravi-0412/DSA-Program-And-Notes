# Logic: 
"""
For each employee, sort their access times.
Check if there are any three access times that fall within any 100-minute window.
If such a window exists, mark the employee as high-access.

q) Why 100 minutes?
basically, 5:32 to 6:21, 08:08 to 09:07 it is converted to 532 to 621 and 808 to 907. 
"""


from collections import defaultdict

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        # Create a dictionary to store access times for each employee.
        access_map = defaultdict(list)
        
        # Populate the dictionary with access times from the input list.
        for employee, time in access_times:
            access_map[employee].append(int(time))
        
        # List to store the names of high-access employees.
        high_access_employees = []
        
        # Iterate through the dictionary to check access patterns for each employee.
        for employee, times in access_map.items():
            # Sort the access times for the employee.
            times.sort()
            
            # Flag to indicate if the employee is a high-access employee.
            is_high_access = False
            
            # Check for consecutive accesses within a 100-minute window.
            n = len(times)
            for i in range(n - 2):
                if times[i + 2] < times[i] + 100:
                    is_high_access = True
                    break
            
            # If the flag is true, the employee is considered high-access.
            if is_high_access:
                high_access_employees.append(employee)
        
        # Return the list containing the names of high-access employees.
        return high_access_employees


"""
import java.util.*;

public class Solution {
    // Function to find high-access employees based on access times.
    public List<String> findHighAccessEmployees(List<List<String>> access_times) {
        // Create a map to store access times for each employee.
        Map<String, List<Integer>> accessMap = new HashMap<>();

        // Populate the map with access times from the input list.
        for (List<String> entry : access_times) {
            String employee = entry.get(0);
            int accessTime = Integer.parseInt(entry.get(1));
            accessMap.computeIfAbsent(employee, k -> new ArrayList<>()).add(accessTime);
        }

        // List to store the names of high-access employees.
        List<String> highAccessEmployees = new ArrayList<>();

        // Iterate through the map to check access patterns for each employee.
        for (Map.Entry<String, List<Integer>> entry : accessMap.entrySet()) {
            List<Integer> times = entry.getValue();
            // Sort the access times for the employee.
            times.sort(null);

            // Flag to indicate if the employee is a high-access employee.
            boolean isHighAccess = false;

            // Check for consecutive accesses within a 100-minute window.
            for (int i = 0; i + 2 < times.size(); ++i) {
                if (times.get(i + 2) - times.get(i) < 100) {
                    isHighAccess = true;
                    break;
                }
            }

            // If the flag is true, the employee is considered high-access.
            if (isHighAccess) {
                highAccessEmployees.add(entry.getKey());
            }
        }

        // Return the list containing the names of high-access employees.
        return highAccessEmployees;
    }
}
"""
