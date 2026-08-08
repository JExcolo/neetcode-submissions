class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        dummy = Node(0)
        self.head = dummy
        self.tail = dummy
        hp = Node(homepage)
        self.head.next = hp
        self.tail.prev = hp
        hp.prev = self.head
        hp.next = self.tail
        self.current_page = hp
        self.len = 1
        

    def visit(self, url: str) -> None:
        new_node = Node(url)
        new_node.prev = self.current_page
        self.current_page.next = new_node
        self.current_page = new_node
        self.tail.prev = self.current_page
        self.current_page.next = self.tail

 

    def back(self, steps: int) -> str:
        if self.current_page.prev == self.head:
            return self.current_page.val
        for _ in range(steps):
            if self.current_page == self.head:
                self.current_page = self.current_page.next
                break
            self.current_page = self.current_page.prev
        return self.current_page.val
        

    def forward(self, steps: int) -> str:
        if self.current_page.next == self.tail:
            return self.current_page.val
        for _ in range(steps):
            if self.current_page == self.tail:
                self.current_page = self.current_page.prev
                break
            self.current_page = self.current_page.next
        return self.current_page.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)