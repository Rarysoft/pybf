from stb import STB


class Memory(object):
  def __init__(self, min_address, max_address, min_value, max_value):
    self.min_address = min_address
    self.max_address = max_address
    self.min_value = min_value
    self.max_value = max_value
    self.bytes = {}
  
  def read(self, address):
    if address > self.max_address or address < self.min_address:
      raise STB("Address out of range")
    return self.bytes[address]
  
  def write(self, address, value):
    if address > self.max_address or address < self.min_address:
      raise STB("Address out of range")
    if value > self.max_value or value < self.min_value:
      raise STB("Value out of range")
    self.bytes[address] = value


class Signed8BitMemory(Memory):
  def __init__(self):
    super().__init__(0x0000, 0x752F, -0x80, 0x7F)


class Signed16BitMemory(Memory):
  def __init__(self):
    super().__init__(0x0000, 0xFFFF, -0x8000, 0x7FFF)


class Unsigned8BitMemory(Memory):
  def __init__(self):
    super().__init__(0x0000, 0x752F, 0x00, 0xFF)


class Unsigned16BitMemory(Memory):
  def __init__(self):
    super().__init__(0x0000, 0xFFFF, 0x0000, 0xFFFF)
