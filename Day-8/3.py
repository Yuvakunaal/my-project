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

infix1 = input("Enter valid infix expression : ").strip()
infix = infix1[::-1]
s = Stack(len(infix))
p = {"%" : 2,"*" :2,"/" : 2,"+" : 1,"-" : 1,")" : 0}
prefix = []
for ch in infix :
    if ch in ["+","-","*","/","%"] :
        while not s.isEmpty() and p[s.peek()]>=p[ch] :
            prefix.append(s.pop())
        s.push(ch)
    elif ch == ")" :
        s.push(ch)
    elif ch == "(" :
        while s.peek() != ")" :
            prefix.append(s.pop())
        s.pop()
    else:
        prefix.append(ch)
while not s.isEmpty():
    prefix.append(s.pop())

ans = "".join(prefix[::-1])
print(ans)