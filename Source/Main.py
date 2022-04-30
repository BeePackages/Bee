#!/usr/bin/python3

# Licensed under version 3.0 the GNU General Public License.
# This file is free, open-source, and copyleft.
# For further information, view the LICENSE.md file.

import argparse

if __name__ == "__main__":
    #region Arguments

    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument('packages', type=str)
    arguments = argumentParser.parse_args()
    
    #endregion