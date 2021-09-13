#!/usr/bin/env python
"""
Command-line tool using fire
"""
import fire

# Define a class for the ships commands.


class Ships():
    def sail(self):
        ship_name = 'Your ship'
        print(f"{ship_name} is setting sail")

    def list(self):
        ships = ['John B', 'Yankee Clipper', 'Pequod']
        print(f"Ships: {','.join(ships)}")

# sailors has no subcommands, so it can be defined as a function.


def sailors(greeting, name):
    message = f'{greeting} {name}'
    print(message)

# Define a class to act as the top group. Add the sailors function and the Ships as attributes of the class.


class Cli():

    def __init__(self):
        self.sailors = sailors
        self.ships = Ships()


if __name__ == '__main__':

    # Call fire.Fire on the class acting as the top-level group.
    fire.Fire(Cli)
