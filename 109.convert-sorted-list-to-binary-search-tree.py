#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
class Solution:
    current_list_node = None 

    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        if not head:
            return None

        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        self.current_list_node = head

        return self._build_bst_recursive(0, n - 1)

    def _build_bst_recursive(self, start_idx: int, end_idx: int) -> TreeNode | None:
        if start_idx > end_idx:
            return None

        mid_idx = (start_idx + end_idx) // 2

        left_child = self._build_bst_recursive(start_idx, mid_idx - 1)
        
        root = TreeNode(self.current_list_node.val)
        self.current_list_node = self.current_list_node.next
        
        root.left = left_child
        root.right = self._build_bst_recursive(mid_idx + 1, end_idx)

        return root
# @lc code=end
