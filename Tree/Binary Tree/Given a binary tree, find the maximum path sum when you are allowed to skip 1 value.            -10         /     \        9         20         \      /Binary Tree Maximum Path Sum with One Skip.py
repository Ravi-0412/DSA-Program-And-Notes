"""
 Given a binary tree, find the maximum path sum when you are allowed to skip 1 value.                                                                                                                                                              
                                                                                                                                                                                                                                                    
        -10                                                                                                                                                                                                                                         
      /     \                                                                                                                                                                                                                                       
     9         20                                                                                                                                                                                                                                   
      \      /  \                                                                                                                                                                                                                                   
      -100   15   7                                                                                                                                                                                                                                 
  Answer 44.                                                                                                                                                                                                                                        
  Maximum Path: 9-> -10 -> 20 -> 15                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
"""

"""
  Assumptions to confirm with the interviewer:
  - A skipped node's value counts as 0, but the path still passes through it (your example relies on this).
  - The skip is optional (used 0 or 1 times).
  - A path that is only the skipped node is allowed and sums to 0.
"""

"""
  Ask: "what would a node need to know from its children to handle the skip in one pass?"

  In 124, a child returns one number: its best downward arm. With a skip allowed, the parent needs to know whether the skip has already been used in that arm. So each child returns two numbers:

  arm_no_skip   = best downward arm with the skip NOT used
  arm_with_skip = best downward arm with the skip used at most once
  This is the same idea as 1186. Maximum Subarray Sum with One Deletion (https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/): 
  add a state for "deletion used or not."

  Where can the skip be in a path that bends at node?

              node
             /    \
       left arm   right arm
  
  ┌───────────────────────────────┬──────────────────────────────────────┐
  │           Skip is…            │               Path sum               │
  ├───────────────────────────────┼──────────────────────────────────────┤
  │ in the left arm, or not used  │ val + left_with_skip + right_no_skip │
  ├───────────────────────────────┼──────────────────────────────────────┤
  │ in the right arm, or not used │ val + left_no_skip + right_with_skip │
  ├───────────────────────────────┼──────────────────────────────────────┤
  │ on the bend node itself       │ 0 + left_no_skip + right_no_skip     │
  └───────────────────────────────┴──────────────────────────────────────┘
  
  The "not used at all" case is already covered, because arm_with_skip means "at most one skip", so it is always ≥ arm_no_skip. The skip can't be in both arms, since you only get one.

  What to return to the parent (a single downward arm)

  arm_no_skip   = val + max(left_no_skip, right_no_skip)

  arm_with_skip = max(
      val + max(left_with_skip, right_with_skip),   # skip is further down, or not used
      0   + max(left_no_skip,  right_no_skip)       # skip this node itself
  )
  All arms are clamped with max(…, 0), the same as in 124: a negative arm is dropped.

  Dry run

            -10
          /     \
         9       20
          \     /  \
         -100  15   7

  node | children (no_skip, with_skip), clamped | best bending here                 | returns (no_skip, with_skip)
  -100 | L(0,0) R(0,0)                          | max(-100, -100, 0) = 0            | (-100, max(-100, 0)) = (-100, 0)
   9   | L(0,0) R(0,0)   (-100 clamped → 0)     | 9                                 | (9, 9)
   15  | —                                      | 15                                | (15, 15)
   7   | —                                      | 7                                 | (7, 7)
   20  | L(15,15) R(7,7)                        | max(42, 42, 0+15+7) = 42          | (35, max(35, 15)) = (35, 35)
  -10  | L(9,9) R(35,35)                        | max(-10+9+35, -10+9+35, 0+9+35)   |
       |                                        |   = max(34, 34, 44) = 44 ✓        |
  The winning case is "skip the bend": 0 + 9 + 35, which is the path 9 → (−10 skipped) → 20 → 15.

  Complexity
  
  Let n = the number of nodes and h = the height of the tree.

"""

class Solution:
      def maxPathSumSkipOne(self, root: Optional[TreeNode]) -> int:
          self.best = -math.inf
          
          def best_arms(node):
              """Returns (best downward arm without a skip, best downward arm with at most 1 skip)."""
              if not node:
                  return 0, 0
                  
              left_no_skip, left_with_skip = best_arms(node.left)
              right_no_skip, right_with_skip = best_arms(node.right)
              # a negative arm makes the path worse → drop it
              left_no_skip, left_with_skip = max(left_no_skip, 0), max(left_with_skip, 0)
              right_no_skip, right_with_skip = max(right_no_skip, 0), max(right_with_skip, 0)
              
              # path bending here: the skip is in the left arm, in the right arm, or on this node
              self.best = max(self.best,
                              node.val + left_with_skip + right_no_skip,
                              node.val + left_no_skip + right_with_skip,
                              left_no_skip + right_no_skip)            # skip this node
                              
              arm_no_skip = node.val + max(left_no_skip, right_no_skip)
              arm_with_skip = max(node.val + max(left_with_skip, right_with_skip),  # skip is below (or unused)
                                  max(left_no_skip, right_no_skip))                 # skip this node
              return arm_no_skip, arm_with_skip
              
          best_arms(root)
          return self.best
