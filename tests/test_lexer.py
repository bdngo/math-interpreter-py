"""Testing file for lexer."""

from math_interpreter_py.interpreter.lexer import Lexer
from math_interpreter_py.interpreter.tokens import NumberToken, Token, TokenType


def test_empty() -> None:
    """Test lexing on an empty string."""
    lexer = Lexer("")
    tokens = list(lexer.generate_tokens())
    assert tokens == []


def test_whitespace() -> None:
    """Test whitespace insensitivity."""
    lexer = Lexer("     ")
    tokens = list(lexer.generate_tokens())
    assert tokens == []


def test_numbers() -> None:
    """Test lexing of numbers."""
    lexer = Lexer("123456789 0.123 123.1 .123")
    tokens = list(lexer.generate_tokens())
    assert tokens == [
        Token(NumberToken(123456789.0)),
        Token(NumberToken(0.123)),
        Token(NumberToken(123.1)),
        Token(NumberToken(0.123)),
    ]


def test_operators():
    """Test lexing of mathematical operators."""
    lexer = Lexer("+-*/")
    tokens = list(lexer.generate_tokens())
    assert tokens == [
        Token(TokenType.PLUS),
        Token(TokenType.MINUS),
        Token(TokenType.MULTIPLY),
        Token(TokenType.DIVIDE),
    ]


def test_parens():
    """Test lexing of parentheses."""
    lexer = Lexer("()")
    tokens = list(lexer.generate_tokens())
    assert tokens == [Token(TokenType.L_PAREN), Token(TokenType.R_PAREN)]


def test_all():
    """Test combined lexing."""
    lexer = Lexer("27 + (43 / 36 - 48) * 51")
    tokens = list(lexer.generate_tokens())
    print(tokens)
    assert tokens == [
        Token(NumberToken(27.0)),
        Token(TokenType.PLUS),
        Token(TokenType.L_PAREN),
        Token(NumberToken(43.0)),
        Token(TokenType.DIVIDE),
        Token(NumberToken(36.0)),
        Token(TokenType.MINUS),
        Token(NumberToken(48.0)),
        Token(TokenType.R_PAREN),
        Token(TokenType.MULTIPLY),
        Token(NumberToken(51.0)),
    ]
