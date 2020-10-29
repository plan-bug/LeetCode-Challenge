class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = []
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.split('.')
            local = ''.join(local)
            result.append(local + '@' + domain)
        
        return len(list(set(result)))
