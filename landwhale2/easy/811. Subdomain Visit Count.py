class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomain = []
        counts = {}
        for cp_str in cpdomains:
            count, domain = cp_str.split(" ")
            count = int(count)
            
            try:
                counts[domain] += count 
            except:
                counts[domain] = count

            for idx, char in enumerate(domain):
                if char == '.':
                    try:
                        counts[domain[idx+1:]] += count
                    except:
                        counts[domain[idx+1:]] = count
        
        return [str(v) + ' ' + k for k,v in counts.items()]
            
