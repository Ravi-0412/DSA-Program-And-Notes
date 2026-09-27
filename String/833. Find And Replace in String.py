"""
Step 1: Brute force. Do literally what the problem says

  To find a brute force, read the problem as instructions: "for each operation, check whether the source matches; if it does, replace it." Turn that sentence straight into code.

  Attempt 1: the literal reading

  for each operation i (in the given order):
      if s has sources[i] at indices[i]:
          s = part before + targets[i] + part after

  Try it on a small example before trusting it.

  Limitation 1: positions shift after a replacement.
  s = "abcd", ops: (0, "a" → "eee"), (2, "cd" → "ffff")

  op0: "abcd" → "eeebcd"
  op1: check "cd" at index 2 → s[2] = 'e'  ✗  no match (it should match)
  result "eeebcd", expected "eeebffff"
  Why it happens: a replacement changes the length of the string, so every position after it moves. The indices you were given point into the original string.

  Fix: process the operations from right to left, sorted by index in descending order. A replacement at index 5 can only move characters at index 5 and later, so the smaller indices you haven't handled yet still point to the right place.

  Limitation 2: a replacement can create a new match.
  s = "abcd", ops: (0, "abz" → "X"), (2, "cd" → "zz")
  
  Original: "abz" at 0?  s[0:3] = "abc"  → no match
  Right to left:
    op1: "abcd" → "abzz"
    op0: "abz" at 0?  s[0:3] = "abz"  → matches  ✗ (this match didn't exist originally)
  Fix: check every operation against the original string first, then apply the replacements.

  Brute force (correct version)

  Complexity. Let n = len(s), k = number of operations, L = the longest source, T = the longest target.

  ┌─────────────┬───────────────────────────────┬──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
  │    Step     │             Cost              │                                                                                           Why                                                                                            │
  ├─────────────┼───────────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ Match       │ O(k·L)                        │ Each startswith compares up to L characters                                                                                                                                              │
  │ checks      │                               │                                                                                                                                                                                          │
  ├─────────────┼───────────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ Sort        │ O(k log k)                    │ Sorting the k operations                                                                                                                                                                 │
  ├─────────────┼───────────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ Rebuilds    │ O(k·(n + k·T))                │ Hidden cost: Python strings can't be changed in place, so s[:idx] + ... + s[...] copies the whole current string. The string can grow to n + k·T characters, and you rebuild up to k     │
  │             │                               │ times.                                                                                                                                                                                   │
  ├─────────────┼───────────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ Total       │ O(k log k + k·L + k·(n +      │ About 100 × 6000 = 6 × 10⁵                                                                                                                                                               │
  │             │ k·T))                         │                                                                                                                                                                                          │
  └─────────────┴───────────────────────────────┴──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  
  Space: O(k) extra for matched and order, plus an O(n + k·T) temporary copy on each rebuild. The output is O(n + k·T).

  Remaining limitation (cost):
  k = 100 replacements, each changing about 3 characters
  → you copy about 6000 characters 100 times = 600,000 characters copied
  → to produce a string that only needed about 6000 characters written

"""
  class Solution:
      def findReplaceString(self, s, indices, sources, targets):
          # 1) Decide every match against the ORIGINAL string, before anything changes.
          #    s.startswith(src, idx) returns False if src would run past the end of s.
          matched = [s.startswith(src, idx) for idx, src in zip(indices, sources)]

          # 2) Order the operations by index, largest first, so smaller indices stay valid.
          order = sorted(range(len(indices)), key=lambda i: indices[i], reverse=True)

          # 3) Apply each matched replacement by rebuilding the whole string.
          for i in order:
              if matched[i]:
                  idx = indices[i]
                  s = s[:idx] + targets[i] + s[idx + len(sources[i]):]
          return s

