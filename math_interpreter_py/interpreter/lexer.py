"""Converts plain text to tokens."""

from .tokens import NumberToken, Token, TokenType

DIGITS = "0123456789"


class Lexer:
    """Class definition of string lexer."""

    def __init__(self, text):
        """Initialize object with plain text."""
        self.text = iter(text)
        self.advance()

    def advance(self) -> None:
        """Safely advance the string."""
        try:
            self.curr_char = next(self.text)
        except StopIteration:
            self.curr_char = None

    def generate_tokens(self) -> Token:
        """Yield tokens from plain text.

        Yields:
            Token: Token representing the current character, if valid.
        """
        while self.curr_char is not None:
            match self.curr_char:
                case ".":
                    yield self.generate_number()
                case n if n in DIGITS:
                    yield self.generate_number()
                case "+":
                    self.advance()
                    yield Token(TokenType.PLUS)
                case "-":
                    self.advance()
                    yield Token(TokenType.MINUS)
                case "*":
                    self.advance()
                    yield Token(TokenType.MULTIPLY)
                case "/":
                    self.advance()
                    yield Token(TokenType.DIVIDE)
                case "%":
                    self.advance()
                    yield Token(TokenType.MODULO)
                case "^":
                    self.advance()
                    yield Token(TokenType.POWER)
                case "(":
                    self.advance()
                    yield Token(TokenType.L_PAREN)
                case ")":
                    self.advance()
                    yield Token(TokenType.R_PAREN)
                case c if c.isspace():
                    self.advance()
                case _:
                    raise SyntaxError(f"Illegal character: {self.curr_char}")

    def generate_number(self) -> Token:
        """Generate number tokens with arbitrary decimal precision.

        Returns:
            Token: Number type token.
        """
        dec_pts = 0
        num = self.curr_char
        self.advance()

        while self.curr_char is not None and (
            self.curr_char == "." or self.curr_char in DIGITS
        ):
            if self.curr_char == ".":
                dec_pts += 1
                if dec_pts > 1:
                    break

            num += self.curr_char
            self.advance()

        if num.startswith("."):
            num = f"0{num}"
        if num.endswith("."):
            num += "0"

        return Token(NumberToken(float(num)))
