from interpreter import Interpreter
from parser_ import Parser
from lexer import Lexer

while True:
    try:
        txt = input("calc > ")
        lexer = Lexer(txt)
        tokens = lexer.generate_tokens()

        parser = Parser(tokens)
        ast = parser.parse()

        interpreter = Interpreter(ast)
        result = interpreter.eval()
        print(result)
    except Exception as e:
        print(e)
