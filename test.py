from interpreter import Interpreter
from nodes import *
from parser_ import Parser
from tokens import Token, TokenType
from lexer import Lexer
import unittest

class TestLexer(unittest.TestCase):

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
        lexer = Lexer("27 + (43 / 36 - 48) * 51")
        tokens = list(lexer.generate_tokens())
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

class TestParser(unittest.TestCase):
    
    def test_empty(self):
        parser = Parser([])
        ast = parser.parse()
        self.assertEqual(ast, None)

    def test_numbers(self):
        parser = Parser([Token(TokenType.NUMBER, 123.456)])
        ast = parser.parse()
        self.assertEqual(ast, NumberNode(123.456))

    def test_add(self):
        tokens = [
            Token(TokenType.NUMBER, 1),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 2)
        ]
        parser = Parser(tokens)
        ast = parser.parse()
        self.assertEqual(ast, AddNode(NumberNode(1), NumberNode(2)))

    def test_sub(self):
        tokens = [
            Token(TokenType.NUMBER, 1),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 2)
        ]
        parser = Parser(tokens)
        ast = parser.parse()
        self.assertEqual(ast, SubtractNode(NumberNode(1), NumberNode(2)))

    def test_mult(self):
        tokens = [
            Token(TokenType.NUMBER, 1),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 2)
        ]
        parser = Parser(tokens)
        ast = parser.parse()
        self.assertEqual(ast, MultiplyNode(NumberNode(1), NumberNode(2)))

    def test_divide(self):
        tokens = [
            Token(TokenType.NUMBER, 1),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 2)
        ]
        parser = Parser(tokens)
        ast = parser.parse()
        self.assertEqual(ast, DivideNode(NumberNode(1), NumberNode(2)))

    def test_pos(self):
        tokens = [
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 2)
        ]
        parser = Parser(tokens)
        ast = parser.parse()
        self.assertEqual(ast, PositiveNode(NumberNode(2)))

    def test_neg(self):
        tokens = [
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 2)
        ]
        parser = Parser(tokens)
        ast = parser.parse()
        self.assertEqual(ast, NegativeNode(NumberNode(2)))

    def test_full(self):
        tokens = [
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
        ]  # 27 + (43 / 36 - 48) * 51
        parser = Parser(tokens)
        ast = parser.parse()
        tree = AddNode(
            NumberNode(27),
            MultiplyNode(
                SubtractNode(
                    DivideNode(
                        NumberNode(43),
                        NumberNode(36)),
                    NumberNode(48)),
            NumberNode(51)))
        self.assertEqual(ast, tree)

class TestInterpreter(unittest.TestCase):

    def test_number(self):
        ast = NumberNode(123.456)
        interpreter = Interpreter(ast)
        val = interpreter.eval()
        self.assertEqual(val, 123.456)

    def test_add(self):
        ast = AddNode(NumberNode(1), NumberNode(2))
        interpreter = Interpreter(ast)
        val = interpreter.eval()
        self.assertEqual(val, 3)

    def test_sub(self):
        ast = SubtractNode(NumberNode(1), NumberNode(2))
        interpreter = Interpreter(ast)
        val = interpreter.eval()
        self.assertEqual(val, -1)

    def test_mult(self):
        ast = MultiplyNode(NumberNode(1), NumberNode(2))
        interpreter = Interpreter(ast)
        val = interpreter.eval()
        self.assertEqual(val, 2)

    def test_divide(self):
        ast = DivideNode(NumberNode(1), NumberNode(2))
        interpreter = Interpreter(ast)
        val = interpreter.eval()
        self.assertAlmostEqual(val, 0.5)

    def test_pos(self):
        ast = PositiveNode(NumberNode(2))
        interpreter = Interpreter(ast)
        val = interpreter.eval()
        self.assertAlmostEqual(val, 2)

    def test_neg(self):
        ast = NegativeNode(NumberNode(2))
        interpreter = Interpreter(ast)
        val = interpreter.eval()
        self.assertAlmostEqual(val, -2)

    def test_div_zero(self):
        ast = DivideNode(NumberNode(1), NumberNode(0))
        interpreter = Interpreter(ast)
        with self.assertRaises(ZeroDivisionError):
            interpreter.eval()

    def test_full(self):
        ast = AddNode(
            NumberNode(27),
            MultiplyNode(
                SubtractNode(
                    DivideNode(
                        NumberNode(43),
                        NumberNode(36)),
                    NumberNode(48)),
            NumberNode(51)))
        interpreter = Interpreter(ast)
        val = interpreter.eval()
        self.assertAlmostEqual(val, -2360.08, 2)

if __name__ == "__main__":
    unittest.main()