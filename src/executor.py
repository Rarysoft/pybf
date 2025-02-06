from abc import ABC, abstractmethod

from input import Input
from memory import Memory
from output import Output


class Executor(ABC):
  @abstractmethod
  def perform_increment(self):
    pass
  
  @abstractmethod
  def perform_decrement(self):
    pass
  
  @abstractmethod
  def perform_increment_pointer(self):
    pass
  
  @abstractmethod
  def perform_decrement_pointer(self):
    pass
  
  @abstractmethod
  def perform_start_loop(self) -> bool:
    pass
  
  @abstractmethod
  def perform_end_loop(self) -> bool:
    pass
  
  @abstractmethod
  def perform_input(self):
    pass
  
  @abstractmethod
  def perform_output(self):
    pass


class BFExecutor(Executor):
  def __init__(self, input: Input, output: Output, memory: Memory, pointer = 0):
    self.input = input
    self.output = output
    self.memory = memory
    self.pointer = pointer
  
  def perform_increment(self):
    current = self.memory.read(self.pointer)
    if current == self.memory.max_value:
      self.memory.write(self.pointer, self.memory.min_value)
      return
    self.memory.write(self.pointer, current + 1)
  
  def perform_decrement(self):
    current = self.memory.read(self.pointer)
    if current == self.memory.min_value:
      self.memory.write(self.pointer, self.memory.max_value)
      return
    self.memory.write(self.pointer, current - 1)
  
  def perform_increment_pointer(self):
    if self.pointer == self.memory.max_address:
      self.pointer = self.memory.min_address
      return
    self.pointer += 1
  
  def perform_decrement_pointer(self):
    if self.pointer == self.memory.min_address:
      self.pointer = self.memory.max_address
      return
    self.pointer -= 1
  
  def perform_start_loop(self):
    return self.memory.read(self.pointer) == 0
  
  def perform_end_loop(self):
    return self.memory.read(self.pointer) != 0
  
  def perform_input(self):
    self.memory.write(self.pointer, self.input.read())
  
  def perform_output(self):
    self.output.write(self.memory.read(self.pointer))
