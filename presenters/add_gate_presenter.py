import models.gate as gate_module
import models.workspace as workspace
import cli.parse as parser

def create_gate(
    gate_type : gate_module.GateType,
    name : str,
    top_x : int,
    top_y : int,
    rotation : parser.TokenType,
    inputs : list[bool]
) -> gate_module.Gate:

    if gate_type == gate_module.GateType.AND_GATE_TYPE:
        return gate_module.AND(name, top_x, top_y, rotation, inputs)

    elif gate_type == gate_module.GateType.NAND_GATE_TYPE:
        and_gate = gate_module.AND(name, top_x, top_y, rotation, inputs)
        return gate_module.NOTDecorator(and_gate)

    elif gate_type == gate_module.GateType.OR_GATE_TYPE:
        return gate_module.OR(name, top_x, top_y, rotation, inputs)

    elif gate_type == gate_module.GateType.NOR_GATE_TYPE:
        or_gate = gate_module.OR(name, top_x, top_y, rotation, inputs)
        return gate_module.NOTDecorator(or_gate)

    elif gate_type == gate_module.GateType.XOR_GATE_TYPE:
        return gate_module.XOR(name, top_x, top_y, rotation, inputs)

    elif gate_type == gate_module.GateType.NXOR_GATE_TYPE:
        xor_gate = gate_module.OR(name, top_x, top_y, rotation, inputs)
        return gate_module.NOTDecorator(xor_gate)

    elif gate_type == gate_module.GateType.NOT_GATE_TYPE:
        if len(inputs) != 1:
            raise ValueError("Error: NOT gate muse have one input")
        return gate_module.NOT(name, top_x, top_y, rotation, inputs)

    elif gate_type == gate_module.GateType.BUFFER_GATE_TYPE:
        return gate_module.Buffer(name, top_x, top_y, rotation, inputs)

class AddGateAction:
    def __init__(
        self,
        gate_type : gate_module.GateType,
        name : str,
        top_x : int,
        top_y : int,
        rotation : parser.TokenType,
        inputs : list[bool],
        workspace : workspace.Workspace
    ) -> None:
        self.gate_type = gate_type
        self.gate_name = name
        self.top_x = top_x
        self.top_y = top_y
        self.rotation = rotation
        self.inputs = inputs
        self.workspace = workspace

    def action(self) -> None:
        gate : gate_module.Gate = create_gate(
            self.gate_type,
            self.gate_name,
            self.top_x,
            self.top_y,
            self.rotation,
            self.inputs
        )

        self.workspace.add(gate)

class RemoveGateAction:
    def __init__(self, gate_name : str, workspace : workspace.Workspace) -> None:
        self.gate_name = gate_name
        self.workspace = workspace

    def action(self) -> None:
        self.workspace.remove(self.gate_name)

class AddGateCommand:
    def __init__(self, action_obj : AddGateAction, undo_obj : RemoveGateAction) -> None:
        self.action_obj = action_obj
        self.undo_obj = undo_obj

    def action(self) -> None:
        self.action_obj.action()

    def undo(self) -> None:
        self.undo_obj.action()

class RemoveGateCommand:
    def __init__(self, action_obj : RemoveGateAction, undo_obj : AddGateAction) -> None:
        self.action_obj = action_obj
        self.undo_obj = undo_obj

    def action(self) -> None:
        self.action_obj.action()

    def undo(self) -> None:
        self.undo_obj.action()
