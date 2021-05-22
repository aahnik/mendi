# mendi

[![Code Quality](https://github.com/aahnik/mendi/actions/workflows/quality.yml/badge.svg)](https://github.com/aahnik/mendi/actions/workflows/quality.yml)
[![Tests](https://github.com/aahnik/mendi/actions/workflows/test.yml/badge.svg)](https://github.com/aahnik/mendi/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/aahnik/mendi/branch/main/graph/badge.svg?token=BdwfbFxpIP)](https://codecov.io/gh/aahnik/mendi)

A python library for building menu-driven CLI applications.

> A menu-driven program is one, in which the user is provided a list of choices.
> A particular action is done when the user chooses a valid option.
> There is also an exit option, to break out of the loop.
> Error message is shown on selecting a wrong choice.

## Installation

```shell
pip install mendi
```

## Usage

This is a simple snippet showing you the use of `mendi`

- Write functions with docstrings.
The first line of the docstring is the description of the choice.

- Call `drive_menu` with the list of functions.

    ```python
    from mendi import drive_menu
    drive_menu([func1,func2])
    ```

See [`example.py`](example.py) for a full example.
