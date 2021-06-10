import argparse

from interpreter import Interpreter, postfix_eval
from parser_ import Parser
from lexer import Lexer


def main():
    parser = argparse.ArgumentParser(description="tokenize, parse, interpret math expressions")
    parser.add_argument("--postfix", help="evaluate postfix instead of infix expressions", action="store_true")
    parser.add_argument("-t", "--tokens", help="print tokens from the lexer", action="store_true")
    parser.add_argument("-a", "--ast", help="print the AST from the parser (infix only)", action="store_true")
    args = parser.parse_args()
    while True:
        try:
            txt = input("calc > ")
            lexer = Lexer(txt)
            tokens = lexer.generate_tokens()
            if args.tokens:
                token_lst = list(tokens)
                print(token_lst)
                tokens = iter(token_lst)
            if args.postfix:
                print(postfix_shell(tokens))
            else:
                val = infix_shell(tokens, args.ast)
                if val == None:
                    continue
                print(val)
        except Exception as e:
            print(e)

def postfix_shell(tokens):
    return postfix_eval(tokens)

def infix_shell(tokens, print_ast=False):
    parser = Parser(tokens)
    ast = parser.parse()

    if ast == None:
        return None

    if print_ast:
        print(ast)
    interpreter = Interpreter(ast)
    result = interpreter.eval()
    return result


if __name__ == "__main__":
    main()
