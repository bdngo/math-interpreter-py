from tokens import Token, TokenType

DIGITS = "0123456789"

class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.curr_char = next(self.text)
        except StopIteration:
            self.curr_char = None
    
    def generate_tokens(self):
        while self.curr_char != None:
            if self.curr_char.isspace():
                self.advance()
            elif self.curr_char == '.' or self.curr_char in DIGITS:
                yield self.generate_number()
            elif self.curr_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.curr_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.curr_char == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.curr_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.curr_char == '(':
                self.advance()
                yield Token(TokenType.L_PAREN)
            elif self.curr_char == ')':
                self.advance()
                yield Token(TokenType.R_PAREN)
            else:
                raise Exception(f"Illegal character: {self.curr_char}")

    def generate_number(self):
        dec_pts = 0
        num = self.curr_char
        self.advance()

        while self.curr_char != None and (self.curr_char == '.' or self.curr_char in DIGITS):
            if self.curr_char == '.':
                dec_pts += 1
                if dec_pts > 1:
                    break
            
            num += self.curr_char
            self.advance()
            
        if num.startswith('.'):
            num = '0' + num
        if num.endswith('.'):
            num += '0'

        return Token(TokenType.NUMBER, float(num))
