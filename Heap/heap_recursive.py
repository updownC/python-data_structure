import random

class Max_heap(object):
  def __init__(self):
    self.heap = [None]

  def bulid_max_heap(self, array):
    if len(array) < 1:
      print('Please check the array')
      return False
    
    self.heap = [None] + array[:]
    
    for i in range( len(self.heap) // 2, 0, -1 ):
      self.max_heapify(i)
    
  def insert(self, value):
    self.heap.append(value)
    current_index = len(self.heap) - 1

    while current_index > 1:
      parent_index = self.parent(current_index)

      if self.heap[current_index] > self.heap[parent_index]:
        self.swap(current_index, parent_index)
        current_index = parent_index
      else:
        break

  def pop(self):
    if len(self.heap) <= 1:
      print('Empty list')
      return 

    popped_data = self.heap[1]
    self.heap[1] = self.heap[-1]
    del self.heap[-1]
    
    self.max_heapify(1)

    return popped_data

  def max_heapify(self, start_index):
    largest_index = start_index
    left_child_index = self.leftChild(start_index)
    right_child_index = self.rightChild(start_index)

    if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest_index]:
      largest_index = left_child_index
    
    if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest_index]:
      largest_index = right_child_index
    
    if largest_index != start_index:
      self.swap(start_index, largest_index)
      self.max_heapify(largest_index)
      
      return
    

  def swap(self, current_index, parent_index):
    self.heap[current_index], self.heap[parent_index] = self.heap[parent_index], self.heap[current_index]
  
  def parent(self, current_index):
    return current_index // 2
  
  def leftChild(self, current_index):
    return current_index * 2
  
  def rightChild(self, current_index):
    return current_index * 2 + 1


maxHeap = Max_heap()

random_set = set()
while len(random_set) < 10 :
  random_set.add(random.randint(0,500))

# for num in random_set:
#   maxHeap.insert(num)

# print(maxHeap.heap)

# for _ in range(len(maxHeap.heap)):
#   maxHeap.pop()
#   print(maxHeap.heap[1:])

maxHeap.bulid_max_heap(list(random_set))

