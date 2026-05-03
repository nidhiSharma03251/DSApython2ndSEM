class Queue:
    def __init__(self, size):
        self.size = size
        self.items = [0] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if self.rear == self.size - 1:
            print("Queue is full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.items[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            val = self.items[self.front]
            self.items[self.front] = 0
            self.front += 1
            return val

    def size(self):
        return len(self.items)

q = Queue(5)
 
q.enqueue("apple")
q.enqueue("banana")
# print(q.size()) 
print(q.dequeue()) 
# print(q.size()) 

