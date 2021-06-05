from tokens import TokenType
from nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()

    def bad_syntax(self, msg="Bad syntax"):
        raise SyntaxError(msg)

    def advance(self):
        try:
            self.curr_token = next(self.tokens)
        except StopIteration:
            self.curr_token = None

    def parse(self):
        if self.curr_token == None:
            return None

        result = self.expr()

        if self.curr_token != None:
            self.bad_syntax()
        
        return result
        
    def expr(self):
        result = self.term()

        while self.curr_token != None and self.curr_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.curr_token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.term())
            elif self.curr_token.type == TokenType.MINUS:
                self.advance()
                result = SubtractNode(result, self.term())

        return result

    def term(self):
        result = self.factor()

        while self.curr_token != None and self.curr_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            if self.curr_token.type == TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result, self.factor())
            elif self.curr_token.type == TokenType.DIVIDE:
                self.advance()
                result = DivideNode(result, self.factor())

        return result

    def factor(self):
        token = self.curr_token

        if token.type == TokenType.L_PAREN:
            self.advance()
            result = self.expr()

            if self.curr_token.type != TokenType.R_PAREN:
                self.bad_syntax("Mismatched parentheses")

            self.advance()
            return result
        elif token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)
        elif token.type == TokenType.PLUS:
            self.advance()
            return PositiveNode(self.factor())
        elif token.type == TokenType.MINUS:
            self.advance()
            return NegativeNode(self.factor())

        self.bad_syntax()
