# class Node(object):
#   def __init__(self, value = None, pointer = None):
#     self.value = value
#     self.pointer = pointer
  
# class Queue(object):
#   def __init__(self):
#     self.head = None
#     self.tail = None
#     self.count = 0
  
#   def dequeue(self):
#     if self.head != None:
#       node = self.head  
#       self.head = node.pointer
#       self.count -= 1
      
#       return node.value
#     else :
#       return "Queue is Empty"

#   def enqueue(self, item):
#     node = Node(item)
    
#     if not self.head:
#       self.head = node
#       self.tail = node
#     else:
#       if self.tail:
#         self.tail.pointer = node
#       self.tail = node
    
#     self.count += 1 

#   def print_queue(self):
#     node = self.head
    
#     while node:
#       print(node.value, end=" ")
#       node = node.pointer

#     print()

#   def size(self):
#     return self.count

class Node(object): 
  def __init__(self, value = None, pointer = None ):
    self.value = value
    self.pointer = pointer

class Queue(object):
  def __init__(self):
    self.head = None
    self.tail = None
    self.count = 0
  
  def enqueue(self, item):
    node = Node(item)
    
    if not self.head:
      self.head = node
      self.tail = node
    else :
      self.tail.pointer = node
      self.tail = node

    self.count += 1
  
  def dequeue(self):
    if self.head:
      item = self.head
      self.head = item.pointer
      self.count -= 1

      return item.value
    else :
      return "Queue is empty"
  
  def print_queue(self):
    node = self.head
    while node:
      print(node.value, end=" ")
      node = node.pointer
    print()

  def isEmpty(self):
    return not bool(self.head)
  
  def size(self):
    return self.count

  def peek(self):
    return self.tail.value

queue = Queue()

for index in range(10):
  queue.enqueue(index)

queue.print_queue()
print(queue.size())
print(queue.dequeue())
queue.print_queue()
print(queue.size())
queue.enqueue(10)
queue.print_queue()

print(queue.dequeue())
print(queue.peek())


# class Queue2(object):
#   def __init__(self):
#     self.queue = []
  
#   def enqueue(self, item):
#     self.queue.append(item)

#   def dequeue(self):
#     if self.queue:
#       return self.queue.pop(0)
#     else:
#       return "Queue is empty"
