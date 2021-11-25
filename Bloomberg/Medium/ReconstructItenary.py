

class Solution:
    def findItinerary(self, tickets):
        # DFS, But we are not marking visited for outgoing flights from visited nodes
        
        self.adj = {}
        tickets.sort(key = lambda x: x[1])
        
        for u,v in tickets:
            if u in self.adj: self.adj[u].append(v)
            else: self.adj[u] = [v]

        # { JFK: [SFO, ATL], ATL: [JFK, SFO], SFO: [ATL]}
        # run DFS
        self.result = []
        self.dfs("JFK")
        
        return self.result[::-1]
    
    def dfs(self, s):
        while s in self.adj and len(self.adj[s]) > 0:
            v = self.adj[s][0]
            self.adj[s].pop(0)
            self.dfs(v)
            
        self.result.append(s)
                
        