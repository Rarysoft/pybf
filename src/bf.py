from dialect import INCREMENT, DECREMENT, INCREMENT_POINTER, DECREMENT_POINTER, START_LOOP, END_LOOP, INPUT, OUTPUT
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
    if token == INCREMENT:
      self.executor.perform_increment()
    elif token == DECREMENT:
      self.executor.perform_decrement()
    elif token == INCREMENT_POINTER:
      self.executor.perform_increment_pointer()
    elif token == DECREMENT_POINTER:
      self.executor.perform_decrement_pointer()
    elif token == START_LOOP:
      if self.executor.perform_start_loop():
        return self.looper.find_end_of_loop_delta(code, position)
    elif token == END_LOOP:
      if self.executor.perform_end_loop():
        return self.looper.find_start_of_loop_delta(code, position)
    elif token == INPUT:
      self.executor.perform_input()
    elif token == OUTPUT:
      self.executor.perform_output()
    return 1
