def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    self.levels = []
    if root == None:
        return []

    stack = [root]

    while stack:
        next_level_nodes = []
        current_lvl = []
        for node in stack:
            current_lvl.append(node.val)
            if node.left:
                next_level_nodes.append(node.left)
            if node.right:
                next_level_nodes.append(node.right)
        stack = next_level_nodes
        self.levels.insert(0, current_lvl)
    return self.levels
