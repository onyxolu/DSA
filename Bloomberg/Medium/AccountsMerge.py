

from collections import defaultdict

# It's a merging problem
# dfs 
# build graph, edges is node (connecting to names with same emails), vertex is each email, we use dfs to find emails in the same group
# 0(nmlogm)

class Solution:
    def accountsMerge(self, accounts):
        graph = defaultdict(set)
        emailToName = {}
        
        for acct in accounts:
            name = acct[0]
            
            # Build edge for all emails
            email1 = acct[1]
            emailToName[email1] = name
            for email2 in acct[2:]:
                graph[email1].add(email2)
                graph[email2].add(email1)
                emailToName[email2] = name
                
        ans = []
        seen = set()
        
        # dfs with stack
        for email in emailToName:
            if email not in seen:
                stack = [email]
                seen.add(email)
                emails = []
                
                while stack:
                    cur = stack.pop()
                    emails.append(cur)
                    
                    for nei in graph[cur]:
                        if nei not in seen:
                            stack.append(nei)
                            seen.add(nei)
                ans.append([emailToName[email]] + sorted(emails))
        return ans
        


# Union Find


class Solution:
    def accountsMerge(self, accounts):
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
                
            return parents[x]
        
        def union(x,y):
            r1 = find(x)
            r2 = find(y)
            
            if r1 != r2:
                parents[r2] = r1
            
        parents = {}
        emailToName = {}
        
        # map emails to name
        # map children emails to parents
        for acct in accounts:
            name = acct[0]
            for email in acct[1:]:
                emailToName[email] = name
                parents[email] = email
                
        print(parents)
        
#         {'johnsmith@mail.com': 'johnsmith@mail.com', 'john_newyork@mail.com': 'john_newyork@mail.com', 'john00@mail.com': 'john00@mail.com', 'mary@mail.com': 'mary@mail.com', 'johnnybravo@mail.com': 'johnnybravo@mail.com'}
# 

              
        # union all emails with first email
        for acct in accounts:
            email1 = acct[1]
            for email2 in acct[2:]:
                union(email1,email2)
                
        groups = defaultdict(list)
        
        # find groups
        for email in parents:
            r = find(email)
            groups[r].append(email)
            
        ans = []
        print(groups)
        
        # defaultdict(<class 'list'>, {'johnsmith@mail.com': ['johnsmith@mail.com', 'john_newyork@mail.com', 'john00@mail.com'], 'mary@mail.com': ['mary@mail.com'], 'johnnybravo@mail.com': ['johnnybravo@mail.com']})
        
        for key in groups:
            ans.append([emailToName[key]] + sorted(groups[key]))
            
        return ans
        