#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        all_paths = []
        current_path = []

        def dfs(node: TreeNode | None, remaining_sum: int):
            if not node:
                return

            current_path.append(node.val)
            
            if not node.left and not node.right: # Check if it's a leaf node
                if remaining_sum - node.val == 0:
                    all_paths.append(list(current_path))
            else:
                dfs(node.left, remaining_sum - node.val)
                dfs(node.right, remaining_sum - node.val)
            
            current_path.pop() # Backtrack

        dfs(root, targetSum)
        return all_paths
# @lc code=end
