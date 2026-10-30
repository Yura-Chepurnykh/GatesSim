from enum import Enum

class ErrorCode(Enum):
    SUCCESS = 0
    UNKNOWN_COMMAND = 1
    UNKNOWN_OPTION = 2
    MISSED_ARGUMENT = 3

class TokenType(Enum):
    INTEGER_TYPE = 0
    FLOAT_TYPE = 1
    STRING_TYPE = 2
    NORTH_TYPE = 3
    SOUTH_TYPE = 4
    EAST_TYPE = 5
    WEST_TYPE = 6
    UNKNOWN_TYPE = 7

class Token:
    def __init__(
        self,
        value : str = "",
        type : TokenType = TokenType.UNKNOWN_TYPE
    ):
        self.value = value
        self.type = type

class LexResult:
    def __init__(
        self,
        error_code : ErrorCode,
        command_name : str = "",
        opt_to_args : dict[str, Token] = {}
    ):
        self.error_code = error_code
        self.command_name = command_name
        self.opt_to_args = opt_to_args

def parse(input : str) -> LexResult:
    commands : list[str] = ["add", "remove", "change", "read", "group", "ungroup", "redo", "undo"]
    options : list[str] = ["x", "y", "rotation", "dx", "dy", "name", "type"]

    toks : list[str] = input.split()

    command : str = ""

    for cmd in commands:
        if toks[0] == cmd:
            command = cmd

    if not command:
        print(f"Error: Unknown command. Use the commands from the list <{[cmd for cmd in commands]}>")
        return LexResult(ErrorCode.UNKNOWN_COMMAND)

    opt_to_args : dict[str, Token] = {}

    for i in range(1, len(toks), 2):
        expanded_tok : str = toks[i][2:]
        option = ""
        for opt in options:
            if expanded_tok == opt:
                option = opt

        if not option:
            print(f"Error: Unknown option. Use the options from the list <{[cmd for cmd in commands]}>")
            return LexResult(ErrorCode.UNKNOWN_OPTION)

        argument_value : str = ""

        if toks[i + 1][:1] == "--":
            print(f"Error: Missed argument. <{toks[i + 1]}> is option")
            return LexResult(ErrorCode.MISSED_ARGUMENT)
        else:
            argument_value = toks[i + 1]

        token_type = TokenType.UNKNOWN_TYPE

        if isinstance(argument_value, int):
            token_type = TokenType.INTEGER_TYPE
        elif isinstance(argument_value, float):
            token_type = TokenType.FLOAT_TYPE
        elif isinstance(argument_value, str):
            token_type = TokenType.STRING_TYPE
        elif argument_value == "west":
            token_type = TokenType.WEST_TYPE
        elif argument_value == "east":
            token_type = TokenType.EAST_TYPE
        elif argument_value == "north":
            token_type = TokenType.NORTH_TYPE
        elif argument_value == "south":
            token_type = TokenType.SOUTH_TYPE
        else:
            token_type = TokenType.UNKNOWN_TYPE

        opt_to_args[option] = Token(argument_value, token_type)

    return LexResult(ErrorCode.SUCCESS, command, opt_to_args)
