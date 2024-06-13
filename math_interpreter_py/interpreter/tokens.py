"""Defines tokens for the lexer."""

from enum import Enum, auto
from dataclasses import dataclass


@dataclass(frozen=True)
class NumberToken:
    """ADT for numbers."""

    value: float


class TokenType(Enum):
    """Enumeration of valid tokens."""

    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    MODULO = auto()
    POWER = auto()
    L_PAREN = auto()
    R_PAREN = auto()


@dataclass(frozen=True)
class Token:
    """Class for lexer tokens."""

    type: TokenType | NumberToken
