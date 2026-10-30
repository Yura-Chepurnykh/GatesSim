from enum import Enum

class ErrorCode(Enum):
    SUCCESS = 0
    UNKNOWN_COMMAND = 1
    UNKNOWN_OPTION = 2
    MISSED_ARGUMENT = 3

class LexResult:
    def __init__(
        self,
        error_code : ErrorCode,
        command_name : str = "",
        opt_to_args : dict[str, str] = {}
    ):
        self.error_code = error_code
        self.command_name = command_name
        self.opt_to_args = opt_to_args

def lex(input : str) -> LexResult:
    commands : list[str] = ["add", "remove", "change", "read", "group", "ungroup", "redo", "undo"]
    options : list[str] = ["x", "y", "rotation", "dx", "dy", "drotation", "name", "type"]

    toks : list[str] = input.split()

    command : str = ""

    for cmd in commands:
        if toks[0] == cmd:
            command = cmd

    if not command:
        print(f"Error: Unknown command. Use the commands from the list <{[cmd for cmd in commands]}>")
        return LexResult(ErrorCode.UNKNOWN_COMMAND)

    opt_to_args : dict[str, str] = {}

    for i in range(1, len(toks), 2):
        expanded_tok : str = toks[i][2:]
        option = ""
        for opt in options:
            if expanded_tok == opt:
                option = opt

        if not option:
            print(f"Error: Unknown option. Use the options from the list <{[cmd for cmd in commands]}>")
            return LexResult(ErrorCode.UNKNOWN_OPTION)

        argument : str = ""

        if toks[i + 1][:1] == "--":
            print(f"Error: Missed argument. <{toks[i + 1]}> is option")
            return LexResult(ErrorCode.MISSED_ARGUMENT)
        else:
            argument = toks[i + 1]

        opt_to_args[option] = argument

    return LexResult(ErrorCode.SUCCESS, command, opt_to_args)
