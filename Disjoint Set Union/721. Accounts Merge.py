"""
You can visualize it as a graph where each Account Index is a node, and an Email is a bridge connecting two account indices.

The Thought Process: Why DSU?
1. The "Bridge" Intuition: If Account 0 has "john@m.com" and Account 1 also has "john@m.com", these two accounts are the same person. The email acts as a connection.
2. Transitive Property: If Account 0 matches Account 1, and Account 1 matches Account 2, then all three must be merged. 
This is exactly what Disjoint Set Union (DSU) handles—merging smaller sets into larger components.
3. The Entities:
    Nodes: The indices of the accounts list (0, 1, 2,...., n-1).
    Connections: Any two indices that share a common email.

The Logic: A Two-Pass Strategy
Pass 1: Build the Connections (Union)
We need a way to track which emails we've seen before. We use a hashmap mail_to_index.
a) Iterate through each account.
b) For each email:
    If we haven't seen it: Map email -> current_account_index.
    If we have seen it: It means the current_account_index and the previously_stored_index belong to the same person. Call dsu.union(current, previous).

Pass 2: Grouping the Emails (Find)
After all unions are done, every account index points to its "Ultimate Parent" (the representative of that person).
a) Create a list of lists (or a dictionary) called mergedMail.
b) Iterate through our mail_to_index map.
c) For each email, find the ultimate_parent of the index it's mapped to.
d) Append the email to mergedMail[ultimate_parent].

Complexity
Time: O(N * K * alpha(N) + M *log M), where N is accounts, K is emails per account, and M is the total number of unique emails (due to sorting).
Space: O(N * K) to store the DSU parents and the email-to-index mapping.

"""

import collections

class DSU:
    def __init__(self, n):
        # parent[i] stores the representative of the set containing i
        self.parent = list(range(n))
        # size[i] stores the number of nodes in the set rooted at i
        self.size = [1] * n
    
    def findUPar(self, n):
        # Path Compression: Connects node directly to the root
        if n == self.parent[n]:
            return n
        self.parent[n] = self.findUPar(self.parent[n])
        return self.parent[n]
    
    def unionBySize(self, n1, n2):
        # Find ultimate parents of both nodes
        p1, p2 = self.findUPar(n1), self.findUPar(n2)
        if p1 == p2:
            return # Already in the same component
            
        # Union by Size: Attach smaller tree under larger tree
        if self.size[p1] < self.size[p2]:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]
        else:
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        n = len(accounts)
        dsu = DSU(n)
        
        # Step 1: Map each email to the FIRST account index that owns it.
        # If we see the email again in a different account, we UNION the two indices.
        email_to_acc = {} # { "email@test.com": account_index }
        
        for i in range(n):
            # Skip the first element as it is the Name, start from index 1 (emails)
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                
                if email not in email_to_acc:
                    # First time seeing this email, associate it with current account index
                    email_to_acc[email] = i
                else:
                    # This email appeared before! Merge current account with previous one.
                    dsu.unionBySize(i, email_to_acc[email])
        
        # Step 2: Group all unique emails by their "Ultimate Parent" account index.
        # This effectively merges all emails belonging to the same person.
        merged_mail_dict = collections.defaultdict(list)
        for email, acc_idx in email_to_acc.items():
            root = dsu.findUPar(acc_idx)
            merged_mail_dict[root].append(email)
            
        # Step 3: Format the final output.
        # Each entry must be [Name, sorted_email1, sorted_email2, ...]
        result = []
        for root_idx, emails in merged_mail_dict.items():
            # The name is taken from the representative account index
            name = accounts[root_idx][0]
            # Requirement: emails must be in sorted order
            result.append([name] + sorted(emails))
            
        return result

