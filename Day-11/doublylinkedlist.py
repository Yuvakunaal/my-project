class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList :
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head == None :
            self.head = new_node
        else:
            current = self.head
            while current.next!=None:
                current = current.next
            current.next = new_node
            new_node.prev = current
    def insert_at_key(self,data,key):
        new_node = Node(data)
        if key == 0:
            self.insert_at_beginning(data)
        else:
            current = self.head
            count = 0
            while current is not None and count < key - 1:
                current = current.next
                count += 1

            if current is None:
                print("count exceeds the key. adding at the end.")
                self.insert_at_end(data)
            else:
                new_node.next = current.next
                current.next = new_node
    def delete_at_beginning(self):
        if self.head == None:
            print("Empty linkedlist")
        else:
            self.head = self.head.next
            self.head.prev = None
    def delete_at_end(self):
        if self.head == None:
            print("Empty linkedlist")
        else:
            current = self.head
            while current.next.next != None:
                current = current.next
            current.next.prev = None
            current.next = None
    def delete_at_key(self,key):
        if self.head is None:
            print("List is empty")
            return
        if key == 0:
            self.delete_from_begin()
        else:
            current = self.head
            count = 0
            while current and count < key:
                current = current.next
                count += 1
            if current is None:
                print("count exceeds the key value, key doesn't exist!!!")
                return
            if current.next is not None:
                current.next.prev = current.prev
            if current.prev is not None:
                current.prev.next = current.next
            if current == self.head:  # If we are deleting the head node
                self.head = current.next
    def display(self):
        current = self.head
        print("None",end=" <-> ")
        while current!=None :
            print(current.data,end=" <-> ")
            current=current.next
        print("None")

dll = DoublyLinkedList()
dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_end(30)
dll.insert_at_key(90,3)

dll.display()

dll.delete_at_beginning()
dll.display()

dll.delete_at_end()
dll.display()

dll.delete_at_key(10)
dll.display()