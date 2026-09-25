#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        self.prev = None

        def traverse(node):
            if not node:
                return

            traverse(node.right)
            traverse(node.left)

            node.right = self.prev
            node.left = None
            self.prev = node

        traverse(root)
# @lc code=end
