# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        curr = dummy

        while l1 and l2:

            v1 = l1.val
            v2 = l2.val

            if v1 < v2 :
                curr.next = ListNode(v1)
                l1 = l1.next
            else:
                curr.next = ListNode(v2)
                l2 = l2.next
            
            curr = curr.next
        
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return dummy.next