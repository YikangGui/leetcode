import time
from myque import myque


class elevator:
  def __init__(self,layers):
    self.building_layers = layers
    self.direction = 'up'
    self.cur_layer = 1
    self.up_queue = myque()
    self.down_queue = myque(True)
    self.switcher = 'open'
  def stop(self):
    self.switcher='stop'
  def push_button(self,layer,direction=None):
    if self.cur_layer>layer:
      self.down_queue.insert(layer)
    elif self.cur_layer<layer:
      self.up_queue.insert(layer)
    else:
      if self.direction=='up':
        self.down_queue.insert(layer)
      else:
        self.up_queue.insert(layer)
  def handle_queue(self,direction):
    self.direction = direction
    if direction == 'up':
      inc = 1
    else:
      inc = -1
    que = getattr(self , direction + '_queue')
    while que.length():
      while self.cur_layer != que.front():
        print '/nelevator in ',self.cur_layer
        time.sleep(1)
        self.cur_layer += inc
      print '/nelevator arrives at ',self.cur_layer
      que.pop_front()
  def run(self):
    while self.switcher=='open':
      if self.up_queue.empty() and self.down_queue.empty():
        """elevator now is waiting, stop at a layer"""
        time.sleep(1)
        continue
      """go up"""
      self.handle_queue('up')
      """go down"""
      self.handle_queue('down')