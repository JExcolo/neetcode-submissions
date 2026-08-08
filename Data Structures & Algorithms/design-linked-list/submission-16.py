class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.len = 0
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.len:
            return -1
        
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next.prev = new_node
        self.len += 1
        

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.prev = self.tail.prev
        new_node.next = self.tail

        new_node.prev.next = new_node
        self.tail.prev = new_node
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.len:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.len:
            self.addAtTail(val)
            return
        curr = self.head
        for _ in range(index):
            curr = curr.next
        new_node = ListNode(val)
        new_node.prev = curr

        new_node.next = curr.next
        curr.next.prev = new_node
        curr.next = new_node
        self.len += 1
        
        
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.len:
            return
        curr = self.head
        for _ in range(index):
            curr = curr.next
        far = curr.next.next
        curr.next = far
        far.prev = curr
        self.len -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)