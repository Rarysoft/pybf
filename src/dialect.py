from __future__ import annotations
from abc import ABC


class Dialect(ABC):
  def __init__(self, increment, decrement, increment_pointer, decrement_pointer, start_loop, end_loop, input, output):
    self.increment = increment
    self.decrement = decrement
    self.increment_pointer = increment_pointer
    self.decrement_pointer = decrement_pointer
    self.start_loop = start_loop
    self.end_loop = end_loop
    self.input = input
    self.output = output


class BFDialect(Dialect):
  def __init__(self):
    super().__init__("+", "-", ">", "<", "[", "]", ",", ".")


current_dialect = BFDialect()
