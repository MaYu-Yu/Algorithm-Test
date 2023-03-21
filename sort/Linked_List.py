class Node():
    data = None
    next = None
    
    def __init__(self,data):
        self.data = data 
class Linked_list():
    head = None
    tail = None
    
    def push_front(self, data):
        node = Node(data)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
    def push_back(self, data):
        node = Node(data)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    def insert(self, index, data):
        current = self.head
        while current:
            if current.data == index:
                node = Node(data)
                node.next = current.next
                current.next = node
                break
            current = current.next
    def print_List(self):
        current = self.head
        if not current:
            print("Linked List is empty...")
            return 0
        while current:
            end = " -> " if current.next else " "
            print(current.data, end=end)
            current = current.next
        print()
if __name__ == "__main__":
    a = Linked_list()
    a.push_back(1)
    a.push_front(0)
    a.push_back(2)
    a.push_back(3)
    a.print_List()
    a.insert(2, 87)
    a.print_List()
