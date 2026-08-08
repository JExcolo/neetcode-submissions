# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            # Set next node to temp storing its info
            temp = current.next
            # reverse the list direction at the current obj
            current.next = previous
            # Set this node to the previous node
            previous = current
            # Change the next node into the current node
            current = temp
        # Return the final node which is stored in current
        return previous



            

        