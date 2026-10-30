from abc import ABC, abstractmethod
from typing import Self

class Gate(ABC):
    def __init__(self, inputs : list[bool]) -> None:
        self.inputs = inputs

    @abstractmethod
    def calc_output(self) -> bool:
        pass

class AND(Gate):
    def __init__(self, inputs : list[bool]):
        super().__init__(inputs)

    def calc_output(self) -> bool:
        output : bool = True
        for input in self.inputs:
            output = output and input
        return output

class OR(Gate):
    def __init__(self, inputs : list[bool]):
        super().__init__(inputs)

    def calc_output(self) -> bool:
        output : bool = False
        for input in self.inputs:
            output = output or input
        return output

class XOR(Gate):
    def __init__(self, inputs : list[bool]):
        super().__init__(inputs)

    def calc_output(self) -> bool:
        output : bool = self.inputs[0]

        for i in range(1, len(self.inputs)):
            output = output ^ self.inputs[i]

        return output

# decorator class
class NOT(Gate):
    def __init__(self, gate : Gate):
        self.gate : Gate = gate
        super().__init__(gate.inputs)

    def calc_output(self) -> bool:
        return not self.gate.calc_output()
