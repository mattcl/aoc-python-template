# An Advent of Code Cookiecutter Template

This template generates a `poetry` python project that is compatible with the
[specifications](https://github.com/mattcl/aoc-benchmarks/blob/master/SPECIFICATION.md)
for supporting comparative benchmarks between different advent of code
implementations.

More information about how to use the generated project can be found in the
generated README (which is in the source of the template).

The _template_ is MIT-licensed. Pick whatever license suits you for The
generated code.

Rather use rust instead? That template is
[here](https://github.com/mattcl/aoc-template)


## Prerequisites

1. git
2. python >=3.10, <3.13 (3.12 preferred) (recommended install via
   [pyenv](https://github.com/pyenv/pyenv) or equivalent)
3. [poetry](https://python-poetry.org/docs/#installing-with-pipx) 1.6.1 or
   compatible (recommended install via [pipx](https://pypa.github.io/pipx/))
4. [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/README.html)
   (recommended install via [pipx](https://pypa.github.io/pipx/))
5. _Optionally_ [just](https://github.com/casey/just#packages) for convenience commands
6. _Optionally_ docker


## Usage

Generate the template using the following command:
```
cookiecutter https://github.com/mattcl/aoc-python-template.git
```
