from abc import ABC, abstractmethod
from stb import STB


class Output(ABC):
  @abstractmethod
  def write(self, value):
    pass


class NullOutput(Output):
  def write(self, value):
    pass


class ConsoleOutput(Output):
  def write(self, value):
    print(chr(value), end="")


class FileOutput(Output):
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
