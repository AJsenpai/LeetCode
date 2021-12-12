class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for e in emails:
            name,domain = e.split('@')
            name = name.split('+')[0].replace('.', '')           
            seen.add(name+'@'+domain)
        # print(seen)
        return len(seen)
            