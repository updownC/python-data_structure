class Node(object):
  def __init__(self, value = None, pointer = None):
    self.value = value
    self.pointer = pointer

class Stack(object):
  def __init__(self):
    self.head = None 
    self.count = 0 

  def isEmpty(self):
    return not bool(self.count)
  
  def push(self, item):
    self.head = Node(item, self.head)
    self.count += 1

  def pop(self):
    if self.head != None: 
      item = self.head
      self.head = self.head.pointer
      self.count -= 1
    
      return item.value

  def peek(self):
    return self.head.value

  def size(self):
    return self.count

  def print_stack(self):
    node = self.head
    while(node):
      print(node.value, end=" ")
      node = node.pointer
    print()

if __name__ == "__main__":
  stack=Stack()

for i in range(10):
  stack.push(i)

stack.print_stack()
print(stack.size())
print(stack.peek())
print(stack.pop())
stack.print_stack()
print(stack.pop())
stack.print_stack()