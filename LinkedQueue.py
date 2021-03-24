class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next
    
class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def put(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            self.tail.next = Node(value, self.tail, None)
            self.tail = self.tail.next


    def get(self):
        if self.head is None:
            print('Queue is Empty!')
            return False
        else:
            self.head = self.head.next
    
    def peek(self):
        if self.head is None:
            print('Queue is Empty!')
        else:
            return self.head.value

    def print(self):
        if self.head is None:
            print('[]', end=' ')
        else:
            cur_node = self.head
            while cur_node is not None:
                print(cur_node.value, end=' ')
                cur_node = cur_node.next
        print()

# 비어있는 연결리스트 큐 생성
queue = LinkedQueue()

# 비어있는 큐에 print함수 테스트
queue.print()

# put함수 테스트
queue.put(2)
queue.put(5)
queue.put(4)

# peek함수 테스트
print(queue.peek())

# 자료가 있는 큐에 print함수 테스트
queue.print()

# get함수 테스트
queue.get()
queue.get()
queue.print()

# 비어있는 큐에 get함수 테스트
queue.get()
queue.get()




