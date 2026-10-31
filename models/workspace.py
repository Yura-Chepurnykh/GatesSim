from uuid import UUID, uuid4
import models.gate as gate_module

# height and length in pixels
class Workspace:
    def __init__(self, height : int, length : int) -> None:
        self.height = height
        self.length = length
        self.name_to_component : dict[str, gate_module.Component] = {}
        self.components : list[gate_module.Component] = []

    def add(self, g : gate_module.Component) -> None:
        print(f"add gate: {g.name}")
        self.name_to_component[g.name] = g
        self.components.append(g)

    def remove(self, name : str) -> None:
        print(f"remove gate: {name}")
        target_gate : gate_module.Component = self.name_to_component[name]
        self.components.remove(target_gate)
