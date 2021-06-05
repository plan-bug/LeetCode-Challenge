class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        maxNum = max(nums)
        idx = nums.index(maxNum)
        node = TreeNode(maxNum)
        node.left = self.constructMaximumBinaryTree(nums[:idx])
        node.right = self.constructMaximumBinaryTree(nums[idx + 1 :])
        return node
