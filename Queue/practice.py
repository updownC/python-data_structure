class List_queue(object):
  def __init__(self):
    self.queue = []
    self.size = len(self.queue)

  def isEmpty(self):
    return not bool(len(self.queue))

  def enqueue(self, value):
    self.queue.append(value)
    self.size += 1
  
  def dequeue(self):
    self.size -= 1
    return self.queue.pop(0)

  def read(self):
    print(f'size: {self.size}')
    
    for value in self.queue:
      print(value, end=" ")
    
    print()

if __name__ == "__main__":
  list_queue = List_queue()

  list_queue.enqueue('2')
  list_queue.enqueue(1)
  list_queue.enqueue(7)
  list_queue.enqueue(10)
  list_queue.enqueue(9)

  list_queue.read()
  print(type(list_queue.dequeue()))
  print(type(list_queue.dequeue()))