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


def prefix_to_infix(prefix):
    s = Stack(len(prefix))
    p = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2}
    infix = []
    for ch in reversed(prefix):
        if ch in p:
            # op1 = "(" + infix.pop() + ")" if infix else ""
            # op2 = "(" + infix.pop() + ")" if infix else ""
            op1 = infix.pop()
            op2 = infix.pop()
            result = op1 + ch + op2
            infix.append(result)
        else: 
            infix.append(ch)

    return infix.pop()


prefix_expression = "+ab"
infix_expression = prefix_to_infix(prefix_expression)
print("Infix expression:", infix_expression)
