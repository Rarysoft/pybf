import os.path

from stb import STB


class NullInput:
  def read(self):
    return 0


class StringInput:
  def __init__(self, data: str, skip_header = False):
    self.data = data
    self.header_read = skip_header
    self.index = 0
  
  
  def read(self):
    if not self.header_read:
      header_read = True
      return len(self.data)
    
    if self.index >= len(self.data):
      raise STB("Read past end of data")
    
    value = self.data[self.index]
    self.index += 1
    return value


class FileInput:
  def __init__(self, filename, skip_header = False):
    try:
      self.file = open(filename, "r")
    except FileNotFoundError as e:
      raise STB("File not found")
    self.length = os.path.getsize(filename)
    self.header_read = skip_header
  
  
  def read(self):
    if not self.header_read:
      self.header_read = True
      return self.length
    
    try:
      value = self.file.read(1)
      if value < 0:
        raise STB("Read past end of file")
      return value
    except:
      raise STB("Unrecoverable file read error")


class NullOutput:
  def write(self, value):
    pass


class ConsoleOutput:
  def write(self, value):
    print(value)


class FileOutput:
  def __init__(self, filename, append = False):
    try:
      self.file = open(filename, "a" if append else "w")
    except FileNotFoundError as e:
      raise STB(e)
  
  
  def write(self, value):
    try:
      self.file.write(value)
    except FileNotFoundError:
      raise STB("Unrecoverable file write error")


