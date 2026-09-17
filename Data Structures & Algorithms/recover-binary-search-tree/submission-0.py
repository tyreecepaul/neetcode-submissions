class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node1, node2 = None, None
        prev = None

        def inorder(node):
            nonlocal node1, node2, prev
            if not node:
                return
            inorder(node.left)
            if prev and prev.val > node.val:
                if not node1:
                    node1 = prev
                node2 = node
            prev = node
            inorder(node.right)

        inorder(root)
        if node1 and node2:
            node1.val, node2.val = node2.val, node1.val