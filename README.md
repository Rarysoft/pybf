# BF

A [brainfuck](https://esolangs.org/wiki/Brainfuck) interpreter library.

## History

This was originally written in Java (https://github.com/Rarysoft/bf). It was then ported to Go
(https://github.com/Rarysoft/bf-go), and then to Python.

## Usage

To execute brainfuck code, create an instance of `BF` and pass the code as a `str` into the instance's `run` method.
An instance of `BF` requires an `Executor` and a `Looper`. The standard implementations are the `BFExecutor` and
`BFLooper` classes. To instantiate a `BFExecutor`, implementations of the `Input`, `Output`, and `Memory` interfaces
are required.

### Input

Four `Input` implementations are provided. First is the `NullInput`, which immediately returns a `null` input (`0x00`)
whenever input is read. Next is `StringInput`, which reads from a provided `str`. Then is `FileInput`, which reads
from a file. Also included is `Pipe`, which is both an `Input` implementation and an `Output` implementation. It pipes
the output from one program into the input of another.

### Output

Four `Output` implementation are provided. First is `NullOutput`, which does nothing with the output. Next is
`ConsoleOutput`, which prints directly to the system console. Then is `FileOutput`, which writes to a file. Also
included is `Pipe`, described previously.

### Memory

There is one abstract base `Memory` class for extension, and four concrete implementations of that base class. The
concrete implementations are `Unsigned8BitMemory`, `Unsigned16BitMemory`, `Signed8BitMemory`, and `Signed16BitMemory`.
The `Unsigned8BitMemory` and `Unsigned16BitMemory` classes provide memory that store unsigned 8-bit (0 to 255) or
16-bit (0 to 65,535) memory values, while the `Signed8BitMemory` and `Signed16BitMemory` classes provide memory that
store signed 8-bit (-127 to 128) or 16-bit (-32,768 to 32,767) memory values. Both of the 8-bit memory classes have a
capacity of 30,000 memory cells, while the two 16-bit memory classes provide 65,536 memory cells.

The `Memory` abstract class can be extended to implement any other sized unsigned or signed memory implementations. The
constructor accepts minimum and maximum addresses, and minimum and maximum values. However, the `Memory` interface
requires addresses and values to be Java `int` types, which effectively limits the possible range of addresses and
values to always be within the range of signed 32-bit integers (-2,147,483,648 to 2,147,483,647). It is therefore
impossible to create a `Memory` implementation that goes beyond that range, such as an unsigned 32-bit integer memory
implementation or any kind of floating-point memory. This is an intentional limitation. This is brainfuck after all.
It's not meant to be practical.

### Example

Most users of the `BFExecutor` will use one of the `Memory` implementations and provide their own `Input` and `Output`
implementations. Non-interactive programs can use the `NullInput` implementation, and simply provide an `Output`
implementation, unless console output is sufficient.

```python
from bf import BF
from executor import BFExecutor
from input import NullInput
from output import ConsoleOutput
from memory import Unsigned16BitMemory

inp = NullInput()
out = ConsoleOutput()
mem = Unsigned16BitMemory()

exe = BFExecutor(inp, out, mem)
bf = BF(exe)

bf.run("++-->><<[,.]")
```

## Exceptions

The standard exception raised by `BF` is the `STB` ("shit the bed") exception. This will be raised if invalid BF code
is found by the interpreter. Although the provided `Memory` implementations will raise an `STB` on any attempt to
reference addresses or values outside the valid range, it should be impossible for valid BF code to result in an `STB`,
as the interpreter implements a number of common brainfuck safeguards, such as wrapping the memory pointer and values
on overflow and underflow.
