import random

class Node(object):
  def __init__(self, value, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right

class BST(object):
  # initiation, 빈 루트를 시작으로 하는 BST 생성
  def __init__(self):
    self.root = None
    self.size = 0
  
  # 빈 트리인지 아닌지 판단   
  def isEmpty(self):
    return not bool(self.root)
  
  # 노드 삽입
  def insert(self, value):
    # 트리가 비어있으면, 루트에 새로운 노드 삽입
    if self.isEmpty():
      self.root = Node(value)
      self.size += 1

      return 

    # 루트가 존재하는 경우, 루트 노드를 현재 노드로 설정 
    current = self.root
    
    # 빈 공간 찾을 때까지 반복
    while True:
      # 현재 노드 값보다 입력 값이 작은 경우
      if value < current.value:
        # 현재 노드의 왼쪽 자식 노드 자리에 값이 이미 존재하는 경우
        if current.left:
          # 현재 노드를 왼쪽 자식 노드로 설정
          current = current.left 
          # 비어있다면 
        else:
          # 새로운 노드 생성
          current.left = Node(value)
          self.size += 1
          
          return
      else :
        if current.right:
          current = current.right
        else:
          current.right = Node(value) 
          self.size += 1

          return
    
  # 트리에서 해당 노드 탐색 
  def include(self, value):
    if self.isEmpty():
      return "ERROR : Empty Tree"

    current = self.root

    while current:
      if value == current.value:
        return current
      elif value < current.value:
        current = current.left
      elif value > current.value:
        current = current.right

    return "ERROR : Value Not Found"
  
  # 노드 삭제
  # 탐색해야 하는 정보 : 0.현재 노드 보다 값이 큰 지/작은 지 1. 리프 노드인가, 2. 자식이 한개 있는가. 3. 자식이 두개 있는가
  # 유지해야 하는 정보 : 1. 현재노드, 2.부모노드 (왜? 노드를 삭제하려면 부모 노드에서 연결을 끊고, 새로운 노드도 부모 노드에 연결해야기 떄문 )
  def delete(self, value):
    if self.isEmpty():
      return "ERROR : Empty Tree"
    
    current = self.root
    parent = self.root
    hasValue = False

  # 우선 값이 있는 지부터 확인한다. 
    while current:
      if value == current.value:
        hasValue = True
        break
      elif value < current.value:
        parent = current
        current = current.left
      elif value > current.value:
        parent = current
        current = current.right
    
    if not hasValue:
      return "ERROR : Value Not Found"

    # 1. 삭제하려는 노드가 부모 노드보다 작은경우
    if  current.value < parent.value:
      # 1-1. 리프 노드인 경우
      if not current.left and not current.right:
        parent.left = None
        del current
        self.size -= 1
        print(f"delete: {value}")

        return 
      # 1-2-1. 왼쪽 자식만 가지는 경우
      if current.left and not current.right:
        parent.left = current.left
        del current
        self.size -= 1
        print(f'delete: {value}')
        
        return 
      # 1-2-2. 오른쪽 자식만 가지는 경우
      if not current.left and current.right:
        parent.left = current.right
        del current
        self.size -= 1
        print(f'delete: {value}')

        return 
      # 1-3. 자식 노드가 두 개인 경우
      if current.left and current.right:
        # 현재 노드의 오른쪽 branch에서 가장 작은 값을 가진 노드를 끌어 올려질 노드로 설정
        hoisted_node = current.right
        hoisted_node_parent = current.right

        while hoisted_node.left:
          hoisted_node_parent = hoisted_node
          hoisted_node = hoisted_node.left

        # 말단 노드 찾았으면, 해당 노드의 오른쪽 여부에 따라서 자신의 자리를 대체하거나 비우고
        if hoisted_node.right:
          hoisted_node_parent.left = hoisted_node.right
        else:
          hoisted_node_parent.left = None
        
        # 삭제하는 노드의 부모의 왼쪽으로 삽입된다 
        parent.left = hoisted_node
        hoisted_node.left = current.left
        hoisted_node.right = current.right
        
        del current
        sief.size -= 1
        print(f'delete: {value}')

        return

    #2. 삭제하려는 노드의 값이 부모 노드보다 큰경우
    if current.value > parent.value:
      # 2-1. 리프
      if not current.left and not current.right: 
        parent.right = None
        del current
        self.size -= 1
        print(f"delete: {value}")

        return 
      # 2-2-1. 왼쪽만 가짐
      if current.left and not current.right:
        parent.right = current.left
        del current
        self.size -= 1
        print(f'delete: {value}')

        return
      # 2-2-2. 오른쪽만 가짐
      if not current.left and current.right:
        parent.right = current.right
        del current
        self.size -= 1
        print (f'delete: {value}')
        
        return 
      # 2-3. 둘 다 가짐
      if current.left and current.right:
        # 현재 노드의 오른쪽 branch에서 가장 작은 값을 가진 노드를 끌어 올려질 노드로 설정
        hoisted_node = current.right
        hoisted_node_parent = current.right

        while hoisted_node.left:
          hoisted_node_parent = hoisted_node
          hoisted_node = hoisted_node.left

        # 말단 노드 찾았으면, 해당 노드의 오른쪽 노드 존재 여부에 따라서 자신의 자리를 대체하거나 비우고
        if hoisted_node.right:
          hoisted_node_parent.left = hoisted_node.right
        else:
          hoisted_node_parent.left = None
        
        # 삭제하는 노드의 부모의 왼쪽으로 삽입된다 
        parent.right = hoisted_node
        hoisted_node.left = current.left
        hoisted_node.right = current.right
        
        del current
        self.size -= 1
        print(f'delete: {value}')

        return


  # 트리 사이즈, 전체 노드 요약
  def summary(self):
    return f'size: {self.size}'



# test code 
bst = BST()

# generate a set of randomly chosen numbers to create binary search tree
insert_set = set()
while len(insert_set) != 100:
  insert_set.add(random.randint(0,300))

# insert randomly generated numbers in binary search tree
for number in insert_set:
  bst.insert(number)
  print(bst.root.value)

# print out the tree's size
print(bst.summary())

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
print(bst.summary())
# print(bst.root.value)
# print(bst.root.left.value)
# print(bst.root.right.value)
# print(bst.root.left.left)
# print(bst.root.left.right.value)