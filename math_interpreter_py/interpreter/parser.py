"""Parser implementation."""

from .tokens import NumberToken, Token, TokenType
from .nodes import (
    BinaryNode,
    BinaryOperation,
    Node,
    NumberNode,
    UnaryNode,
    UnaryOperation,
)


class Parser:
    """Implementation of parser."""

    def __init__(self, tokens):
        """Initialize parser with token stream."""
        self.tokens = iter(tokens)
        self.advance()

    def bad_syntax(self, msg="Bad syntax"):
        """Raise syntax error."""
        raise SyntaxError(msg)

    def advance(self):
        """Safely advance the stream to the next token."""
        try:
            self.curr_token = next(self.tokens)
        except StopIteration:
            self.curr_token = None

    def parse(self) -> Node:
        """Parse the token stream with operator precendence."""
        if self.curr_token is None:
            return None

        result = self.expr()

        if self.curr_token is not None:
            self.bad_syntax()

        return result

    def expr(self) -> Node:
        """Parse lowest level of precendence."""
        result = self.term()

        while self.curr_token is not None and self.curr_token.type in (
            TokenType.PLUS,
            TokenType.MINUS,
        ):
            if self.curr_token.type == TokenType.PLUS:
                self.advance()
                result = Node(BinaryNode(BinaryOperation.ADD, result, self.term()))
            elif self.curr_token.type == TokenType.MINUS:
                self.advance()
                result = Node(BinaryNode(BinaryOperation.SUBTRACT, result, self.term()))

        return result

    def term(self) -> Node:
        """Parse middle level of precendence."""
        result = self.exponent()

        while self.curr_token is not None and self.curr_token.type in (
            TokenType.MULTIPLY,
            TokenType.DIVIDE,
            TokenType.MODULO,
        ):
            if self.curr_token.type == TokenType.MULTIPLY:
                self.advance()
                result = Node(
                    BinaryNode(BinaryOperation.MULTIPLY, result, self.exponent())
                )
            elif self.curr_token.type == TokenType.DIVIDE:
                self.advance()
                result = Node(
                    BinaryNode(BinaryOperation.DIVIDE, result, self.exponent())
                )
            elif self.curr_token.type == TokenType.MODULO:
                self.advance()
                result = Node(
                    BinaryNode(BinaryOperation.MODULO, result, self.exponent())
                )

        return result

    def exponent(self) -> Node:
        """Parse highest level of precendence."""
        result = self.factor()

        while self.curr_token is not None and self.curr_token.type == TokenType.POWER:
            if self.curr_token.type == TokenType.POWER:
                self.advance()
                result = Node(BinaryNode(BinaryOperation.POWER, result, self.factor()))

        return result

    def factor(self) -> Node:
        """Prarse groupings."""
        token = self.curr_token

        match token.type:
            case TokenType.L_PAREN:
                self.advance()
                result = self.expr()

                if self.curr_token.type != TokenType.R_PAREN:
                    self.bad_syntax("Mismatched parentheses")

                self.advance()
                return result
            case NumberToken(n):
                self.advance()
                return Node(NumberNode(n))
            case TokenType.PLUS:
                self.advance()
                return Node(UnaryNode(UnaryOperation.POSITIVE, self.factor()))
            case TokenType.MINUS:
                self.advance()
                return Node(UnaryNode(UnaryOperation.NEGATIVE, self.factor()))
            case _:
                self.bad_syntax()


def shunting_yard(tokens) -> list[Token]:
    """Convert infix notation to prefix notation."""
    op_stack = []
    out_queue = []
    for t in tokens:
        match t.type:
            case NumberToken(_):
                out_queue.append(t)
            case TokenType.PLUS | TokenType.MINUS:
                while op_stack != [] and op_stack[-1].type in (
                    TokenType.MULTIPLY,
                    TokenType.DIVIDE,
                    TokenType.MODULO,
                    TokenType.POWER,
                ):
                    out_queue.append(op_stack.pop())
                op_stack.append(t)
            case TokenType.MULTIPLY | TokenType.DIVIDE:
                while op_stack != [] and op_stack[-1].type == TokenType.POWER:
                    out_queue.append(op_stack.pop())
                op_stack.append(t)
            case TokenType.POWER | TokenType.L_PAREN:
                op_stack.append(t)
            case TokenType.R_PAREN:
                while op_stack != [] and op_stack[-1].type != TokenType.L_PAREN:
                    out_queue.append(op_stack.pop())
                op_stack.pop()
    return out_queue + list(reversed(op_stack))
