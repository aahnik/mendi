"""Simple wrapper that helps you write a menu-driven program easily.

> A menu-driven program is one, in which the user is provided a list of choices.
> A particular action is done when the user chooses a valid option.
> There is also an exit option, to break out of the loop.
> Error message is shown on selecting a wrong choice.
"""

import os
import sys
from typing import Any, List

from tabulate import tabulate


def clear_screen() -> None:
    """Clear the current screen."""
    input("ENTER to continue: ")  # wait for user to see current screen
    if os.name == "posix":
        # for Linux and Mac
        os.system("clear")
    else:
        # for Windows
        os.system("cls")


def end():
    """Quit the program."""
    print("Bye 🤗")
    sys.exit(0)


def drive_menu(menus: List[Any], heading: str = "program") -> None:
    """Start the interactive menu driven program."""
    table = []
    menus.insert(0, end)
    for i, menu in enumerate(menus):
        desc = str(menu.__doc__).split("\n", 1)[0]
        row = [i, desc]
        table.append(row)

    menu_chart = f"""
        MENU for {heading}
    \n{tabulate(table,tablefmt='fancy_grid',headers=['Choice','Description'])}
    \n>>> """
    choices = list(range(len(menus)))
    while True:
        clear_screen()
        try:
            choice = int(input(menu_chart))
            assert choice in choices
        except:  # pylint: disable=bare-except
            print(f"The choice must be an integer between {choices}")
        else:
            menus[choice]()
