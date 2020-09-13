class Stack(object):
  def __init__(self):
    self.stack = []

  def isEmpty(self):
    return not bool(self.stack)
  
  def push(self, item):
    self.stack.append(item)
    print("Now: ",self.stack)

  def pop(self):
    if len(self.stack) != 0:
      item = self.stack.pop()
      print("Now: ",self.stack)
      return item
    else:
      return "Stack is Empty"
  
  def peek(self):
    return self.stack[-1]

  def size(self):
    return len(self.stack)

if __name__ == "__main__":
  
  stack = Stack()

  print(f"스택이 비었습니까? {stack.isEmpty()}")
  for index in range(10):
    stack.push(index)
  print(f'스택의 크기: {stack.size()}')
  print(f'가장 마지막 아이템: {stack.peek()}')
  stack.pop()

  print(f'가장 마지막 아이템: {stack.peek()}')
  