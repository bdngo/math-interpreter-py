import sys

from interpreter import Interpreter, postfix_eval
from parser_ import Parser
from lexer import Lexer


def main():
    while True:
        try:
            txt = input("calc > ")
            lexer = Lexer(txt)
            tokens = lexer.generate_tokens()
            if len(sys.argv) >= 2 and sys.argv[1] == "--postfix":
                print(postfix_shell(tokens))
            else:
                val = infix_shell(tokens)
                if val == None:
                    continue
                print(val)
        except Exception as e:
            print(e)

def postfix_shell(tokens):
    return postfix_eval(tokens)

def infix_shell(tokens):
    parser = Parser(tokens)
    ast = parser.parse()

    if ast == None:
        return None

    interpreter = Interpreter(ast)
    result = interpreter.eval()
    return result


if __name__ == "__main__":
    main()
