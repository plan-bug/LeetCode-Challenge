class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dic = {e.id: e for e in employees}
        return self.dfs(dic, id)

    def dfs(self, emp: dict, id: int) -> int:
        for e in emp[id].subordinates:
            emp[id].importance += self.dfs(emp, e)
        return emp[id].importance
