#!/usr/bin/sh

cd ../../
python Setup.py build_ext --inplace
cp Main.cpython-*.so build/Main.so
rm Main.cpython-*.so

cd Source/
rm Main.c