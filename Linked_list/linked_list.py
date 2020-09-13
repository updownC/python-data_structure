class Node(object):
  def __init__(self, value = None, pointer = None):
    self.value = value
    self.pointer = pointer

class Linked_list(object):
  def __init__(self):
    self.head = None
    self.count = 0 
  
  def add(self, item):
    if not self.head:
      self.head = Node(item)
      self.count += 1 
    else:
      node = self.head

      while node.pointer:
        node = node.pointer
      
      node.pointer = Node(item)
      self.count += 1

  def remove(self, item):
    # 0. node가 아무것도 존재하지 않을 때 
    if not self.head:
      print ("list가 비어있습니다.")
    else: 
      node = self.head
      # 1, head node 삭제
      if node.value == item:
        self.head = node.pointer
        self.count -= 1
        del node
        return

      while node.pointer:
        # 나머지 node 삭제
        if node.pointer.value == item:
          target_node = node.pointer
          node.pointer = target_node.pointer
          del target_node
          self.count -= 1  
          return 
        else:
          node = node.pointer  

      print ('해당 node를 찾을 수 없습니다')

  def insert(self, target, item):
    node = self.head
    is_target = False
    
    while not is_target:
      # 전체 순회 결과 target이 없는 경우
      if not node.pointer:
        return print('item이 존재하지 않습니다.') 
      # target을 찾은경우
      if node.pointer.value == target:
        is_target = True
      else:
        node = node.pointer
    
    target_node = node.pointer
    new_node = Node(item)
    node.pointer = new_node
    new_node.pointer = target_node

  def read(self):
    node = self.head
    while node.pointer:
      print(node.value, end=" ")
      node = node.pointer
    print(node.value)

  def size(self):
    print(self.count)

list = Linked_list()

for i in range(10):
  list.add(i)

list.read()
list.size()
list.insert(11,2.5)
list.read()
list.remove(9)
list.read()