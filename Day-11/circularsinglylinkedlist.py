class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CircularSingleLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        new_node = Node(data)
        if self.head==None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head==None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next!=self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
    def insert_at_key(self,data,key):
        new_node = Node(data)
        if key == 0:
            self.insert_at_begin(data)
        else:
            current = self.head
            count = 0
            while current.next != self.head and count < key - 1:
                current = current.next
                count += 1
            new_node.next = current.next
            current.next = new_node
    def delete_at_beginning(self):
        current = self.head
        if self.head==None:
            print("Empty linked list !!!")
        elif current.next==self.head:
            self.head = None
        else:
            while current.next!=self.head:
                current = current.next
            current.next = self.head.next
            self.head = current.next
    def delete_at_end(self):
        current = self.head
        if self.head==None:
            print("Empty linked list !!!")
        elif current.next == self.head:
            self.head = None
        else:
            while current.next.next!=self.head:
                current = current.next
            current.next = self.head
    def delete_at_key(self,key):
        if self.head is None:
            print("List is empty")
            return
        if key == 0:
            self.delete_from_begin()
            return
        current = self.head
        count = 0
        while current.next != self.head and count < key - 1:
            current = current.next
            count += 1
        if current.next == self.head or count < key - 1:
            print("count exceeds key value, key doesnt exist!")
        else:
            current.next = current.next.next
    def display(self):
        if self.head==None:
            print("None")
        else:
            current = self.head
            if current.next==self.head:
                print(current.data,end="🔄")
            else:
                while True:
                    print(current.data,end=" -> ")
                    current = current.next
                    if current==self.head:
                        print("🔄")
                        break

cll = CircularSingleLinkedList()
cll.insert_at_beginning(10)
cll.insert_at_beginning(20)
cll.insert_at_end(30)
cll.insert_at_key(90,3)

cll.display()

cll.delete_at_beginning()
cll.display()

cll.delete_at_end()
cll.display()

cll.delete_at_key(10)
cll.display()


