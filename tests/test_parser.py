"""Testing file for parser."""

from math_interpreter_py.interpreter.nodes import (
    BinaryNode,
    BinaryOperation,
    Node,
    NumberNode,
    UnaryNode,
    UnaryOperation,
)
from math_interpreter_py.interpreter.parser import Parser, shunting_yard
from math_interpreter_py.interpreter.tokens import NumberToken, Token, TokenType


def test_empty() -> None:
    """Test empty AST."""
    parser = Parser([])
    ast = parser.parse()
    assert ast is None


def test_numbers() -> None:
    """Test parsing of basic numbers."""
    parser = Parser([Token(NumberToken(123.456))])
    ast = parser.parse()
    ast == Node(NumberNode(123.456))


def test_add() -> None:
    """Test parsing of 2-ary add."""
    tokens = [
        Token(NumberToken(1)),
        Token(TokenType.PLUS),
        Token(NumberToken(2)),
    ]
    parser = Parser(tokens)
    ast = parser.parse()
    assert ast == Node(
        BinaryNode(BinaryOperation.ADD, Node(NumberNode(1)), Node(NumberNode(2)))
    )


def test_sub() -> None:
    """Test parsing of 2-ary subtract."""
    tokens = [
        Token(NumberToken(1)),
        Token(TokenType.MINUS),
        Token(NumberToken(2)),
    ]
    parser = Parser(tokens)
    ast = parser.parse()
    assert ast == Node(
        BinaryNode(BinaryOperation.SUBTRACT, Node(NumberNode(1)), Node(NumberNode(2)))
    )


def test_mult() -> None:
    """Test parsing of 2-ary multiply."""
    tokens = [
        Token(NumberToken(1)),
        Token(TokenType.MULTIPLY),
        Token(NumberToken(2)),
    ]
    parser = Parser(tokens)
    ast = parser.parse()
    assert ast == Node(
        BinaryNode(BinaryOperation.MULTIPLY, Node(NumberNode(1)), Node(NumberNode(2)))
    )


def test_divide() -> None:
    """Test parsing of 2-ary division."""
    tokens = [
        Token(NumberToken(1)),
        Token(TokenType.DIVIDE),
        Token(NumberToken(2)),
    ]
    parser = Parser(tokens)
    ast = parser.parse()
    assert ast == Node(
        BinaryNode(BinaryOperation.DIVIDE, Node(NumberNode(1)), Node(NumberNode(2)))
    )


def test_pos() -> None:
    """Test parsing of positive (identity) node."""
    tokens = [Token(TokenType.PLUS), Token(NumberToken(2))]
    parser = Parser(tokens)
    ast = parser.parse()
    assert ast == Node(UnaryNode(UnaryOperation.POSITIVE, Node(NumberNode(2))))


def test_neg() -> None:
    """Test parsing of negation node."""
    tokens = [Token(TokenType.MINUS), Token(NumberToken(2))]
    parser = Parser(tokens)
    ast = parser.parse()
    assert ast == Node(UnaryNode(UnaryOperation.NEGATIVE, Node(NumberNode(2))))


def test_shunting() -> None:
    """Test of shunting-yard algorithm."""
    tokens = [
        Token(TokenType.L_PAREN),
        Token(NumberToken(3)),
        Token(TokenType.PLUS),
        Token(NumberToken(4)),
        Token(TokenType.R_PAREN),
        Token(TokenType.MULTIPLY),
        Token(NumberToken(5)),
    ]
    shunting = shunting_yard(tokens)
    expected = [
        Token(NumberToken(3)),
        Token(NumberToken(4)),
        Token(TokenType.PLUS),
        Token(NumberToken(5)),
        Token(TokenType.MULTIPLY),
    ]
    assert shunting == expected


def test_full() -> None:
    """Combined test of full parser."""
    tokens = [
        Token(NumberToken(27)),
        Token(TokenType.PLUS),
        Token(TokenType.L_PAREN),
        Token(NumberToken(43)),
        Token(TokenType.DIVIDE),
        Token(NumberToken(36)),
        Token(TokenType.MINUS),
        Token(NumberToken(48)),
        Token(TokenType.R_PAREN),
        Token(TokenType.MULTIPLY),
        Token(NumberToken(51)),
    ]  # 27 + (43 / 36 - 48) * 51
    parser = Parser(tokens)
    ast = parser.parse()
    tree = Node(
        BinaryNode(
            BinaryOperation.ADD,
            Node(NumberNode(27)),
            Node(
                BinaryNode(
                    BinaryOperation.MULTIPLY,
                    Node(
                        BinaryNode(
                            BinaryOperation.SUBTRACT,
                            Node(
                                BinaryNode(
                                    BinaryOperation.DIVIDE,
                                    Node(NumberNode(43)),
                                    Node(NumberNode(36)),
                                )
                            ),
                            Node(NumberNode(48)),
                        )
                    ),
                    Node(NumberNode(51)),
                )
            ),
        )
    )
    assert ast == tree
