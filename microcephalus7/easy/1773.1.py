class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        return len([0 for t,c,n in items if (ruleKey,ruleValue) in (("type",t),("color",c),("name",n))])