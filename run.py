from models.gate import Gate, OR, AND, NOTDecorator, XOR, GateType
import cli.parse as parsers
import views.views as views
import models.workspace as workspaces
import presenters.add_gate_presenter as add_gate_pres

def main() -> int:
    # result : parser.LexResult = parser.parse("add --type AND --x 10")

    # print (f"error code: {result.error_code}")

    # if result.error_code != parser.ErrorCode.SUCCESS:
    #     return 1

    # print (f"command name: {result.command_name}")

    # for key, value in result.opt_to_args.items():
    #     print(f"{key} : {value}")

    view = views.View()
    workspace = workspaces.Workspace(100, 200)
    parser = parsers.Parser()
    result = parser.parse(view.cmd)

    cmd_action = None
    cmd_undo = None
    cmd_obj = None

    if result.command_name == "add":
        x : int = -1
        y : int = -1
        rotation : parsers.TokenType = parsers.TokenType.UNKNOWN_TYPE
        name : str = ""
        inputs : list[bool] = []
        type : parsers.TokenType = parsers.TokenType.UNKNOWN_TYPE

        for key, val in result.opt_to_args.items():
            print(f"{key}, {val.value}")

            if key == "x":
                x = int(val.value)
            elif key == "y":
                y = int(val.value)
            elif key == "rotation":
                rotation = parsers.TokenType(val.value)
            elif key == "name":
                name = val.value
            elif key == "inputs":
                inputs[0] = bool(val.value)

        cmd_action = add_gate_pres.AddGateAction(GateType.AND_GATE_TYPE, name, x, y, rotation, inputs, workspace)
        cmd_undo = add_gate_pres.RemoveGateAction(name, workspace)
        cmd_obj = add_gate_pres.AddGateCommand(cmd_action, cmd_undo)

    if cmd_obj:
        cmd_obj.action()
        cmd_obj.undo()

    return 0

if __name__ == "__main__":
    main()
