# Method 1: 

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
    int v;
    int[] parent;
    int[] size;

    public DSU(int n) {
        v = n;
        parent = new int[n];        // here '0' based indexing is used in Q.
        size = new int[n];          // will give the size of each parent component.
                                    // initially size of all be '1'(node itself).
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    // finding the ultimate parent
    public int findUPar(int n) {
        if (n == parent[n]) {
            // Root parent will be the parent of itself. so continue till we find that.
            return n;
        }

        // this will assign the root parent of every node coming in that ultimate root.
        // This is called path compression.
        return parent[n] = findUPar(parent[n]);
    }

    public boolean unionBySize(int n1, int n2) {
        int p1 = findUPar(n1);
        int p2 = findUPar(n2);

        if (p1 == p2) {
            // we can't do union since they belong to the same component.
            return false;
        }

        // wherever we are assigning the parent means we are directly connecting those two nodes.
        if (size[p1] < size[p2]) {
            // attaching ultimate parent of 'n1' i.e p1 to ultimate parent of 'n2' i.e p2.
            parent[p1] = p2;
            size[p2] += size[p1]; // increase the size of p2 by size of p1.
        } else {
            // rank[p1]>= rank[p2]
            // attaching ultimate parent of 'n2' i.e p2 to ultimate parent of 'n1' i.e p1.
            parent[p2] = p1;
            size[p1] += size[p2];
        }
        return true;
    }
}

class Solution {
    public int makeConnected(int n, int[][] connections) {
        if (connections.length < n - 1) {
            return -1;
        }

        DSU dsu = new DSU(n);

        for (int[] edge : connections) {
            int n1 = edge[0], n2 = edge[1];
            dsu.unionBySize(n1, n2);
        }

        int component = 0;
        for (int i = 0; i < n; i++) {
            if (dsu.parent[i] == i) {
                component++;
            }
        }

        return component - 1;
    }
}


"""


# C++
"""
#include <vector>
using namespace std;

class DSU {
public:
    int v;
    vector<int> parent, size;

    DSU(int n) {
        v = n;
        parent.resize(n);          // here '0' based indexing is used in Q.
        size.assign(n, 1);         // will give the size of each parent component.
                                   // initially size of all be '1'(node itself).
        for (int i = 0; i < n; ++i) {
            parent[i] = i;
        }
    }

    // finding the ultimate parent
    int findUPar(int n) {
        if (n == parent[n]) {
            // Root parent will be the parent of itself. so continue till we find that.
            return n;
        }

        // This is called path compression.
        return parent[n] = findUPar(parent[n]);
    }

    bool unionBySize(int n1, int n2) {
        int p1 = findUPar(n1);
        int p2 = findUPar(n2);

        if (p1 == p2) {
            // we can't do union since they belong to the same component.
            return false;
        }

        // wherever we are assigning the parent means we are directly connecting those two nodes.
        if (size[p1] < size[p2]) {
            // attaching ultimate parent of 'n1' i.e p1 to ultimate parent of 'n2' i.e p2.
            parent[p1] = p2;
            size[p2] += size[p1];  // increase the size of p2 by size of p1.
        } else {
            // size[p1] >= size[p2]
            // attaching ultimate parent of 'n2' i.e p2 to ultimate parent of 'n1' i.e p1.
            parent[p2] = p1;
            size[p1] += size[p2];
        }

        return true;
    }
};

class Solution {
public:
    int makeConnected(int n, vector<vector<int>>& connections) {
        if (connections.size() < n - 1) {
            return -1;
        }

        DSU dsu(n);

        for (auto& edge : connections) {
            int n1 = edge[0], n2 = edge[1];
            dsu.unionBySize(n1, n2);
        }

        int component = 0;
        for (int i = 0; i < n; ++i) {
            if (dsu.parent[i] == i) {
                component++;
            }
        }

        return component - 1;
    }
};


"""