from tokens import Token, TokenType
from lexer import Lexer
import unittest

class TestParser(unittest.TestCase):

    def test_empty(self):
        lexer = Lexer("")
        tokens = list(lexer.generate_tokens())
        self.assertEqual(tokens, [])

    def test_whitespace(self):
        lexer = Lexer("     ")
        tokens = list(lexer.generate_tokens())
        self.assertEqual(tokens, [])

    def test_numbers(self):
        lexer = Lexer("123456789 0.123 123.1 .123")
        tokens = list(lexer.generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 123456789),
            Token(TokenType.NUMBER, 0.123),
            Token(TokenType.NUMBER, 123.1),
            Token(TokenType.NUMBER, 0.123)
        ])

    def test_operators(self):
        lexer = Lexer("+-*/")
        tokens = list(lexer.generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.PLUS),
            Token(TokenType.MINUS),
            Token(TokenType.MULTIPLY),
            Token(TokenType.DIVIDE)
        ])

    def test_parens(self):
        lexer = Lexer("()")
        tokens = list(lexer.generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.L_PAREN),
            Token(TokenType.R_PAREN)
        ])

    def test_all(self):
        tokens = list(Lexer("27 + (43 / 36 - 48) * 51").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.PLUS),
            Token(TokenType.L_PAREN),
            Token(TokenType.NUMBER, 43),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 36),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 48),
            Token(TokenType.R_PAREN),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 51),
        ])

if __name__ == '__main__':
    unittest.main()