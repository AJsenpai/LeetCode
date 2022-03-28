from collections import deque
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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return 
        
        queue = deque()
        queue.append(root)
        
        while queue:
            level_size = len(queue)
            previous = None
            
            for _ in range(level_size):
                curr_node = queue.popleft()
                
                if previous:
                    previous.next = curr_node
                previous = curr_node
                
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
        return root

        
# O(1)  S | O(N) T
#     def connect(self, root):
#         head = root
#         while root:
#             cur, root = root, root.left
#             while cur:
#                 if cur.left:
#                     cur.left.next = cur.right
#                     if cur.next: cur.right.next = cur.next.left
#                 else: break
#                 cur = cur.next
                
#         return head