# Optimisation
"""
 Step 2: Find the gap. What work is wasted?

  Look at the brute force and ask these questions. They work on almost any problem:

  1. Am I redoing the same work? Yes. Every replacement copies the whole string, even though only a small window changes.
  2. What do I actually need to know? The final string is just the original string with some windows swapped out. I already know every window from the original indices, because I checked the matches up front.
  3. So can I decide first and build once? Yes. If I know all the swaps before I start writing, I can build the result in one left-to-right pass. Nothing shifts, because I'm always reading the original string.
  4. What lookup do I need during that pass? At each position i: "does a replacement start here, and which one?" An array match[i] answers that in O(1).

  Brute force:   check → rebuild whole string → rebuild again → ...   (k full copies)
                                  ↓ gap: most of each copy is wasted
  Optimal:       check all → mark positions → ONE pass building the output


  Step 3: Optimal. Mark the matches, then build once
  
  Logic:
  1. Create match[pos], which holds the index of the operation that starts at pos, or -1 if none does.
  2. Walk through s once. If a replacement starts here, append its target and skip over the source window. Otherwise copy the character.
  3. Collect the pieces in a list and call "".join once at the end. This avoids repeated string +. 
  
  Dry run:
  s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
  
  pos:     0    1    2    3
  s:       a    b    c    d
  match:   0   -1    1   -1
  
  i=0 → op 0 → append "eee",  skip len("a")  = 1 → i=1   res = ["eee"]
  i=1 → -1   → append "b",                        i=2   res = ["eee","b"]
  i=2 → op 1 → append "ffff", skip len("cd") = 2 → i=4   res = ["eee","b","ffff"]
  i=4 → stop → "".join → "eeebffff" ✓

  Neither trap can happen here. Indices never shift, because you only read the original string and write to a separate result. New matches can't appear, because every match was checked against the original.


  Complexity:
  
  ┌───────────────────┬──────────────────┬───────────────────────────────────────────────────────────────────────────┐
  │       Step        │       Cost       │                                    Why                                    │
  ├───────────────────┼──────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ [-1] * len(s)     │ O(n)             │ Initializes the lookup array                                              │
  ├───────────────────┼──────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ Match checks      │ O(k·L)           │ Same as the brute force                                                   │
  ├───────────────────┼──────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ The walk          │ O(n)             │ i only moves forward, so each character is copied or skipped exactly once │
  ├───────────────────┼──────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ Appending targets │ O(k·T)           │ At most k targets written                                                 │
  ├───────────────────┼──────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ "".join           │ O(n + k·T)       │ One pass over all the pieces                                              │
  ├───────────────────┼──────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ Total             │ O(n + k·L + k·T) │ About 10⁴, compared with 6 × 10⁵ for the brute force                      │
  └───────────────────┴──────────────────┴───────────────────────────────────────────────────────────────────────────┘
  
  This is optimal: any solution has to read the input, O(n + k·L), and write the output, O(n + k·T).

  Space: O(n) extra for match. The output is O(n + k·T), which you can't avoid.

  A shorter variant: use match = {idx: op ...} as a dict and look up with match.get(i). The extra space drops to O(k), which is better when the string is huge but has only a few operations.
"""

class Solution:
      def findReplaceString(self, s, indices, sources, targets):
          # match[pos] = op number that starts at pos, -1 if none
          match = [-1] * len(s)
          for op, (idx, src) in enumerate(zip(indices, sources)):
              if s.startswith(src, idx):          # check the ORIGINAL s: no shifts, no new matches
                  match[idx] = op                 # store op number to get both source & target later

          res = []                                # list + one join avoids O(n) string copies
          i = 0
          while i < len(s):                       # while loop: i may jump more than 1
              op = match[i]
              if op != -1:
                  res.append(targets[op])         # write replacement
                  i += len(sources[op])           # skip the SOURCE length in the original s
              else:
                  res.append(s[i])                # copy char unchanged
                  i += 1
          return "".join(res)                     # build the final string once

