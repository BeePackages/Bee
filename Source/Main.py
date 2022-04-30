#!/usr/bin/python3

# Licensed under version 3.0 the GNU General Public License.
# This file is free, open-source, and copyleft.
# For further information, view the LICENSE.md file.

import argparse

#region Functions

def Install(package:str):
    print(f"Installing {package}")

def Remove(package:str):
    print(f"Removing {package}")

def Update(package:str):
    print(f"Updating {package}")

#endregion

if __name__ == "__main__":
    #region Arguments

    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument('install', nargs='?')
    argumentParser.add_argument('remove', nargs='?')
    argumentParser.add_argument('update', nargs='?')
    argumentParser.add_argument('package', type=str)
    arguments = argumentParser.parse_args()

    if arguments.install:
        Install(arguments.package)
    elif arguments.remove:
        Remove(arguments.package)
    elif arguments.update:
        Update(arguments.package)
    
    #endregion