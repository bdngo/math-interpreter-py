from nodes import *

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
