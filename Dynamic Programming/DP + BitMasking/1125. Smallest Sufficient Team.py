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
    

# How we can optimise.
# We can mark skills visited using bit as we traverse each person.
# We can get this idea seeing the constrint of 'req_skills'.

# Time: O(people * 2^skill)
# Space: O(2^skill)

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        skill_index = {skill : i for i , skill in enumerate(req_skills)}
        # storing [skill : index] : This will help in keep track of skills that we have got from people.
        # We can use bit to mark those skill so we require their index.
        dp = {0: []}   # store the [combination_skills : person_required]
        for i in range(len(people)):
            cur_skill = 0   # skills that cur person 'i' can contribute
            for skill in people[i]:
                # Marking this 'skill' as we got.
                cur_skill |= 1 << skill_index[skill]   # in bit position of skill make = 1.
            # Now add this cur_skill to all the skillSet present and form new combination of skillSet.
            for pre , peoples in dict(dp).items():
                skill_comb = pre | cur_skill
                if skill_comb == pre:
                    # if same then skip because adding this person will increase the person required
                    continue
                if skill_comb not in dp or len(dp[skill_comb]) > 1 + len(peoples):
                    # if this combination is not present or person required for this combination is 'len(peoples)'.
                    dp[skill_comb] = peoples + [i]
        return dp[2**n -1]   # return the person_required to get all the skills


# Try by this method also:
# https://leetcode.com/problems/smallest-sufficient-team/solutions/1201778/python3-top-down-dp/

# Note vvi: This Q is exactly same as "Set cover problem".
# problem: 
# Given a set of elements {1, 2, …, n} (called the universe) and a collection S of m sets whose union equals the universe,
# the set cover problem is to identify the smallest sub-collection of S whose union equals the universe. For example,
# consider the universe U = {1, 2, 3, 4, 5} and the collection of sets S = { {1, 2, 3}, {2, 4}, {3, 4}, {4, 5} }. 
# Clearly the union of S is U. However, we can cover all of the elements with the following, smaller number of sets: { {1, 2, 3}, {4, 5} }.

# link: https://en.wikipedia.org/wiki/Set_cover_problem