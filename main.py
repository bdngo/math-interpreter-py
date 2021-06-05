from lexer import Lexer

while True:
    txt = input("calc > ")
    lexer = Lexer(txt)
    tokens = lexer.generate_tokens()
    print(list(tokens))