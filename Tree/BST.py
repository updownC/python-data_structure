import random

class Node(object):
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None

class BST(object):
  def __init__(self):
    self.root = None
    self.count = 0

  def insert(self, value):
    if not self.root:
      self.root = Node(value)
      self.count += 1
      return
    
    current_node = self.root

    while True:
      if value < current_node.value:
        if current_node.left:
          current_node = current_node.left
        else:
          current_node.left = Node(value)
          self.count += 1
          return
      elif value > current_node.value:
        if current_node.right:
          current_node = current_node.right
        else:
          current_node.right = Node(value)
          self.count += 1 
          return
    
  def include(self, value):
    if not self.root:
      return "Empty Tree!"

    current_node = self.root

    while current_node:
      if value == current_node.value:
        return True
      elif value > current_node.value:
        current_node = current_node.right
      elif value < current_node.value:
        current_node = current_node.left
    
    return False  

  def delete(self, value):
    if not self.root:
      return "Empty Tree"

    has_node = False
    current = self.root
    parent = self.root
    
    # tree 탐색 하면서 해당 node 가지고 있는지 확인, 
    while current:
      if value == current.value:
        has_node = True
        break
      elif value < current.value:
        parent = current
        current = current.left
      elif value > current.value:
        parent = current
        current = current.right

    # 트리 전체 탐색 결과 해당 node가 존재하지 않으면 매서드 종료
    if not has_node:
      print(current.value)
      return print('value not found')

    # 1.해당 node가 leaf node인 경우 
    if not current.left and not current.right:
      if value < parent.value:
        print (f'DELETE : {current.value}')
        parent.left = None
        self.count -= 1
        del current
        
        return
      else: 
        print (f'DELETE : {current.value}')
        parent.right = None
        self.count -= 1
        del current
        
        return
    # 2.해당 node 가 하나의 child를 가진 경우
    # 2-1. 하나의 child가 해당 노드의 left인 경우 
    if current.left and not current.right:
      if value < parent.value:
        parent.left = current.left
        print (f'DELETE : {current.value}')
        del current
        self.count -= 1
        
        return
      else:
        parent.right = current.left
        print (f'DELETE : {current.value}')
        del current
        self.count -= 1
        
        return
    # 2-2. 하나의 child가 해당 노드의 right인 경우 
    elif not current.left and current.right:
      if value < parent.value:
        parent.left = current.right
        print (f'DELETE : {current.value}')
        del current
        self.count -= 1
        
        return
      else:
        parent.right = current.right
        print (f'DELETE : {current.value}')
        del current
        self.count -= 1
        
        return
    # 3. 해당 node의 자식이 두개인 경우.
    # - 유지해야하는 정보 : 삭제할 노드, 삭제할 노드의 부모, 자리를 채울 노드, 자리 채울 노드의 부모 
    if current.right and current.left :
      # 부모노드 기준 왼쪽 node인 경우
      if value < parent.value :
        change_node_parent = current.right
        change_node = current.right
        # 삭제하고자 하는 노드의 오른쪽 subtree에서 최소value노드 탐색
        while change_node.left:
          change_node_parent = change_node
          change_node = change_node.left
        # 해당 노드의 오른쪽 자식이 있으면 부모 노드의 왼쪽에 삽입
        if change_node.right:
          change_node_parent.left = change_node.right
        else: 
          change_node_parent.left = None
        # 삭제하고자 하는 노드의 위치로 돌아와서, 해당 노드의 부모 좌측에 탐색된 노드 삽입 
        parent.left = change_node
        change_node.left = current.left
        change_node.right = current.right

        print (f'DELETE : {current.value}')
        print (f'NOW : {parent.left.value}, {change_node.value}')
        del current
        self.count -= 1
      else :
        change_node_parent = current.right
        change_node = current.right
        while change_node.left:
          change_node_parent = change_node
          change_node = change_node.left
        if change_node.right :
          change_node_parent.left = change_node.right
        else: 
          change_node_parent = None
        parent.right = change_node
        change_node.left = current.left
        change_node.right = current.right

        print (f'DELETE : {current.value}')
        del current
        self.count -= 1

  def size(self):
    return self.count


# test code 
bst = BST()

# generate a set of randomly chosen numbers to create binary search tree
insert_set = set()
while len(insert_set) != 100:
  insert_set.add(random.randint(0,999))

# insert randomly generated numbers in binary search tree
for number in insert_set:
  bst.insert(number)

# print out the tree's size
print(bst.size())

# check wheather all the numbers in list inserted correctly
for number in insert_set:
  if bst.include(number) == False: 
    print('value not found')

# remove random 10 nodes from the tree
remove_set = set()
insert_list = list(insert_set)

while len(remove_set) != 10:
  remove_set.add(insert_list[random.randint(0,len(insert_list)-1)])

for number in remove_set:
  bst.delete(number)

# print out the tree size
print(bst.size())