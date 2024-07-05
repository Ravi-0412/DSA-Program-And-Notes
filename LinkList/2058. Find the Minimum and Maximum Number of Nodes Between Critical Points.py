# 
class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> list[int]:
        pre, cur = head, head.next
        index = 1
        first_critical_index = -1
        last_critical_index = -1
        min_distance = float('inf')
        max_distance = float('-inf')

        while cur and cur.next:
            # Check if cur is a critical point
            if (cur.val > pre.val and cur.val > cur.next.val) or (cur.val < pre.val and cur.val < cur.next.val):
                # Update ans
                if first_critical_index != -1:
                    min_distance = min(min_distance, index - last_critical_index)
                    max_distance = max(max_distance, index - first_critical_index)

                if first_critical_index == -1:
                    first_critical_index = index  # Update this first time only to get maximum distance
                last_critical_index = index  # Update this every time to get minimum distance

            pre = cur
            cur = cur.next
            index += 1

        # Return the result based on the presence of critical points using the ternary operator
        return [-1, -1] if first_critical_index == last_critical_index else [min_distance, max_distance]

# java
"""
class Solution {
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        ListNode pre = head, cur = head.next;
        int index = 1;
        int firstCriticalIndex = -1, lastCriticalIndex = -1;
        int minDistance = Integer.MAX_VALUE, maxDistance = Integer.MIN_VALUE;

        while (cur != null && cur.next != null) {
            // Check if cur is a critical point
            if ((cur.val > pre.val && cur.val > cur.next.val) || (cur.val < pre.val && cur.val < cur.next.val)) {
                // Update ans
                if (firstCriticalIndex != -1) {
                    minDistance = Math.min(minDistance, index - lastCriticalIndex);
                    maxDistance = Math.max(maxDistance, index - firstCriticalIndex);
                }

                if (firstCriticalIndex == -1) {
                    firstCriticalIndex = index;    # we need to update this first time only to get maximum distance
                }
                lastCriticalIndex = index;    # we need to update this every time only to get minimum distance
            } 
            pre = cur;
            cur = cur.next;
            index += 1;
        }

        // Return the result based on the presence of critical points using the ternary operator
        return firstCriticalIndex == lastCriticalIndex ? new int[]{-1, -1} : new int[]{minDistance, maxDistance};
    }
}
"""