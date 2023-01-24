# how to think about DSU.
# for simplicity replace the name->0,1,2... for each account.
# just traverse through mails for each account and keep mapping with its account_no if doesn't eaxist in map.
# if exist in map then connect those account into one component by calling the function union.

# after creating map, find all the merged mail of each account into a list of list by traversing through the items in map.
# VVI: But add mail to the ultimate parent.. 
# And at last add name before merged  mail.

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


# Later try by DFS also.