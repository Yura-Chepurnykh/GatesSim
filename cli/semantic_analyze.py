import parse as parser

class SemanticCheckResult:
    def __init__(self, error_code : parser.ErrorCode, error_message : str):
        self.error_code = error_code
        self.error_message = error_message

def check_name(token : parser.Token) -> SemanticCheckResult:
    if token.type != parser.TokenType.STRING_TYPE:
        return SemanticCheckResult(
            parser.ErrorCode.INCORRECT_NAME_TYPE,
            "Error: The name of the gate or gate group must be in <"">"
        )

    return SemanticCheckResult(parser.ErrorCode.SUCCESS, "Success: Everything is correct")
