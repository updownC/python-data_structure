# from queue import Queue, PriorityQueue

# # general queue
# que = Queue()

# que.put("HI")
# que.put("hello")
# que.put("world")

# print(que.qsize())
# print(que.get())

# # Priority Queue
# prior_q = PriorityQueue()

# prior_q.put((10,"hi"))
# prior_q.put((5,"hello"))
# prior_q.put((15,"world"))

# print(prior_q.get())
# print(prior_q.get())

class Queue(object):
  def __init__(self):
    self.queue = []
  
  def enqueue(self,item):
    self.queue.append(item)

  def dequeue(self):
    if len(self.queue) != 0:
      return self.queue.pop(0)
    else:
      return "Queue is Empty"

  def size(self):
    return len(self.queue)

queue = Queue()
queue.enqueue('hello')
queue.enqueue('world')
queue.enqueue('sangha')

print(queue.dequeue())
print(queue.size())

print(queue.dequeue())
print(queue.size())

print(queue.dequeue())
print(queue.size())

print(queue.dequeue())
print(queue.size())