# follow ups:
"""
1. s has 10⁹ characters and k is small. Solve it with O(k) extra space.

  Step 1: Start from the current optimal and find what's too big

  Our previous solution used two things that grow with n:

  match = [-1] * len(s)   → 10⁹ slots, but at most k (≈100) are ever not -1
  res.append(s[i])        → up to 10⁹ one-character items in a list
  At 10⁹ characters, the list alone holds 10⁹ references of 8 bytes each, about 8 GB, before the result string even exists. That fails.

  Step 2: Find the gap

  Ask: "how much of this data carries real information?"
  - match[] is almost entirely -1. Only k slots matter. When a table is mostly empty, store only the entries that are set.
  - The characters between replacements are never changed. Why copy them one at a time? Copy each untouched stretch as one slice.

  s:    [ untouched ][ src0 ][ untouched ][ src1 ][ untouched tail ]
  out:  [ slice     ][ tgt0 ][ slice     ][ tgt1 ][ slice          ]
         → at most 2k + 1 pieces, not 10⁹

  This means you only need the matched operations, sorted from left to right, and a pointer prev marking where the not-yet-copied part of s begins.

  Step 3: Dry run

  s = "abcd", indices = [2, 0], sources = ["cd", "a"], targets = ["ffff", "eee"]

  matched ops sorted by index → [(0, op1), (2, op0)]

  prev=0, (idx 0, op1): s[0:0] = ""   → append "", "eee"    prev = 0+1 = 1
  prev=1, (idx 2, op0): s[1:2] = "b"  → append "b", "ffff"  prev = 2+2 = 4
  tail: s[4:] = ""                    → append ""

  "".join → "eeebffff" ✓
  

  Complexity

  Let n = len(s), k = number of operations, L = the longest source, T = the longest target.

  ┌──────────────────────┬────────────────────────────┬───────────────────────────────┬───────────────────────────────────────────────────────────────────┐
  │         Step         │            Time            │          Extra space          │                                Why                                │
  ├──────────────────────┼────────────────────────────┼───────────────────────────────┼───────────────────────────────────────────────────────────────────┤
  │ Match checks         │ O(k·L)                     │ none                          │ startswith compares up to L characters, k times                   │
  ├──────────────────────┼────────────────────────────┼───────────────────────────────┼───────────────────────────────────────────────────────────────────┤
  │ Sort the matched ops │ O(k log k)                 │ O(k)                          │ At most k tuples                                                  │
  ├──────────────────────┼────────────────────────────┼───────────────────────────────┼───────────────────────────────────────────────────────────────────┤
  │ Build the pieces     │ O(n + k·T)                 │ O(k) pieces                   │ Every character of s lands in exactly one slice, plus the targets │
  ├──────────────────────┼────────────────────────────┼───────────────────────────────┼───────────────────────────────────────────────────────────────────┤
  │ join                 │ O(n + k·T)                 │ output only                   │ One final copy                                                    │
  ├──────────────────────┼────────────────────────────┼───────────────────────────────┼───────────────────────────────────────────────────────────────────┤
  │ Total                │ O(n + k log k + k·L + k·T) │ O(k), not counting the output │                                                                   │
  └──────────────────────┴────────────────────────────┴───────────────────────────────┴───────────────────────────────────────────────────────────────────┘

  Trade-off compared with the match[] version: you pay O(k log k) for the sort to save O(n) space. When k is small and n is huge, that's clearly worth it.

"""

  class Solution:
      def findReplaceString(self, s, indices, sources, targets):
          # only the matched ops, sorted left to right: O(k) space
          ops = sorted((idx, op) for op, idx in enumerate(indices)
                       if s.startswith(sources[op], idx))   # still checked against the ORIGINAL s
          res, prev = [], 0                                   # prev = start of the part not copied yet
          for idx, op in ops:
              res.append(s[prev:idx])                         # copy the untouched chunk as one slice
              res.append(targets[op])                         # write the replacement
              prev = idx + len(sources[op])                   # skip the source window
          res.append(s[prev:])                                # the tail after the last replacement
          return "".join(res)
        

