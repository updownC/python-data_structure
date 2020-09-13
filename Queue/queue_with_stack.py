class Stack(object):
  def __init__(self):
    self.in_stack = []
    self.out_stack = []

  def _transfer(self):
    while self.in_stack:
      self.out_stack.append(self.in_stack.pop())

  def enqueue(self,item):
    self.in_stack.append(item)
    print(f"Now :{self.in_stack}")

  def dequeue(self):
    if not out_stack:
      self._transfer()
    if out_stack:
      item = self.out_stack.pop()
      print(f"Now :{}")
    else :
      return "Stack is Empty"