class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        idx = ["type","color","name"].index(ruleKey)
        return len([i for i in items if i[idx] == ruleValue])