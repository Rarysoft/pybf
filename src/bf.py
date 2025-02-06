from dialect import current_dialect
from executor import Executor
from stb import STB


class BF:
  def __init__(self, executor: Executor):
    self.executor = executor
  
  def run(self, code: str):
    if not code:
      raise STB("Code is missing")
    self.execute(code)
  
  def execute(self, code: str):
    position = 0
    while position < len(code):
      delta = self.perform(code, position)
      position += delta
  
  def perform(self, code: str, position: int):
    token = code[position]
    if token == current_dialect.increment:
      self.executor.perform_increment()
    elif token == current_dialect.decrement:
      self.executor.perform_decrement()
    elif token == current_dialect.increment_pointer:
      self.executor.perform_increment_pointer()
    elif token == current_dialect.decrement_pointer:
      self.executor.perform_decrement_pointer()
    elif token == current_dialect.start_loop:
      if self.executor.perform_start_loop():
        return self.__find_end_of_loop_delta(code, position)
    elif token == current_dialect.end_loop:
      if self.executor.perform_end_loop():
        return self.__find_start_of_loop_delta(code, position)
    elif token == current_dialect.input:
      self.executor.perform_input()
    elif token == current_dialect.output:
      self.executor.perform_output()
    return 1
  
  @staticmethod
  def __find_start_of_loop_delta(code: str, position: int):
    BF.__validate_args(code, position)
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
  
  @staticmethod
  def __find_end_of_loop_delta(code: str, position: int):
    BF.__validate_args(code, position)
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
