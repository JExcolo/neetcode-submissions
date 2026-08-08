# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverser(head, None)
        
    def reverser(self, head, prev):
        if head is None:
            return prev
        
        temp = head.next
        head.next = prev
        return self.reverser(temp, head)
        