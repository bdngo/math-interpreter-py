from nodes import *
from tokens import Token, TokenType

class Interpreter:

    def __init__(self, ast):
        self.ast = ast

    def eval(self):
        return self.evalHelper(self.ast)

    def evalHelper(self, ast):
        if isinstance(ast, NumberNode):
            return ast.node
        elif isinstance(ast, AddNode):
            return self.evalHelper(ast.node_a) + self.evalHelper(ast.node_b)
        elif isinstance(ast, SubtractNode):
            return self.evalHelper(ast.node_a) - self.evalHelper(ast.node_b)
        elif isinstance(ast, MultiplyNode):
            return self.evalHelper(ast.node_a) * self.evalHelper(ast.node_b)
        elif isinstance(ast, DivideNode):
            eval_b = self.evalHelper(ast.node_b)
            if eval_b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return self.evalHelper(ast.node_a) / eval_b
        elif isinstance(ast, PositiveNode):
            return self.evalHelper(ast.node)
        elif isinstance(ast, NegativeNode):
            return -self.evalHelper(ast.node)

def postfix_eval(tokens):
    stack = []
    for t in tokens:
        if t.type == TokenType.PLUS:
            a = stack.pop().value
            b = stack.pop().value
            stack.append(Token(TokenType.NUMBER, a + b))
        elif t.type == TokenType.MINUS:
            a = stack.pop().value
            b = stack.pop().value
            stack.append(Token(TokenType.NUMBER, b - a))
        elif t.type == TokenType.MULTIPLY:
            a = stack.pop().value
            b = stack.pop().value
            stack.append(Token(TokenType.NUMBER, a * b))
        elif t.type == TokenType.DIVIDE:
            a = stack.pop().value
            b = stack.pop().value
            stack.append(Token(TokenType.NUMBER, a / b))
        else:
            stack.append(t)
    return stack[0].value
