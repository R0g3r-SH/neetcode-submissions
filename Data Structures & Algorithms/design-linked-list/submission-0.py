class Node :
    def __init__ (self,val,next_node = None):
        self.val = val
        self.next = next_node

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
        

    def get(self, index: int) -> int:

        curr = self.head.next
        i=0

        while curr:
            if index == i:
                return curr.val
            
            curr = curr.next
            i+=1

        return -1
                
        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node

        if not new_node.next:
            self.tail = new_node
        

    def addAtTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        

    def addAtIndex(self, index: int, val: int) -> None:

        i = 0
        curr = self.head

        while i < index and curr:
            i+=1
            curr = curr.next

        new_node = Node(val)

        if curr:
            
            new_node.next = curr.next
            curr.next = new_node

            if new_node.next is None:
                self.tail = new_node

        

    def deleteAtIndex(self, index: int) -> None:

        i  = 0 
        curr = self.head

        while i < index and curr:
            i+=1
            curr = curr.next
        
        if curr and curr.next:

            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next

            return True


        return False
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)