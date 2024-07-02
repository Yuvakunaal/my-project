class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self, element):
        if len(self.stack) == self.size:
            print("Stack overflow")
        else:
            self.stack.append(element)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack underflow")
        else:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.size

    def show_size(self):
        return len(self.stack)

    def display(self):
        return self.stack

postfix = input("Enter valid postfix : ").strip()
s = Stack(len(postfix))
p = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2}
for i in postfix:
    if i in p:
        op1 = s.pop()
        op2 = s.pop()
        a = op2 + i + op1 
        s.push(a)
    else: 
        s.push(i)
infix = s.pop()
print(infix)