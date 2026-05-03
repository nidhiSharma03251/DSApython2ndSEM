class Stack():
    def __init__(self, size):
        self.size = size
        self.stk = [0]*size
        self.top = -1

    def push(self, x):
        if self.top == self.size-1:
            print("Stack is full")
        else:
            self.top += 1
            self.stk[self.top] = x
            print("Pushed element: ", x)

    def pop(self):
        if self.top < 0:
            print("Stack is empty")
        else:
            val = self.stk[self.top]
            self.top -= 1
            return val


    def display(self):
        for i in range(self.top, -1, -1):
            print(self.stk[i], end=" ")


s = Stack(8)
s.display() 
print("\n")
s.push(1)
s.display() 
print("\n")
s.push(2)
s.display()
print("\n")
s.push(5)
s.display() 
print("\n")
print("Popped element: ", s.pop())
s.display() 