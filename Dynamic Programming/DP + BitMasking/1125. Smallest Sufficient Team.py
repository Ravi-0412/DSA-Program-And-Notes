# My method: Correct only but TLE
# Time : O(2^60 * 16). 1 <= people.length <= 60 ,0 <= people[i].length <= 16

# Logic: for eevry person we have choice whether to use take that person or not.
# VVi: If we take then we need to remove those skill which was not contributed before and this cur person is contributing.
# (Not all skills that cur person poses, otherwise you will get extra person than expected)

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        set_req_skills = set(req_skills)

        def solve(cur , added):
            if not set_req_skills:
                if not self.ans:
                    self.ans = added.copy()

                elif len(self.ans) > len(added):
                    self.ans = added.copy()
                return 
        
            if cur == len(people):
                return 
            # when we don't take this person
            solve(cur + 1, added)
            # when we take this peerson
            cur_skill = set()  # skill which was not contributed before and this cur person is contribute.
            for skill in people[cur]:
                if skill in set_req_skills:
                    set_req_skills.remove(skill)
                    cur_skill.add(skill)
            added.append(cur)
            solve(cur + 1 , added)
            # Remove person and skill contributued by them.
            added.pop()
            for skill in cur_skill:
                set_req_skills.add(skill)

        self.ans = []
        solve(0, [])
        return self.ans
    

# To get only the minimum no of people using same method.
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        set_req_skills = set(req_skills)

        def solve(cur):
            if not set_req_skills:
                return 0
            if cur == len(people):
                return float('inf')
            notTake = solve(cur + 1)
            take = 0
            cur_skill = set()
            for skill in people[cur]:
                if skill in set_req_skills:
                    set_req_skills.remove(skill)
                    cur_skill.add(skill)
            take = 1 + solve(cur + 1)
            for skill in cur_skill:
                set_req_skills.add(skill)
            return min(notTake , take)

        return solve(0)

# Method 2 :
"""
How we can optimise ?

Key Insight:
  The SET OF COVERED SKILLS is what matters, not which person covered which skill.
  Two different teams covering the same skill set are interchangeable
  from the perspective of future decisions.

We can mark skills visited using bit as we traverse each person.
We can get this idea seeing the constrint of 'req_skills'.

 dp[skill_mask] = smallest team that covers exactly skill_mask
  Answer = dp[1111...1] (all skills covered)

Time: O(people * 2^skill)
Space: O(2^skill)

"""

from typing import List
from functools import lru_cache

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

        n_skills    = len(req_skills)
        n_people    = len(people)
        all_covered = (1 << n_skills) - 1

        skill_bit   = {skill: i for i, skill in enumerate(req_skills)}

        # Precompute bitmask of skills each person contributes
        person_mask = self.build_person_masks(people, skill_bit)

        @lru_cache(maxsize=None)
        def min_team_from(person_idx, covered):
            # Base case: all skills already covered — no more people needed
            if covered == all_covered:
                return ()

            # Ran out of people without covering all skills
            # Return a sentinel that will never be chosen as minimum
            if person_idx == n_people:
                return None

            # --- Choice 1: SKIP this person ---
            skip = min_team_from(person_idx + 1, covered)

            # --- Choice 2: TAKE this person ---
            new_coverage = covered | person_mask[person_idx]
            rest         = min_team_from(person_idx + 1, new_coverage)

            # If taking leads to a dead end, taking result is also dead end
            take = None if rest is None else (person_idx,) + rest

            return self.pick_smaller_team(skip, take)

        result = min_team_from(0, 0)
        return list(result)


    def build_person_masks(self, people: List[List[str]], skill_bit: dict) -> List[int]:
        """Convert each person's skill list into a single bitmask integer."""
        masks = []
        for person_skills in people:
            mask = 0
            for skill in person_skills:
                mask |= (1 << skill_bit[skill])
            masks.append(mask)
        return masks


    def pick_smaller_team(self, team_a, team_b):
        """
        Return the smaller of two teams.
        None means 'impossible/dead end' — always lose to a valid team.
        If both None, return None. If both valid, return shorter one.
        """
        if team_a is None:
            return team_b
        if team_b is None:
            return team_a
        return team_a if len(team_a) <= len(team_b) else team_b


