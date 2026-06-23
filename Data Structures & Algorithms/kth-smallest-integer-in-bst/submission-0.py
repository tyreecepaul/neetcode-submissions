class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = k
        def dfs(root):
            if not root:
                return

            res = dfs(root.left)
            if res is not None: 
                return res

            self.cnt -= 1
            if not self.cnt:
                return root.val
            return dfs(root.right)
            
        return dfs(root)