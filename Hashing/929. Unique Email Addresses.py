"""
Question: 
Every valid email consists of a local name and a domain name, separated by the '@' sign. 
Besides lowercase letters, the email may contain one or more '.' or '+'.
For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, 
mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.
For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. 
This allows certain emails to be filtered. Note that this rule does not apply to domain names.
For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.
Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

Example 1:
Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

Example 2:
Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3

Constraints:
    1 <= emails.length <= 100
    1 <= emails[i].length <= 100
    emails[i] consist of lowercase English letters, '+', '.' and '@'.
    Each emails[i] contains exactly one '@' character.
    All local and domain names are non-empty.
    Local names do not start with a '+' character.
    Domain names end with the ".com" suffix.
    Domain names must contain at least one character before ".com" suffix.

"""

"""
Logic:
The problem gives us three main rules for "normalizing" an email:
The Split: An email has two parts: local_name and domain_name. They are separated by the first (and only) @.
The Dot Rule (Local only): Remove all . from the local_name.
The Plus Rule (Local only): Ignore everything in the local_name after the first +.
The Domain: Leave it exactly as it is.
Goal: After normalizing each email, count how many unique strings we have. A set is the perfect tool for this.

Time Complexity: O(N * K), where N is the number of emails and K is the average length of an email. 
We visit every character of every email at least once.
Space : O(N * K)

Q)  "testemail+david@lee.tcode.com"
why this is a valid domain name having more dots.

Ans: The rule about dots only applies to the local name (the part before the @). Here is why lee.tcode.com is valid and remains unchanged:
"""

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            # 1. Split into local and domain parts
            local, domain = email.split('@')
            
            # 2. Handle the '+' rule: keep only what's before the first '+'
            # We use split('+')[0] to get the part before the plus
            local = local.split('+')[0]
            
            # 3. Handle the '.' rule: remove all dots
            local = local.replace('.', '')
            
            # 4. Reconstruct and add to set
            unique_emails.add(local + '@' + domain)
            
        return len(unique_emails)

# Method 2: Without using python inbult function
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            local, domain = email.split('@')
            actual_local = []
            
            for char in local:
                if char == '+':
                    break  # Stop processing local name
                elif char == '.':
                    continue # Skip dots
                else:
                    actual_local.append(char)
            
            # Use "".join() for O(N) string construction
            unique_emails.add("".join(actual_local) + '@' + domain)
            
        return len(unique_emails)
    