# Method 3: 
# Memoisation using array

from typing import List

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

        n_skills    = len(req_skills)
        n_people    = len(people)
        all_covered = (1 << n_skills) - 1

        skill_bit   = {skill: i for i, skill in enumerate(req_skills)}
        person_mask = build_person_masks(people, skill_bit)

        # dp[person_idx][covered] = smallest team using people[0..person_idx]
        #                           that achieves exactly 'covered' skill mask
        #
        # Dimensions: (n_people + 1) rows  ×  (all_covered + 1) columns
        # None = this (person_idx, covered) state is not yet reachable
        dp = [[None] * (all_covered + 1) for _ in range(n_people + 1)]

        # Base case: before considering anyone (person_idx=0),
        # the only reachable state is covered=0 with empty team
        dp[0][0] = ()

        for person_idx in range(n_people):
            contribution = person_mask[person_idx]

            for covered in range(all_covered + 1):

                # This state is unreachable — skip it
                if dp[person_idx][covered] is None:
                    continue

                current_team = dp[person_idx][covered]

                # --- Choice 1: SKIP person_idx ---
                # State carries forward unchanged to next person
                dp[person_idx + 1][covered] = pick_smaller_team(
                    dp[person_idx + 1][covered],
                    current_team
                )

                # --- Choice 2: TAKE person_idx ---
                new_coverage = covered | contribution
                new_team     = current_team + (person_idx,)

                dp[person_idx + 1][new_coverage] = pick_smaller_team(
                    dp[person_idx + 1][new_coverage],
                    new_team
                )

        return list(dp[n_people][all_covered])


def build_person_masks(people: List[List[str]], skill_bit: dict) -> List[int]:
    """Convert each person's skill list into a single bitmask integer."""
    masks = []
    for person_skills in people:
        mask = 0
        for skill in person_skills:
            mask |= (1 << skill_bit[skill])
        masks.append(mask)
    return masks


def pick_smaller_team(team_a, team_b):
    """
    Return the smaller valid team.
    None = unreachable/dead-end, always loses to a valid team.
    """
    if team_a is None:
        return team_b
    if team_b is None:
        return team_a
    return team_a if len(team_a) <= len(team_b) else team_b

# Method 4: 
# Tabulation with space optimised

from typing import List

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

        n_skills    = len(req_skills)
        all_covered = (1 << n_skills) - 1

        skill_bit   = {skill: i for i, skill in enumerate(req_skills)}
        person_mask = build_person_masks(people, skill_bit)

        # dp maps skill_mask → smallest list of people that covers it
        # dict naturally holds only reachable states — no None checks needed
        dp = {0: []}

        for person_idx, contribution in enumerate(person_mask):

            # Snapshot current states so person_idx is added at most once
            for covered, team in list(dp.items()):
                new_coverage = covered | contribution

                # Person adds no new skills to this state — skip
                if new_coverage == covered:
                    continue

                # Update if new_coverage never seen or we found smaller team
                if new_coverage not in dp or len(dp[new_coverage]) > len(team) + 1:
                    dp[new_coverage] = team + [person_idx]

        return dp[all_covered]


def build_person_masks(people: List[List[str]], skill_bit: dict) -> List[int]:
    """Convert each person's skill list into a single bitmask integer."""
    masks = []
    for person_skills in people:
        mask = 0
        for skill in person_skills:
            mask |= (1 << skill_bit[skill])
        masks.append(mask)
    return masks

"""
Try by this method also:
https://leetcode.com/problems/smallest-sufficient-team/solutions/1201778/python3-top-down-dp/

Note vvi: This Q is exactly same as "Set cover problem".
problem: 
Given a set of elements {1, 2, …, n} (called the universe) and a collection S of m sets whose union equals the universe,
the set cover problem is to identify the smallest sub-collection of S whose union equals the universe. For example,
consider the universe U = {1, 2, 3, 4, 5} and the collection of sets S = { {1, 2, 3}, {2, 4}, {3, 4}, {4, 5} }. 
Clearly the union of S is U. However, we can cover all of the elements with the following, smaller number of sets: { {1, 2, 3}, {4, 5} }.

link: https://en.wikipedia.org/wiki/Set_cover_problem
"""
