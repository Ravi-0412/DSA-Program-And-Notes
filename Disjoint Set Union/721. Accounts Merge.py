"""
How to think about DSU ?
for simplicity replace the name->0,1,2... for each account.
just traverse through mails for each account and keep mapping with its account_no if doesn't eaxist in map.
if exist in map then connect those account into one component by calling the function union.

after creating map, find all the merged mail of each account into a list of list by traversing through the items in map.
VVI: But add mail to the ultimate parent. 
And at last add name before merged  mail.
"""

class DSU:
    def __init__(self, n):
        self.v= n
        self.parent=  [i for i in range(n)]
        self.size=    [1 for i in range(n)]   
    
    def findUPar(self, n):   
        if n== self.parent[n]:   
            return n
        self.parent[n]= self.findUPar(self.parent[n])   
        return self.parent[n]
    
    def unionBySize(self, n1, n2):
        p1, p2= self.findUPar(n1), self.findUPar(n2)
        if p1== p2:   # we can't do union since they belong to the same component.
            return
            # return False
        if self.size[p1] < self.size[p2]:
            self.parent[p1]= p2  
            self.size[p2]+= self.size[p1]   
        else :   # rank[p1]>= rank[p2]
            self.parent[p2]= p1   
            self.size[p1]+= self.size[p2]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n= len(accounts)
        dsu= DSU(n)
        mail_to_Name= {}
        for name in range(n):   # first index will represent the name in each account.
            for emails in range(1, len(accounts[name])):   # email for each account will start from '1' for each name.
                mail= accounts[name][emails]
                if mail not in mail_to_Name:  # if this email is not into 'map'
                    mail_to_Name[mail]= name
                else: # join the two accounts(name into 1 by updating the parent)
                    dsu.unionBySize(name, mail_to_Name[mail])
                    # no need to map this curr mail because this same mail is already there.
        # map with mail-> account_no(i.e 0,1,2) is created
        # Now disjoint set is also created and account with same email id is merged into one.
        
        # Now take email one by one from 'map' and add that to the ultimate parent of their account_no(values) with name in sorted order.
        # first merging mail together belonging to same account.
        mergedMail= [[] for i in range(n)]
        for mail, account_no in mail_to_Name.items():
            ultimate_parent= dsu.findUPar(account_no)
            mergedMail[ultimate_parent].append(mail)
        # now all mail will be get merged into respective parent account
        
        # now add the name before these mails.
        print(mergedMail)
        ans= []
        for i in range(n):
            if not mergedMail[i]: # after merging there may not be any mail because they are already added to parent account.
                continue
            mergedMail[i].sort()  # sorting emails after merging.
            merged_account= []    # to store the name and email for each account after merging
            merged_account.append(accounts[i][0])  # adding the name of each count first
            for mail in mergedMail[i]:
                merged_account.append(mail)
            ans.append(merged_account)
        return ans

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
# Later try by DFS also.
