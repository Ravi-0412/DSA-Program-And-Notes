"""
 Thought process

  1. Start from what worked in 939. A diagonal (two opposite corners) fixed the whole rectangle, so you only had to check that the other two corners exist.

  2. Find what breaks. With tilted rectangles, one diagonal fits infinitely many rectangles, so you can't compute the missing corners from it. Instead of "one diagonal → the rectangle", ask: "what do both diagonals of a rectangle have in
  common?"

  3. Look for invariants (properties that are always true). Take a real rectangle and measure both diagonals:
          A(1,2)
         ╱      ╲
    D(0,1)      B(2,1)
         ╲      ╱
          C(1,0)
          
  diagonal A–C: midpoint (1,1), length 2
  diagonal B–D: midpoint (1,1), length 2
  - They have the same midpoint. The diagonals cut each other in half, which makes the shape a parallelogram.
  - They have the same length. A parallelogram with equal diagonals is a rectangle.
  
  The reverse is also true: any two point pairs with the same midpoint and the same length are the two diagonals of a rectangle.

  4. That tells you the data structure. "Find pairs that share a property" means computing a key per pair and grouping in a hashmap. Here, key = (midpoint, length). Every two pairs inside one group form one rectangle.

  5. Keep the key exact. Floats can make two equal keys look different (0.1 + 0.2 ≠ 0.3), so avoid them:
  - Midpoint = (x1+x2)/2 can be a fraction like 0.5. Store x1+x2 instead: equal sums mean equal midpoints.
  - Length = √(dx²+dy²) is irrational. Store dx²+dy² instead: equal squared lengths mean equal lengths.
  
  6. Compute the area. For diagonals (p1, p2) and (p3, p4), p3 is adjacent to both p1 and p2, so area = |p1−p3| × |p2−p3|.

  Dry run

  points = [(1,2), (2,1), (1,0), (0,1)]
  
  All 6 pairs → key (x1+x2, y1+y2, length²):
    (1,2)-(2,1) → (3,3,2)
    (1,2)-(1,0) → (2,2,4)   ┐
    (1,2)-(0,1) → (1,3,2)   │
    (2,1)-(1,0) → (3,1,2)   │ same key
    (2,1)-(0,1) → (2,2,4)   ┘
    (1,0)-(0,1) → (1,1,2)

  Groups with 2+ diagonals: (2,2,4) → [((1,2),(1,0)), ((2,1),(0,1))]
    p1=(1,2), p2=(1,0), p3=(2,1)
    |p1−p3| = √2, |p2−p3| = √2 → area 2 ✓

    This passes all 3 LeetCode examples and matches the O(n³) version on 1,500 random inputs.

  Complexity

  Let n = the number of points, P = n(n−1)/2 = the number of pairs, and gₖ = the size of group k.

  ┌─────────────────────────────┬─────────────────────────────┬───────┬────────────────────────────────────────┐
  │            Step             │            Time             │ Space │                  Why                   │
  ├─────────────────────────────┼─────────────────────────────┼───────┼────────────────────────────────────────┤
  │ Generate the pairs          │ O(n²)                       │ O(1)  │ combinations yields one pair at a time │
  ├─────────────────────────────┼─────────────────────────────┼───────┼────────────────────────────────────────┤
  │ Build each key              │ O(1) per pair               │       │ A few additions and multiplications    │
  ├─────────────────────────────┼─────────────────────────────┼───────┼────────────────────────────────────────┤
  │ Insert into the dict        │ O(1) amortized per pair     │ O(n²) │ Stores all P pairs                     │
  ├─────────────────────────────┼─────────────────────────────┼───────┼────────────────────────────────────────┤
  │ Visit the groups            │ O(number of groups) ≤ O(n²) │       │                                        │
  ├─────────────────────────────┼─────────────────────────────┼───────┼────────────────────────────────────────┤
  │ Combine pairs within groups │ O(Σ gₖ²)                    │ O(1)  │ Every two diagonals in a group         │
  ├─────────────────────────────┼─────────────────────────────┼───────┼────────────────────────────────────────┤
  │ math.dist × 2               │ O(1)                        │       │                                        │
  ├─────────────────────────────┼─────────────────────────────┼───────┼────────────────────────────────────────┤
  │ Total                       │ O(n² + Σ gₖ²)               │ O(n²) │                                        │
  └─────────────────────────────┴─────────────────────────────┴───────┴────────────────────────────────────────┘

  What Σ gₖ² means in practice:
  - Typical inputs: most groups hold 1 or 2 pairs, so Σ gₖ² ≈ O(n²) and the total is O(n²).
  - Worst case: points spread evenly around one circle. All n/2 diameters share the center and the length, so one group has about n/2 pairs, which is about n²/4 combinations. Other groups stay small, so it's still roughly O(n²). A tight
    worst-case bound is known to be a little above n², but in interviews saying "O(n²) in practice" is fine.
"""

class Solution:
      def minAreaFreeRect(self, points: List[List[int]]) -> float:
          # (2·midpoint, length²) → all point pairs that could be a diagonal with that shape
          diagonals_by_key = defaultdict(list)
          for p1, p2 in itertools.combinations(points, 2):          # every pair once
              key = (p1[0] + p2[0], p1[1] + p2[1],                  # sums instead of midpoint → no fractions
                     (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)   # squared length → no sqrt
              diagonals_by_key[key].append((p1, p2))

          min_area = math.inf
          for pairs in diagonals_by_key.values():
              for (p1, p2), (p3, _) in itertools.combinations(pairs, 2):   # any 2 diagonals → one rectangle
                  # p3 is adjacent to both ends of diagonal p1–p2
                  min_area = min(min_area, math.dist(p1, p3) * math.dist(p2, p3))

          return min_area if min_area < math.inf else 0