# Java
"""
import java.util.*;

class DSU {
    int[] parent, size;

    DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    int findUPar(int node) {
        if (parent[node] == node) return node;
        return parent[node] = findUPar(parent[node]);
    }

    void unionBySize(int u, int v) {
        int pu = findUPar(u), pv = findUPar(v);
        if (pu == pv) return;
        if (size[pu] < size[pv]) {
            parent[pu] = pv;
            size[pv] += size[pu];
        } else {
            parent[pv] = pu;
            size[pu] += size[pv];
        }
    }
}

class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        int n = accounts.size();
        DSU dsu = new DSU(n);
        Map<String, Integer> mailToIndex = new HashMap<>();

        for (int i = 0; i < n; i++) {
            for (int j = 1; j < accounts.get(i).size(); j++) {
                String mail = accounts.get(i).get(j);
                if (!mailToIndex.containsKey(mail)) {
                    mailToIndex.put(mail, i);
                } else {
                    dsu.unionBySize(i, mailToIndex.get(mail));
                }
            }
        }

        Map<Integer, List<String>> merged = new HashMap<>();
        for (Map.Entry<String, Integer> entry : mailToIndex.entrySet()) {
            String mail = entry.getKey();
            int parent = dsu.findUPar(entry.getValue());
            merged.computeIfAbsent(parent, x -> new ArrayList<>()).add(mail);
        }

        List<List<String>> result = new ArrayList<>();
        for (Map.Entry<Integer, List<String>> entry : merged.entrySet()) {
            List<String> emails = entry.getValue();
            Collections.sort(emails);
            List<String> account = new ArrayList<>();
            account.add(accounts.get(entry.getKey()).get(0));
            account.addAll(emails);
            result.add(account);
        }

        return result;
    }
}
"""

# C++ Code 
"""
#include <bits/stdc++.h>
using namespace std;

class DSU {
public:
    vector<int> parent, size;
    DSU(int n) {
        parent.resize(n);
        size.resize(n, 1);
        for (int i = 0; i < n; i++) parent[i] = i;
    }

    int findUPar(int n) {
        if (n == parent[n])  // same comment as Python
            return n;
        parent[n] = findUPar(parent[n]);
        return parent[n];
    }

    void unionBySize(int n1, int n2) {
        int p1 = findUPar(n1), p2 = findUPar(n2);
        if (p1 == p2)  // we can't do union since they belong to the same component.
            return;
            // return False
        if (size[p1] < size[p2]) {
            parent[p1] = p2;
            size[p2] += size[p1];
        } else {  // rank[p1]>= rank[p2]
            parent[p2] = p1;
            size[p1] += size[p2];
        }
    }
};

class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        int n = accounts.size();
        DSU dsu(n);
        unordered_map<string, int> mail_to_Name;
        for (int name = 0; name < n; name++) {  // first index will represent the name in each account.
            for (int emails = 1; emails < (int)accounts[name].size(); emails++) {  // email for each account will start from '1' for each name.
                string mail = accounts[name][emails];
                if (mail_to_Name.find(mail) == mail_to_Name.end()) {  // if this email is not into 'map'
                    mail_to_Name[mail] = name;
                } else {  // join the two accounts(name into 1 by updating the parent)
                    dsu.unionBySize(name, mail_to_Name[mail]);
                    // no need to map this curr mail because this same mail is already there.
                }
            }
        }
        // map with mail-> account_no(i.e 0,1,2) is created
        // Now disjoint set is also created and account with same email id is merged into one.

        // Now take email one by one from 'map' and add that to the ultimate parent of their account_no(values) with name in sorted order.
        // first merging mail together belonging to same account.
        vector<vector<string>> mergedMail(n);
        for (auto& [mail, account_no] : mail_to_Name) {
            int ultimate_parent = dsu.findUPar(account_no);
            mergedMail[ultimate_parent].push_back(mail);
        }
        // now all mail will be get merged into respective parent account

        // now add the name before these mails.
        // print(mergedMail); // (Python print removed in C++)
        vector<vector<string>> ans;
        for (int i = 0; i < n; i++) {
            if (mergedMail[i].empty()) {  // after merging there may not be any mail because they are already added to parent account.
                continue;
            }
            sort(mergedMail[i].begin(), mergedMail[i].end());  // sorting emails after merging.
            vector<string> merged_account;  // to store the name and email for each account after merging
            merged_account.push_back(accounts[i][0]);  // adding the name of each count first
            for (auto& mail : mergedMail[i]) {
                merged_account.push_back(mail);
            }
            ans.push_back(merged_account);
        }
        return ans;
    }
};

"""
# Later try by DFS also.
