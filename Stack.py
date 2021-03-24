import array

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = 0
        self.array = array.array('l', [0]*capacity)
    
    def push(self, value):
        if self.capacity == self.top:
            print('스택 오버 플로우')
        else:
            self.array[self.top] = value
            self.top += 1

    def pop(self):
        if self.top == 0:
            return '스택이 비어있습니다.'
        else:
            self.top -= 1
            return self.array[self.top]

    def peek(self):
        if self.top == 0:
            return None
        else:
            return self.array[self.top-1]
    
    def is_empty(self):
        return not bool(self.top)

    def print(self):
        for i in range(self.top):
            print(self.array[i], end=' ')
        print()

# 크기가 4인 스택 array 생성
stack = Stack(4)

# is_empty 함수 테스트
print(stack.is_empty())

# push 함수 테스트
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

# print 함수 테스트
stack.print()

# array가 꽉 차있을때 push 함수 테스트
stack.push(5)
stack.print()

# pop 함수 테스트
print(stack.pop())
print(stack.pop())
stack.print()

# peek 함수 테스트
print(stack.peek())
stack.print()

# pop으로 전체 array 비우기
print(stack.pop())
print(stack.pop())
print(stack.pop())
stack.print()
