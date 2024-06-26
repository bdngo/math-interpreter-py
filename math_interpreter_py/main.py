"""Wrapper for interpreter."""

import argparse

from math_interpreter_py.interpreter.interpreter import Interpreter, postfix_eval
from math_interpreter_py.interpreter.lexer import Lexer
from math_interpreter_py.interpreter.parser import Parser, shunting_yard


def main() -> None:
    """Drive the interpreter."""
    parser = argparse.ArgumentParser(
        description="tokenize, parse, interpret math expressions"
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--postfix",
        help="evaluate postfix instead of infix expressions",
        action="store_true",
    )
    group.add_argument(
        "-b",
        "--backend",
        type=str,
        choices=("recursive", "shunting"),
        default="recursive",
        help="backend for parsing infix expressions",
    )

    parser.add_argument(
        "-t", "--tokens", help="print tokens from the lexer", action="store_true"
    )
    parser.add_argument(
        "-a",
        "--ast",
        help="print the AST or transformed tokens from the parser (infix only)",
        action="store_true",
    )

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
                print(postfix_eval(tokens))
            else:
                val = infix_shell(tokens, print_ast=args.ast, backend=args.backend)
                if val is None:
                    continue
                print(val)
        except Exception as e:
            print(e)


def infix_shell(tokens, print_ast=False, backend="recursive", json=False) -> float:
    if backend == "recursive":
        parser = Parser(tokens)
        ast = parser.parse()

        if ast is None:
            return None

        if print_ast:
            print(ast)

        interpreter = Interpreter(ast)
        return interpreter.eval()
    elif backend == "shunting":
        pf_tokens = shunting_yard(tokens)
        if print_ast:
            print(pf_tokens)
        return postfix_eval(pf_tokens)


if __name__ == "__main__":
    main()
