class Node(object):
  def __init__(self, data = None, prev = None, next = None):
    self.data = data
    self.prev = prev
    self.next = next

class Double_linked(object):
  def __init__(self):
    self.head = None
    self.tail = None
    self.count = 0

  def add(self, data):
    # empty list 
    if self.isEmpty():
      new_node = Node(data)
      self.head = new_node
      self.tail = new_node
      self.count += 1
    else :
      node = self.head

      while node.next:
        node = node.next 
      
      new_node = Node(data)
      node.next = new_node
      new_node.prev = node
      self.tail = new_node
      self.count += 1
  
  def insert(self, target, data):
    if self.isEmpty():
      return print ('Empty List !')

    node = self.head
    while node.next:
      if node.next.data == target:
          new_node = Node(data)
          node.next.prev = new_node
          new_node.next = node.next
          new_node.prev = node
          node.next = new_node
          self.count += 1 
          return
      else:    
        node = node.next

    print('Item not found')

  def descript(self,item):
    if self.isEmpty():
      return print('Empty list !')

    node = self.head
    while node.next:
      if node.data == item:
        if node == self.head:
          print(f'Now : {node.data}\nPrev : {None}\nNext : {node.next.data}')
        else:
          print(f'Now : {node.data}\nPrev : {node.prev.data}\nNext : {node.next.data}')
        return 
      else: 
        node = node.next
    if node.data == item:
      print(f'Now : {node.data}\nPrev : {node.prev.data}\nNext : {None}')
      return 
    
    print("Item not found")

  def asc_read(self):
    if self.isEmpty():
      return print ('Empty List !')

    node = self.head
    while node.next:
      print(node.data, end=" ") 
      node = node.next
    print(node.data)

  def desc_read(self):
    if self.isEmpty():
      return print('Empty List!')

    node = self.tail
    while node.prev:
      print(node.data, end=" ")
      node = node.prev
    print(node.data)

  def isEmpty(self):
     return not bool(self.head or self.tail) 
  
  def size(self):
    return self.count

list = Double_linked()

print(list.size())

for index in range(10):
  list.add(index)

list.desc_read()
list.asc_read()
list.insert(5,4.5)
list.asc_read()
list.descript(4)