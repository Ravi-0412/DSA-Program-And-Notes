"""
The Problem: "The Play Store Compatibility Engine"The Scenario: Google Play Store has N APKs. Each APK i has three properties: 
version_id, min_os, and max_os.
A user with an OS version V needs the highest version_id that is compatible with their device.
Constraint: min_os <= V <= max_os
"""

"""
Part 1: The Offline Version (Batch Processing)The Setup: We are given a fixed list of N APKs and a fixed list of M user queries all at once. 
We need to return the answer for all queries.

Ans:
1. Brute Force Logic: 
For each query V, iterate through all N APKs. Check if V is in range. Keep track of the maximum version_id.
Complexity: O(M * N) time, O(1) extra space.

2. Optimized Logic (Sweep Line + Max-Heap)
Thought Process: The "Waste" in Brute Force is checking APKs that aren't even near the query's OS version. 
If we sort both APKs and Queries by OS version, we can "sweep" a line across the OS timeline.
The Strategy: 
  Create "Events": An APK starts at min_os and ends at max_os.
  Sort APK Start Events, APK End Events, and Queries.
  Move across the timeline. When you hit a min_os, add that APK to a Max-Heap.
  When you hit a Query, the top of the heap is your answer (if that APK hasn't expired yet).
  Refinement: To handle expiration, when we pop from the heap, check if max_os < current_os. If so, discard it and look at the next one.

Time : O((N+M) * log N)
"""

import heapq

class OfflineAPKEngine:
    def solve(self, apks, queries):
        """
        apks: List of [version_id, min_os, max_os]
        queries: List of os_version
        """
        # Sort APKs by min_os to know when they 'enter' the timeline
        apks.sort(key=lambda x: x[1])
        
        # Sort queries while keeping track of original index for the result array
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        
        results = [-1] * len(queries)
        max_heap = [] # Stores (-version_id, max_os)
        apk_ptr = 0
        n = len(apks)
        
        for original_idx, os_v in sorted_queries:
            # 1. Add all APKs that can now be supported (min_os <= current_os)
            while apk_ptr < n and apks[apk_ptr][1] <= os_v:
                v_id, _, max_os = apks[apk_ptr]
                heapq.heappush(max_heap, (-v_id, max_os))
                apk_ptr += 1
            
            # 2. Clean up: Remove APKs that are too old for the current OS (max_os < current_os)
            # some apk may end before this current OS version
            while max_heap and max_heap[0][1] < os_v:
                heapq.heappop(max_heap)
            
            # 3. The top of the heap is the highest version available for this point
            if max_heap:
                results[original_idx] = -max_heap[0][0]
                
        return results

# --- TEST CASES ---
offline_engine = OfflineAPKEngine()
# Case 1: Standard overlap (Query OS 12)
# Case 2: Max OS limit check (Query OS 25)
# Case 3: No support (Query OS 5)
apks = [[100, 10, 20], [200, 10, 30], [50, 1, 4]]
queries = [12, 25, 5]
print(f"Offline Results: {offline_engine.solve(apks, queries)}") # Expected: [200, 200, -1]

"""
Real life scenarios

Scenario 1: The "Smart Home Device" Compatibility
Imagine you are an engineer at a smart home company. Your company releases different versions of a Smart Thermostat.

The Constraints: Each thermostat model requires a specific range of voltage from the house's electrical system to operate safely (e.g., Model A needs 10V–20V, Model B needs 15V–30V).

The Goal: A customer tells you their house has exactly 18V. You want to give them the most advanced (highest version) thermostat that won't blow up or fail at that specific voltage.

Relating to the Logic:

Voltage = OS Version.

Voltage Range [Min, Max] = APK Support Range.

Thermostat Model # = APK Version ID.

Scenario 2: The "Streaming Quality" Logic (Netflix/YouTube)
Imagine a streaming service that has multiple versions of the same movie file (4K, 1080p, 720p, 480p).

The Constraints: Each file version requires a certain Internet Bandwidth range.

4K needs 25Mbps–100Mbps.

1080p needs 5Mbps–50Mbps.

The Goal: A user currently has exactly 30Mbps. You want to provide the highest quality (max version) file that their current speed can handle.

Relating to the Logic:

Bandwidth Speed = OS Version.

Bandwidth Range = APK Support Range.

Video Quality Index = APK Version ID.
"""

"""
Part 2: The Online Version (Real-time Stream)   => Understand it later
The Follow-up: Now, the system is live. APKs are uploaded at any time, and users query the service at any time. We cannot wait to "batch" them.
1. Thought Process (Segment Tree)
The Logic: We need a data structure that supports:
  update(min, max, version): Add a new APK to the system.
  query(os_v): Instantly find the max version at this point.
The Structure: A Segment Tree where each leaf is an OS version. Each node in the tree stores the maximum APK version covering that range.
The Problem: Standard Segment Trees usually store the max of a range. Here, an APK covers a range, and we query a point. This is "Dual" to the standard RMQ.

# Time: O(log OS_Range) per operation | Space: O(N log OS_Range)
"""

class OnlineAPKEngine:
    def __init__(self, max_api_level=50):
        self.n = max_api_level
        # Each node stores the maximum APK version covering this range
        self.tree = [-1] * (4 * self.n)

    def add_apk(self, version_id, min_os, max_os):
        """ Update a range with a potential new maximum: O(log N) """
        def _update(node, start, end, l, r, val):
            if l <= start and end <= r:
                self.tree[node] = max(self.tree[node], val)
                return
            mid = (start + end) // 2
            if l <= mid: _update(2*node, start, mid, l, r, val)
            if r > mid: _update(2*node+1, mid+1, end, l, r, val)

        _update(1, 0, self.n, min_os, max_os, version_id)

    def query(self, os_version):
        """ Query a point: O(log N) """
        def _get_max(node, start, end, idx):
            if start == end:
                return self.tree[node]
            
            mid = (start + end) // 2
            # Path maximum: we take the max version found on the way down
            res = self.tree[node]
            if idx <= mid:
                res = max(res, _get_max(2*node, start, mid, idx))
            else:
                res = max(res, _get_max(2*node+1, mid+1, end, idx))
            return res

        return _get_max(1, 0, self.n, os_version)

# --- TEST CASES ---
online_engine = OnlineAPKEngine(35)
online_engine.add_apk(10, 5, 15)
online_engine.add_apk(50, 10, 20)
# Query at OS 12: should be 50 (both 10 and 50 are valid, 50 is higher)
# Query at OS 7: should be 10 (only 10 is valid)
print(f"Online Query OS 12: {online_engine.query(12)}") # Expected: 50
print(f"Online Query OS 7: {online_engine.query(7)}")   # Expected: 10


"""
what if range of os version is very large for a APK & APK releases are less ?
-> Do it later , search in google L4 chat(gemini) 
"""
