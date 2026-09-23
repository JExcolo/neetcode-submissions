# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head

        while head and head.val == val:
            head = head.next

        prev = None
        curr = head
        while curr:
            prev = curr
            curr = curr.next
            while curr and curr.val == val:
                prev.next = curr.next
                curr = curr.next
        
        return head
            


        