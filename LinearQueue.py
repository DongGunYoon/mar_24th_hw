import array

class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.isEmpty = True
        self.array = array.array('l', [0]*capacity)

    def put(self, value):
        if self.rear == self.capacity:
            print('Queue is Full!')
            return False

        self.array[self.rear] = value
        self.rear += 1
        self.isEmpty = False

    def get(self):
        if self.isEmpty is True:
            print("Queue is Empty!")
            return False

        value = self.array[self.front]
        self.front += 1
        if self.front == self.rear:
            self.isEmpty = True
        
        return value

    def peek(self):
        if self.isEmpty is True:
            print("Queue is Empty!")
            return False
        
        return self.array[self.front]

    def print(self):
        if self.isEmpty is True:
            print('[]', end=' ')
        
        for i in range(self.front, self.rear):
            print(self.array[i], end=" ")
        print()

# 크기가 5인 선형 큐 생성
linear = LinearQueue(5)

# 비어있는 상황 print함수 테스트
linear.print()

# 비어있는 상황 get함수 테스트
linear.get()

# put 함수 테스트
linear.put(3)
linear.put(5)
linear.put(7)
linear.put(9)
linear.put(11)

# 큐가 가득 찬 상태에서 put함수 테스트
linear.put(13)
linear.print()

# get 함수 테스트
linear.get()
linear.get()

# get 함수 정상 작동 테스트
linear.print()

# peek 함수 정상 작동 테스트
print(linear.peek())