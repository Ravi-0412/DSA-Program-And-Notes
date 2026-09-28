"""
 Assumptions to state out loud in the interview:
  - Duplicate points are removed first.
  - Rectangles with zero area don't count.
  - The function returns the count; there's a variant that returns the rectangles themselves.
"""

# Method 1: Brute force
"""
 How to think of it: a rectangle is 4 points, so try every set of 4 and check whether it's a rectangle.

  The check: 4 distinct points form an axis-aligned rectangle exactly when they use 2 distinct x values and 2 distinct y values. That gives 2 × 2 = 4 possible positions, and 4 distinct points must fill all of them.
  {(1,1),(1,4),(4,1),(4,4)} → xs={1,4}, ys={1,4} → 2 and 2 ✓
  {(1,1),(1,4),(4,1),(2,2)} → xs={1,2,4}          → 3 ✗

 ┌───────┬───────┬─────────────────────────────────────────┐
  │       │ Cost  │                   Why                   │
  ├───────┼───────┼─────────────────────────────────────────┤
  │ Time  │ O(n⁴) │ C(n, 4) ≈ n⁴/24 groups, O(1) check each │
  ├───────┼───────┼─────────────────────────────────────────┤
  │ Space │ O(n)  │ The set of unique points                │
  └───────┴───────┴─────────────────────────────────────────┘

  Limitation:
  n = 1000 → about 4·10¹⁰ groups → far too slow

"""

def count_rectangles(points):
      unique_points = list({tuple(p) for p in points})       # remove duplicates
      count = 0
      for quad in itertools.combinations(unique_points, 4):  # every set of 4 points
          if len({x for x, _ in quad}) == 2 and len({y for _, y in quad}) == 2:
              count += 1
      return count

# Method 2:
"""
First gap. Why pick all 4 corners?

Ask: "once I've chosen some of the corners, are the rest already fixed?" Yes. Two opposite corners (x1,y1) and (x2,y2) fix the other two, (x1,y2) and (x2,y1). This is your 939 idea. So choose 2 points, not 4, and look up the other two in a
  set.

  Trap: counting each rectangle twice. Every rectangle has two diagonals, and both would count it:
  (1,4) ──── (4,4)
    │   ╲  ╱   │      diagonal ↗ (1,1)–(4,4)
    │   ╱  ╲   │      diagonal ↘ (1,4)–(4,1)
  (1,1) ──── (4,1)    → the same rectangle is counted 2×
  Fix: only count the bottom-left → top-right diagonal (x1 < x2 and y1 < y2). Each rectangle is then counted exactly once, so you can return the list of rectangles too, 
  without dividing by 2.

    │      Step       │   Time    │                     Space                      │       Why       │
  ├─────────────────┼───────────┼────────────────────────────────────────────────┼─────────────────┤
  │ Build the set   │ O(n)      │ O(n)                                           │                 │
  ├─────────────────┼───────────┼────────────────────────────────────────────────┼─────────────────┤
  │ Every pair      │ O(n²)     │                                                │ n²/2 pairs      │
  ├─────────────────┼───────────┼────────────────────────────────────────────────┼─────────────────┤
  │ Two set lookups │ O(1) each │                                                │ Hashing a tuple │
  ├─────────────────┼───────────┼────────────────────────────────────────────────┼─────────────────┤
  │ Total           │ O(n²)     │ O(n), plus O(R) if you return the R rectangles │                 │
  └─────────────────┴───────────┴────────────────────────────────────────────────┴─────────────────┘
  
  Limitation: it checks all n²/2 pairs, even pairs that could never be a diagonal.
  points spread out, one per column: (0,5), (1,9), (2,3), ...
  → zero rectangles are possible, yet it still tests about n²/2 pairs
"""

def find_rectangles(points):
      point_set = {tuple(p) for p in points}
      rectangles = []
      for (x1, y1), (x2, y2) in itertools.combinations(point_set, 2):
          if x1 > x2:
              (x1, y1), (x2, y2) = (x2, y2), (x1, y1)            # make p1 the left point
          # only the ↗ diagonal counts, so each rectangle is found exactly once
          if x1 < x2 and y1 < y2 and (x1, y2) in point_set and (x2, y1) in point_set:
              rectangles.append(((x1, y1), (x1, y2), (x2, y1), (x2, y2)))
      return rectangles        # len(rectangles) is the count

