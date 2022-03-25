# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next        


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 
        
        minheap = [] # merging low to high
        
        for i,head in enumerate(lists):
            if head:
                heappush(minheap, (head.val, i, head))                
        
        head,tail = None,None # new linked list
        while minheap:
            node_val, i, node = heappop(minheap)
            
            if head is None:
                head=tail = node
            else:
                tail.next=  node
                tail = node
            
            if node.next is not None:
                heappush(minheap, (node.next.val,i, node.next))
        return head
        