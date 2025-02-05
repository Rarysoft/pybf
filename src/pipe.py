from input import Input
from output import Output
from stb import STB


class Pipe(Input, Output):
  def __init__(self, skip_header = False):
    self.header_read = skip_header
    self.data = []
  
  def read(self):
    if not self.header_read:
      self.header_read = True
      return len(self.data)
    if len(self.data) == 0:
      raise STB("Illegal read operation")
    return self.data.pop(0)
  
  def write(self, value: int):
    self.data.append(value)
