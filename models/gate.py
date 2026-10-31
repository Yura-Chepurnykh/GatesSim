from abc import ABC, abstractmethod
from typing import Self
from enum import Enum
import uuid
import cli.parse as parser

class GateType(Enum):
    AND_GATE_TYPE    = 0
    NAND_GATE_TYPE   = 1
    OR_GATE_TYPE     = 2
    NOR_GATE_TYPE    = 3
    XOR_GATE_TYPE    = 4
    NXOR_GATE_TYPE   = 5
    NOT_GATE_TYPE    = 6
    BUFFER_GATE_TYPE = 7

class Component(ABC):
    def __init__(
        self,
        name : str,
        top_x : int,
        top_y : int,
        rotation : parser.TokenType
    ) -> None:
        self.id = uuid.uuid4()
        self.name = name
        self.top_x = top_x
        self.top_y = top_y
        self.rotation = rotation

class ComponentsGroup(Component):
    def __init__(
        self,
        name : str,
        top_x : int,
        top_y : int,
        rotation : parser.TokenType
    ) -> None:
        super().__init__(name, top_x, top_y, rotation)
        self.id = uuid.uuid4()

class Gate(Component):
    def __init__(
        self,
        name : str,
        top_x : int,
        top_y : int,
        rotation : parser.TokenType,
        inputs : list[bool]
    ) -> None:
        super().__init__(name, top_x, top_y, rotation)
        self.inputs = inputs
        self.id = uuid.uuid4()

    @abstractmethod
    def calc_output(self) -> bool:
        pass

class AND(Gate):
    def __init__(
        self,
        name : str,
        top_x : int,
        top_y : int,
        rotation : parser.TokenType,
        inputs : list[bool]
    ):
        super().__init__(name, top_x, top_y, rotation, inputs)
        self.id = uuid.uuid4()

    def calc_output(self) -> bool:
        output : bool = True
        for input in self.inputs:
            output = output and input
        return output

class OR(Gate):
    def __init__(
        self,
        name : str,
        top_x : int,
        top_y : int,
        rotation : parser.TokenType,
        inputs : list[bool]
    ):
        super().__init__(name, top_x, top_y, rotation, inputs)
        self.id = uuid.uuid4()

    def calc_output(self) -> bool:
        output : bool = False
        for input in self.inputs:
            output = output or input
        return output

class XOR(Gate):
    def __init__(
        self,
        name : str,
        top_x : int,
        top_y : int,
        rotation : parser.TokenType,
        inputs : list[bool]
    ):
        super().__init__(name, top_x, top_y, rotation, inputs)
        self.id = uuid.uuid4()

    def calc_output(self) -> bool:
        output : bool = self.inputs[0]

        for i in range(1, len(self.inputs)):
            output = output ^ self.inputs[i]

        return output

class NOT(Gate):
    def __init__(
        self,
        name : str,
        top_x : int,
        top_y : int,
        rotation : parser.TokenType,
        inputs : list[bool]
    ):
        super().__init__(name, top_x, top_y, rotation, inputs)
        self.id = uuid.uuid4()

    def calc_output(self) -> bool:
        return not self.inputs[0]

class Buffer(Gate):
    def __init__(
        self,
        name : str,
        top_x : int,
        top_y : int,
        rotation : parser.TokenType,
        inputs : list[bool]
    ):
        super().__init__(name, top_x, top_y, rotation, inputs)
        self.id = uuid.uuid4()

    def calc_output(self) -> bool:
        return self.inputs[0]

# decorator class
class NOTDecorator(Gate):
    def __init__(self, gate : Gate, name = ""):
        self.gate : Gate = gate
        self.id = uuid.uuid4()
        self.name = name

    def calc_output(self) -> bool:
        return not self.gate.calc_output()
