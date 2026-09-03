class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        pos = {value: i for i, value in enumerate(inorder)}
        preIndex = 0

        def helper(left, right):
            nonlocal preIndex

            if left > right:
                return None

            rootValue = preorder[preIndex]
            preIndex += 1

            root = TreeNode(rootValue)

            mid = pos[rootValue]

            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(inorder) - 1)