from tokens import Token, TokenType
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
        result = self.exponent()

        while self.curr_token != None and self.curr_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.MODULO):
            if self.curr_token.type == TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result, self.exponent())
            elif self.curr_token.type == TokenType.DIVIDE:
                self.advance()
                result = DivideNode(result, self.exponent())
            elif self.curr_token.type == TokenType.MODULO:
                self.advance()
                result = ModuloNode(result, self.exponent())

        return result

    def exponent(self):
        result = self.factor()

        while self.curr_token != None and self.curr_token.type == TokenType.POWER:
            if self.curr_token.type == TokenType.POWER:
                self.advance()
                result = PowerNode(result, self.factor())

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

def shunting_yard(tokens):
    op_stack = []
    out_queue = []
    for t in tokens:
        if t.type == TokenType.NUMBER:
            out_queue.append(t)
        elif t.type in (TokenType.PLUS, TokenType.MINUS):
            while op_stack != [] and op_stack[-1].type in (TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.MODULO, TokenType.POWER):
                out_queue.append(op_stack.pop())
            op_stack.append(t)
        elif t.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            while op_stack != [] and op_stack[-1].type == TokenType.POWER:
                out_queue.append(op_stack.pop())
            op_stack.append(t)
        elif t.type == TokenType.POWER:
            op_stack.append(t)
        elif t.type == TokenType.L_PAREN:
            op_stack.append(t)
        elif t.type == TokenType.R_PAREN:
            while op_stack != [] and op_stack[-1].type != TokenType.L_PAREN:
                out_queue.append(op_stack.pop())
            op_stack.pop()
    return out_queue + list(reversed(op_stack))
