import random

# class Node(object):
#   def __init__(self, value = None):
#     self.value = value
#     self.leftChild = None
#     self.rightChild = None

class Heap(object):
  def __init__(self):
    self.heap = [None]

  def is_move_up(self,current_index,parent_index):
    if current_index <= 1:
      return False

    if self.heap[current_index] > self.heap[parent_index]:
      return True
    else :
      return False 
    
  def insert(self, value):
    self.heap.append(value)
    
    current_index = len(self.heap) - 1
    parent_index = current_index // 2

    while self.is_move_up(current_index, parent_index):

      if self.heap[current_index] > self.heap[parent_index]:
        self.swap(current_index,parent_index)
        current_index = parent_index
        parent_index = current_index // 2
      else:
        break

  def is_move_down(self, current_index):
    left_child_index = current_index * 2
    right_child_index = current_index * 2 + 1
    print(len(self.heap), left_child_index)
    print(len(self.heap), right_child_index)
    if left_child_index >= len(self.heap):
      return False
    elif right_child_index >= len(self.heap) :
      if self.heap[left_child_index] > self.heap[current_index]:
        return True
      else:
        return False
    else :
      if self.heap[left_child_index] > self.heap[right_child_index]:
        if self.heap[left_child_index] > self.heap[current_index]:
          return True
        else:
          return False
      else :
        if self.heap[right_child_index] > self.heap[current_index]:
          return True
        else:
          return False   

  def pop(self):
    if len(self.heap) < 1 :
      return None

    returned_data = self.heap[1]
    self.heap[1] = self.heap[-1]
    del self.heap[-1]
    current_index = 1

    while self.is_move_down(current_index):
      left_child_index = current_index * 2
      right_child_index = current_index * 2 + 1
    
      if right_child_index >= len(self.heap) :
        if self.heap[left_child_index] > self.heap[current_index]:
          self.swap(left_child_index,current_index)
          current_index = left_child_index

      else :
        if self.heap[left_child_index] > self.heap[right_child_index]:
          if self.heap[left_child_index] > self.heap[current_index]:
            self.swap(left_child_index, current_index)
            current_index = left_child_index
        else :
          if self.heap[right_child_index] > self.heap[current_index]:
            self.swap(right_child_index, current_index)
            current_index = right_child_index

    return returned_data

  def swap(self, current, parent):
    self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]

  def print_heap(self):
    for value in self.heap:
      print(value,end=" ")
    print()


heap = Heap()
random_set = set({ random.randint(1,500) for i in range(15) })
   
for i in random_set:
  heap.insert(i)
heap.print_heap()

for i in range(len(heap.heap)-1):
  print(heap.pop())
  heap.print_heap()
