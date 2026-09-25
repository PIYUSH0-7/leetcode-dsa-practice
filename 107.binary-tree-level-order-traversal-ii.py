#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        levels = []
        q = deque([root])

        while q:
            current_level_vals = []
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                current_level_vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levels.append(current_level_vals)
        
        return levels[::-1]
# @lc code=end
