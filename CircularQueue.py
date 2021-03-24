import array

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.isFull = False
        self.array = array.array('l', [0]*capacity)

    def put(self, value):
        if self.isFull is True:
            print('큐가 가득 찼습니다.')
            return False

        self.array[self.rear] = value
        self.rear = (self.rear + 1) % (self.capacity)

        if self.rear == self.front:
            self.isFull = True

    def get(self):
        if self.isFull is False and self.rear == self.front:
            print('큐가 비어 있습니다.')
            return False

        value = self.array[self.front]
        self.front = (self.front + 1) % (self.capacity)
        self.isFull = False
        return value

    def peek(self):
        if self.isFull is False and self.rear == self.front:
            print('큐가 비어 있습니다.')
            return False

        return self.array[self.front]

    def print(self):
        s = ''
        startIdx = self.front
        endIdx = self.rear

        if self.rear == self.front and self.isFull is False:
            print('[]')
            return

        if endIdx <= startIdx:
            endIdx += self.capacity

        for i in range(startIdx, endIdx):
            s += str(self.array[i % self.capacity]) + ' '

        print(s)

queue = CircularQueue(5)
queue.print()

queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)
queue.put(6)
queue.print()

print(queue.get())
print(queue.get())
print(queue.get())
print(queue.get())
queue.print()

print(queue.get())
print(queue.get())
print(queue.get())

queue.put(4)
queue.put(5)
queue.put(6)
queue.print()

print(queue.get())
print(queue.get())
print(queue.get())
queue.print()