# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        output = []
        sets = set()
        map = {}
        for arr in lists:
            curr = arr
            while curr is not None:
                sets.add(curr.val)
                if curr.val in map:
                    map[curr.val] += 1
                else:
                    map[curr.val] = 1
                curr = curr.next
        for num in sorted(sets):
            for i in range(map[num]):
                output.append(num)

        dummy = ListNode()
        curr = dummy
        for val in output:
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next

        
        