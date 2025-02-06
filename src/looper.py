from abc import ABC, abstractmethod
from dialect import current_dialect
from stb import STB


class Looper(ABC):
  @abstractmethod
  def find_end_of_loop_delta(self, code: str, position: int) -> int:
    pass
  
  @abstractmethod
  def find_start_of_loop_delta(self, code: str, position: int) -> int:
    pass


class BFLooper(Looper):
  def find_start_of_loop_delta(self, code: str, position: int):
    BFLooper.__validate_args(code, position)
    done = False
    delta = 0
    loop_count = 1
    while not done:
      delta -= 1
      if position + delta < 0:
        raise STB("Loop has no start")
      token = code[position + delta]
      if token == current_dialect.start_loop:
        loop_count -= 1
        if loop_count == 0:
          done = True
          continue
      if token == current_dialect.end_loop:
        loop_count += 1
    return delta
  
  def find_end_of_loop_delta(self, code: str, position: int):
    BFLooper.__validate_args(code, position)
    done = False
    delta = 0
    loop_count = 1
    while not done:
      delta += 1
      if position + delta == len(code):
        raise STB("Loop has no end")
      token = code[position + delta]
      if token == current_dialect.end_loop:
        loop_count -= 1
        if loop_count == 0:
          done = True
          continue
      if token == current_dialect.start_loop:
        loop_count += 1
    return delta
  
  @staticmethod
  def __validate_args(code, position):
    if not code:
      raise STB("Code is missing")
    if position < 0:
      raise STB("Position before start of code")
    if position >= len(code):
      raise STB("Position after end of code")
