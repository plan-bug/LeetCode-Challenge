# or 의 이유
# 처음의 if not original 일때 return 이 None이기 때문
# 어느 쪽에서든 node가 none이 되면 다음 함수로 넘어가는 것이 아니라 그 순간 None이 되고 함수가 종료되기 때문에 or을 통해 True가 있을 때까지 감
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        if original == target:
            return cloned

        return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)
