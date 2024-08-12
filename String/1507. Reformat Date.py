class Solution:
    def reformatDate(self, date: str) -> str:
        M = {"Jan" : "01", "Feb" : "02", "Mar" : "03", "Apr" : "04", "May" : "05", "Jun" : "06", "Jul" : "07", "Aug" : "08", "Sep" : "09", "Oct" : "10", "Nov" : "11", "Dec" : "12", }
        
        D = ""
        if (len(date) == 13):
            # day is > 9
            D += date[9 :] + "-" + M[date[5: 8]] + "-" + date[:2]
        else:
            # day is <= 9
            D += date[8 :] + "-" + M[date[4: 7]] + "-0" + date[0]
        return D


# java
"""
import java.util.HashMap;
import java.util.Map;

class Solution {
    public String reformatDate(String date) {
        // Month mapping
        Map<String, String> M = new HashMap<>();
        M.put("Jan", "01");
        M.put("Feb", "02");
        M.put("Mar", "03");
        M.put("Apr", "04");
        M.put("May", "05");
        M.put("Jun", "06");
        M.put("Jul", "07");
        M.put("Aug", "08");
        M.put("Sep", "09");
        M.put("Oct", "10");
        M.put("Nov", "11");
        M.put("Dec", "12");
        
        String D = "";
        
        // Extract year
        String year = date.substring(date.length() - 4);
        
        // Extract month
        String month = M.get(date.substring(date.length() - 8, date.length() - 5));
        
        // Extract day
        String day = date.length() == 13 ? date.substring(0, 2) : "0" + date.substring(0, 1);
        
        // Construct the final date in "YYYY-MM-DD" format
        D = year + "-" + month + "-" + day;
        
        return D;
    }
}
"""