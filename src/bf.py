from dialect import current_dialect
from executor import Executor
from looper import Looper
from stb import STB


class BF:
  def __init__(self, executor: Executor, looper: Looper):
    self.executor = executor
    self.looper = looper
  
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
        return self.looper.find_end_of_loop_delta(code, position)
    elif token == current_dialect.end_loop:
      if self.executor.perform_end_loop():
        return self.looper.find_start_of_loop_delta(code, position)
    elif token == current_dialect.input:
      self.executor.perform_input()
    elif token == current_dialect.output:
      self.executor.perform_output()
    return 1
