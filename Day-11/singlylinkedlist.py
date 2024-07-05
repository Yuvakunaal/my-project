class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SinglyLinkedList :
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        new_node = Node(data)
        if self.head is None :
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None :
            self.head = new_node
        else :
            current = self.head
            while current.next is not None :
                current = current.next
            current.next = new_node
    def insert_at_key(self,data,key):
        new_node = Node(data)
        if key == 0:
            self.insert_at_beginning(data)
        else:
            current = self.head
            count = 0
            while current is not None and count < key-1:
                current = current.next
                count+=1
            if current is None:
                print("count exceeded the key value. so adding at end!!!")
                self.insert_at_end(data)
            else:
                new_node.next = current.next
                current.next = new_node
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty!!!")
            return
        self.head = self.head.next
    def delete_at_end(self):
        if self.head is None:
            print("List is empty!!!")
            return
        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None
    def delete_at_key(self,key):
        if self.head is None:
            print("List is empty!!!")
            return
        if key == 0:
            self.delete_at_beginning()
        else:
            current = self.head
            count = 0
            while current is not None and count < key-1:
                current = current.next
                count+=1
            if current is None or current.next is None:
                print("Key doesnot exist in list!!!")
            else:
                current.next = current.next.next
                
sll = SinglyLinkedList()
sll.insert_at_beginning(10)
sll.insert_at_beginning(20)
sll.insert_at_end(30)
sll.insert_at_key(90,3)

sll.display()

sll.delete_at_beginning()
sll.display()

sll.delete_at_end()
sll.display()

sll.delete_at_key(10)
sll.display()
