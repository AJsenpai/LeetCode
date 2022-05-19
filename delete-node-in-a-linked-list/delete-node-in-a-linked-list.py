# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # if self.head.val == node.val:
        #     self.head = self.head.next
        # curr_node = self.head
        # while curr_node and curr_node.val!= node.val:
        #     curr_node = curr_node.next
        
        node.val = node.next.val
        node.next= node.next.next
            