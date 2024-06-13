"""Defines class to ingest AST and interpret result."""

from operator import (
    add,
    sub,
    mul,
    truediv,
    mod,
    pow,
    pos,
    neg,
)

from .nodes import (
    BinaryOperation,
    BinaryNode,
    Node,
    NumberNode,
    UnaryOperation,
    UnaryNode,
)
from .tokens import NumberToken, Token, TokenType


BINARY_OPERATION_TO_FUNC = {
    BinaryOperation.ADD: add,
    BinaryOperation.SUBTRACT: sub,
    BinaryOperation.MULTIPLY: mul,
    BinaryOperation.DIVIDE: truediv,
    BinaryOperation.MODULO: mod,
    BinaryOperation.POWER: pow,
}
UNARY_OPERATION_TO_FUNC = {
    UnaryOperation.POSITIVE: pos,
    UnaryOperation.NEGATIVE: neg,
}


class Interpreter:
    """Class defining interpreter object."""

    def __init__(self, ast: Node):
        """Initialize interpreter with AST."""
        self.ast = ast

    def eval(self) -> float:
        """Interpret the AST."""
        return self.eval_helper(self.ast)

    def eval_helper(self, ast: Node):
        """Help evaluation function."""
        match ast.type:
            case NumberNode(n):
                return n
            case BinaryNode(op, node_l, node_r):
                return BINARY_OPERATION_TO_FUNC[op](
                    self.eval_helper(node_l), self.eval_helper(node_r)
                )
            case UnaryNode(op, node):
                return UNARY_OPERATION_TO_FUNC[op](self.eval_helper(node))


def postfix_eval(tokens) -> float:
    """Evaluate postfix expressions."""
    stack = []
    for t in tokens:
        match t.type:
            case TokenType.PLUS:
                a = stack.pop().value
                b = stack.pop().value
                stack.append(Token(NumberToken(a + b)))
            case TokenType.MINUS:
                a = stack.pop().value
                b = stack.pop().value
                stack.append(Token(NumberToken(b - a)))
            case TokenType.MULTIPLY:
                a = stack.pop().value
                b = stack.pop().value
                stack.append(Token(NumberToken(a * b)))
            case TokenType.DIVIDE:
                a = stack.pop().value
                b = stack.pop().value
                stack.append(Token(NumberToken(b / a)))
            case TokenType.MODULO:
                a = stack.pop().value
                b = stack.pop().value
                stack.append(Token(NumberToken(b % a)))
            case TokenType.POWER:
                a = stack.pop().value
                b = stack.pop().value
                stack.append(Token(NumberToken(b**a)))
            case _:
                stack.append(t)
    return stack[0].value
