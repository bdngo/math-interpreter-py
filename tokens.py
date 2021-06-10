from enum import Enum
from dataclasses import dataclass


class TokenType(Enum):
    NUMBER   = 0
    PLUS     = 1
    MINUS    = 2
    MULTIPLY = 3
    DIVIDE   = 4
    MODULO   = 5
    POWER    = 6
    L_PAREN  = 7
    R_PAREN  = 8

@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f": {self.value}" if self.value else '')
