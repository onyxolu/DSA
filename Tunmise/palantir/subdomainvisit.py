class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        seen = {}
        result = []
        for site in cpdomains:
            count = int(site.split()[0])
            url = site.split()[1]
            subDomains = url.split(".")
            while subDomains:
                key = '.'.join(subDomains)
                if seen.get(key) is None:
                    seen[key] = count
                else:
                    seen[key] += count
                    
                subDomains.pop(0)   # remove the leaf from the front 

                
            
        result = [ str(v) + " " + k  for k, v in seen.items() ]
        
        return result 