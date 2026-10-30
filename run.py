from models.gate import Gate, OR, AND, NOT, XOR
import cli.lexer as lex

def main() -> int:
    result : lex.LexResult = lex.lex("add --type AND --x 10")

    print (f"error code: {result.error_code}")

    if result.error_code != lex.ErrorCode.SUCCESS:
        return 1

    print (f"command name: {result.command_name}")

    for key, value in result.opt_to_args.items():
        print(f"{key} : {value}")

    return 0

if __name__ == "__main__":
    main()
