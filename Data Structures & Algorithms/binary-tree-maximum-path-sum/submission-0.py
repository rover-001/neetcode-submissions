class Solution:
    def maxPathSum(self, root):
        self.maximum = float('-inf')

        def dfs(node):
            if node is None:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Path passing through current node
            current = node.val + left + right

            self.maximum = max(self.maximum, current)

            # Return the best single-side path to parent
            return node.val + max(left, right)

        dfs(root)
        return self.maximum