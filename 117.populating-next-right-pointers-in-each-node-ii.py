#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        level_start = root

        while level_start:
            dummy_head = Node(0) # A dummy node to serve as the head of the next level's linked list
            child_prev = dummy_head # Pointer to the last node added to the next level's linked list
            
            curr_level_node = level_start
            
            # Traverse the current level using the 'next' pointers
            while curr_level_node:
                # If a left child exists, link it to the next level's chain
                if curr_level_node.left:
                    child_prev.next = curr_level_node.left
                    child_prev = child_prev.next
                
                # If a right child exists, link it to the next level's chain
                if curr_level_node.right:
                    child_prev.next = curr_level_node.right
                    child_prev = child_prev.next
                
                # Move to the next node in the current level
                curr_level_node = curr_level_node.next
            
            # After processing all nodes in the current level, 
            # dummy_head.next will point to the first node of the next level.
            # Set level_start to this first node for the next iteration.
            # If dummy_head.next is None, it means no children were found, 
            # so we've reached the end of the tree.
            level_start = dummy_head.next
            
        return root
# @lc code=end
