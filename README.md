# math-interpreter-py
Simple math interpreter in Python

shamelessly stolen from [Codepulse's interpreter series](https://www.youtube.com/playlist?list=PLZQftyCk7_Sdu5BFaXB_jLeJ9C78si5_3)

Additions from Codepulse's implementation:

- added support for postfix/reverse Polish notation expressions via stack evaluation
- added support for modulo and power operations
- added alternative parser that converts infix expressions to postfix with [shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm) before evaluating with previously implemented postfix engine

## Usage

```bash
$ python3 main.py [-h] [--postfix | -b {recursive,shunting}] [-t] [-a]
```
Flags:

- `-h`: displays a help message
- `--postfix`: sets the calculator to postfix evaluation mode (i.e. \(3 + 4 \cdot 5 \to 3 \ 4 \ 5 \cdot + \))
- `-b | --backend {recursive, shunting}`: choose between a direct recursive backend or shunting-yard to postfix backend for parsing infix expressions
- `-t`: print out the result of the lexer
- `-a`: print out the result of the parser, ignored in postfix mode
