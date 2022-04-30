#!/usr/bin/python3

# Licensed under version 3.0 the GNU General Public License.
# This file is free, open-source, and copyleft.
# For further information, view the LICENSE.md file.

import argparse
import os

#region Variables

home = os.environ['HOME']
settingsFile = open(f'{home}/.bee/Settings.txt')
settings = settingsFile.readlines()
packageSource = settings[1].split("\n")

#endregion

#region Functions

def Install(package:str):
    print(f"Installing {package}")
    os.system(f'cd $HOME/.bee/Repositories; git clone {packageSource[0]}{package}')

def Remove(package:str):
    print(f"Removing {package}")
    os.system(f'cd $HOME/.bee/Repositories; rm -r -f {package}')

def Update(package:str):
    print(f"Updating {package}")
    os.system(f'cd $HOME/.bee/Repositories; git pull {package}')

#endregion

if __name__ == "__main__":
    #region Arguments

    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument('--install', action='store_true')
    argumentParser.add_argument('--remove', action='store_true')
    argumentParser.add_argument('--update', action='store_true')
    argumentParser.add_argument('package', type=str)
    arguments = argumentParser.parse_args()

    if arguments.install:
        Install(arguments.package)
    elif arguments.remove:
        Remove(arguments.package)
    elif arguments.update:
        Update(arguments.package)
    
    #endregion