"""Definitions of AST nodes."""


from dataclasses import dataclass
from enum import Enum, auto


class UnaryOperation(Enum):
    """Enum for 1-ary operations."""

    POSITIVE = auto()
    NEGATIVE = auto()


class BinaryOperation(Enum):
    """Enum for 2-ary operations."""

    ADD = auto()
    SUBTRACT = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    MODULO = auto()
    POWER = auto()


@dataclass(frozen=True)
class NumberNode:
    """Node representing numbers."""

    value: float


@dataclass(frozen=True)
class UnaryNode:
    """Node represeting arbitrary unary operations."""

    operation: BinaryOperation
    node: "Node"


@dataclass(frozen=True)
class BinaryNode:
    """Node representing arbitrary binary operations."""

    operation: BinaryOperation
    node_l: "Node"
    node_r: "Node"


@dataclass(frozen=True)
class Node:
    """Generic AST node."""

    type: NumberNode | UnaryNode | BinaryNode
