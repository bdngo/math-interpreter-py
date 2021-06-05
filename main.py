from parser_ import Parser
from lexer import Lexer

while True:
    txt = input("calc > ")
    lexer = Lexer(txt)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    ast = parser.parse()
    print(ast)