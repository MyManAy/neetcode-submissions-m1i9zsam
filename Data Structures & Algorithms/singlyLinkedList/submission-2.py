class LinkedNode:
    def __init__(self, val, next_node):
        self.val = val
        self.next = next_node

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        node = self.head
        for i in range(0, index):
            if node is None:
                return -1
            node = node.next
        if node is None:
            return -1
        return node.val
        

    def insertHead(self, val: int) -> None:
        if self.head is None:
            node = LinkedNode(val, None)
            self.head = node
            self.tail = self.head
        else:
            node = LinkedNode(val, self.head)
            self.head = node
        print(self.getValues())


    def insertTail(self, val: int) -> None:
        if self.tail is None:
            node = LinkedNode(val, None)
            self.tail = node
            self.head = self.tail
        else:
            node = LinkedNode(val, None)
            self.tail.next = node
            self.tail = self.tail.next
        print(self.getValues())
        

    def remove(self, index: int) -> bool:
        if index == 0 and self.head:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return True

        i = 0
        curr = self.head
        while i < index and curr:
            if curr.next:
                if i == index-1:
                    if curr.next == self.tail:
                        self.tail = curr
                    curr.next = curr.next.next
                    return True
            i += 1
            curr = curr.next
        
        # Remove the node ahead of curr
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        node = self.head
        values = []
        while node is not None:
            values.append(node.val)
            node = node.next
        return values
        
