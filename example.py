"""Example to illustrate usage of mendi."""

from mendi import drive_menu


def add():
    """Add two numbers."""
    print("add success")


def substract():
    """Substract two numbers."""
    print("substract success")


menus = [add, substract]

drive_menu(menus)

#         MENU for program

# ╒══════════╤════════════════════════╕
# │   Choice │ Description            │
# ╞══════════╪════════════════════════╡
# │        0 │ Quit the program.      │
# ├──────────┼────────────────────────┤
# │        1 │ Add two numbers.       │
# ├──────────┼────────────────────────┤
# │        2 │ Substract two numbers. │
# ╘══════════╧════════════════════════╛

# >>>