# Method 3:
"""
Thought process

  1. What does Method 2 waste? It tests every pair of points as a diagonal, about n²/2 pairs, even when the two points could never be corners of the same rectangle.
  
  2. Split the shape into simpler parts. An axis-aligned rectangle is two vertical sticks joined by a flat top and a flat bottom:

   4 │   ●━━━━━━━━━━━●
     │   ┃           ┃       left stick:  x=1, heights 1 → 4
     │   ┃           ┃       right stick: x=4, heights 1 → 4
   1 │   ●━━━━━━━━━━━●
         1           4
  A stick is two points in the same column.

  3. When do two sticks make a rectangle? Both the top and the bottom must be flat, so the two sticks must start at the same height and end at the same height:
  
  sticks (1→4) and (1→4)  → flat top, flat bottom → rectangle ✓
  sticks (1→4) and (1→3)  → top is slanted        → no ✗
  So a stick's label is its pair of heights, (bottom y, top y).

  4. What the problem becomes. "Find rectangles" turns into "count pairs of sticks with the same label", the same pattern as 1512. Number of Good Pairs (https://leetcode.com/problems/number-of-good-pairs/). A hashmap from label to count solves
  it.

  5. Why this is faster. Sticks only come from points in the same column, so you never pair points across columns the way Method 2 did.

  Logic

  1. Group the points by column: x → the set of y values in that column.
  2. In each column, sort its ys and make every stick (every pair of ys).
  3. For each stick, look up how many sticks with the same label were already seen. Each of them forms one rectangle with this stick, so add that number to the answer. Then increase the count for this label.

  Dry run

  points = (1,1) (1,4) (4,1) (4,4) (4,5) (6,1) (6,4) (2,2)

   5 │               ●
   4 │   ●           ●       ●
   1 │   ●           ●       ●
   2 │       ●
     └──────────────────────────
         1   2       4       6

  column x=1: ys [1,4]     → sticks (1,4)
  column x=4: ys [1,4,5]   → sticks (1,4) (1,5) (4,5)
  column x=6: ys [1,4]     → sticks (1,4)
  column x=2: ys [2]       → no sticks

  process          seen before   rectangles   sticks_seen after
  x=1 (1,4)             0            0          (1,4):1
  x=4 (1,4)             1           +1          (1,4):2
  x=4 (1,5)             0            0          (1,5):1
  x=4 (4,5)             0            0          (4,5):1
  x=6 (1,4)             2           +2          (1,4):3
                                   ────
                                     3   → columns {1,4}, {1,6}, {4,6} ✓

  This returns 1 for your example and matches the O(n⁴) brute force on 3,000 random inputs.
  
  Why it's correct

  - No double counting: each rectangle is counted once, when its right stick is processed. At that moment its left stick is already in sticks_seen.
  - No false matches: within one column the ys form a set, so a label appears at most once per column. Two sticks with the same label are always in different columns, which makes them a real rectangle.
  - Why the sort matters: (1,4) and (4,1) would otherwise be two different keys for the same stick.

  Complexity

  Let n = the number of points and cₓ = the number of points in column x (so Σ cₓ = n).

  ┌─────────────────────────┬─────────────────────────────┬─────────────────────────────────────────┬──────────────────────────────┐
  │          Step           │            Time             │                  Space                  │             Why              │
  ├─────────────────────────┼─────────────────────────────┼─────────────────────────────────────────┼──────────────────────────────┤
  │ Group by column         │ O(n)                        │ O(n)                                    │ One set insert per point     │
  ├─────────────────────────┼─────────────────────────────┼─────────────────────────────────────────┼──────────────────────────────┤
  │ Sort each column        │ O(Σ cₓ log cₓ) ≤ O(n log n) │                                         │ Makes labels (low, high)     │
  ├─────────────────────────┼─────────────────────────────┼─────────────────────────────────────────┼──────────────────────────────┤
  │ Make sticks             │ O(Σ cₓ²)                    │                                         │ cₓ(cₓ−1)/2 sticks per column │
  ├─────────────────────────┼─────────────────────────────┼─────────────────────────────────────────┼──────────────────────────────┤
  │ Counter lookup + update │ O(1) per stick              │ O(number of distinct labels) ≤ O(Σ cₓ²) │ Hashing a tuple of 2 ints    │
  ├─────────────────────────┼─────────────────────────────┼─────────────────────────────────────────┼──────────────────────────────┤
  │ Total                   │ O(n log n + Σ cₓ²)          │ O(n + Σ cₓ²)                            │                              │
  └─────────────────────────┴─────────────────────────────┴─────────────────────────────────────────┴──────────────────────────────┘

  What Σ cₓ² means on real layouts:
  every point in its own column      → Σ cₓ² = n            → about O(n log n)
  100 columns × 10 points each       → Σ cₓ² = 100·100 = 10⁴ (vs Method 2's ~5·10⁵)
  all points in 1–2 columns          → Σ cₓ² ≈ n²           → same as Method 2

  Trade-off against Method 2: Method 3 is usually much faster, but its counter can grow to O(n²) in the worst case. Method 2 always uses O(n) space and can also list the rectangles.

  Only need the count?                  → Method 3
  Need the rectangles, or tight memory? → Method 2
  
  Takeaway you can reuse : 
  To count shapes: split the shape into matching parts (sticks), find the label the parts must share (their heights), then count equal labels with count += seen[label]; seen[label] += 1.

# meaning of below lines:
  for stick_heights in itertools.combinations(sorted(ys), 2):   # sorted → label is (low, high)                                                                                                                                                     
                rectangle_count += sticks_seen[stick_heights]

=>  These two lines do two jobs:
  
  1. The for line: from one column's y values, list every stick (every pair of heights).
  2. The += line: for each stick, add "how many sticks with exactly these heights were seen before" to the answer.

  Line 1: for stick_heights in itertools.combinations(sorted(ys), 2):

  Say column x=4 has the points (4,5), (4,1), (4,4). Then ys = {5, 1, 4}.

  sorted(ys)                 → [1, 4, 5]
  combinations([1,4,5], 2)   → (1,4)  (1,5)  (4,5)
  Each tuple is one stick, a pair of points in this column:

   5 │  ●        (1,5): stick from y=1 to y=5
   4 │  ●        (4,5): stick from y=4 to y=5
   1 │  ●        (1,4): stick from y=1 to y=4
       x=4

  Why sorted? A set has no guaranteed order. Without sorting, one column could produce (4,1) while another produces (1,4). Those are different dictionary keys for the same stick, so the match would be missed. Sorting makes every label (low,
  high).

  Line 2: rectangle_count += sticks_seen[stick_heights]

  sticks_seen is a notebook: for each label, it records how many sticks with that label you've already met, all in earlier columns.

  A new stick forms one rectangle with each of those earlier sticks, so you add that number to the answer.

  sticks_seen = {(1,4): 2}     ← already met two (1,4) sticks, at x=1 and x=4

  new stick (1,4) at x=6:
      rectangle_count += sticks_seen[(1,4)]   → += 2
  
      x=1 stick + x=6 stick → rectangle 1
      x=4 stick + x=6 stick → rectangle 2
  Then the next line, sticks_seen[stick_heights] += 1, records this stick in the notebook, so the next matching stick will pair with it too.

  Counter returns 0 for a label it has never seen, so the first stick of a label adds 0 and doesn't crash.

  An analogy: handshakes

  People walk into a room one at a time. Each person shakes hands with everyone already inside who wears the same shirt color. How many handshakes happen in total?

                
"""

def count_rectangles(points):
      ys_by_column = defaultdict(set)                # x → distinct y values in that column
      for x, y in points:
          ys_by_column[x].add(y)                     # set removes duplicate points

      sticks_seen = Counter()                        # (bottom y, top y) → sticks seen so far
      rectangle_count = 0
      for ys in ys_by_column.values():
          for stick_heights in itertools.combinations(sorted(ys), 2):   # sorted → label is (low, high)
              rectangle_count += sticks_seen[stick_heights]             # pairs with every earlier matching stick
              sticks_seen[stick_heights] += 1
      return rectangle_count


