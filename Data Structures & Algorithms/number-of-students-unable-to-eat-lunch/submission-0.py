class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = None
        # self.prev

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        head = Node(None)
        curr = Node(students[0])
        head.next = curr
        tail = curr
        for i in range(1, len(students)):
            new = Node(students[i])
            curr.next = new
            curr = curr.next
            tail = curr
        
        point = tail
        ind = 0
        grabbed = 0
        student = head.next
        while ind < len(sandwiches):
            if sandwiches[ind] == student.val:
                grabbed += 1
                head.next = student.next
                student.next = None
                student = head.next
                ind += 1
                point = tail
            elif student == point:
                return len(students) - grabbed
            else:
                head.next = student.next
                tail.next = student
                student.next = None
                tail = student
                student = head.next

        
        return 0
            


            
