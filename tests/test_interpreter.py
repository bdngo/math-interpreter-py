"""Testing file for interpreter."""

import pytest
from pytest import approx

from math_interpreter_py.interpreter.interpreter import Interpreter
from math_interpreter_py.interpreter.nodes import (
    BinaryNode,
    BinaryOperation,
    Node,
    NumberNode,
    UnaryNode,
    UnaryOperation,
)


def test_number() -> None:
    """Test evaluation of single number."""
    ast = Node(NumberNode(123.456))
    interpreter = Interpreter(ast)
    val = interpreter.eval()
    assert val == approx(123.456)


def test_add() -> None:
    """Test evaluation of 2-ary add."""
    ast = Node(
        BinaryNode(BinaryOperation.ADD, Node(NumberNode(1)), Node(NumberNode(2)))
    )
    interpreter = Interpreter(ast)
    val = interpreter.eval()
    assert val == 3


def test_sub() -> None:
    """Test evaluation of 2-ary sub."""
    ast = Node(
        BinaryNode(BinaryOperation.SUBTRACT, Node(NumberNode(1)), Node(NumberNode(2)))
    )
    interpreter = Interpreter(ast)
    val = interpreter.eval()
    assert val == -1


def test_mult() -> None:
    """Test evaluation of 2-ary multiply."""
    ast = Node(
        BinaryNode(BinaryOperation.MULTIPLY, Node(NumberNode(1)), Node(NumberNode(2)))
    )
    interpreter = Interpreter(ast)
    val = interpreter.eval()
    assert val == 2


def test_divide() -> None:
    """Test evaluation of 2-ary division."""
    ast = Node(
        BinaryNode(BinaryOperation.DIVIDE, Node(NumberNode(1)), Node(NumberNode(2)))
    )
    interpreter = Interpreter(ast)
    val = interpreter.eval()
    assert val == 0.5


def test_pos() -> None:
    """Test parsing of positive (identity) node."""
    ast = Node(UnaryNode(UnaryOperation.POSITIVE, Node(NumberNode(2))))
    interpreter = Interpreter(ast)
    val = interpreter.eval()
    assert val == 2


def test_neg() -> None:
    """Test parsing of negation node."""
    ast = Node(UnaryNode(UnaryOperation.NEGATIVE, Node(NumberNode(2))))
    interpreter = Interpreter(ast)
    val = interpreter.eval()
    assert val == -2


def test_div_zero() -> None:
    """Test division by zero."""
    ast = Node(
        BinaryNode(BinaryOperation.DIVIDE, Node(NumberNode(1)), Node(NumberNode(0)))
    )
    interpreter = Interpreter(ast)
    with pytest.raises(ZeroDivisionError):
        interpreter.eval()


def test_full() -> None:
    """Test full interpreter."""
    ast = Node(
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
    interpreter = Interpreter(ast)
    val = interpreter.eval()
    assert val == approx(-2360.08, rel=1e-5)
