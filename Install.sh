#!/usr/bin/sh

mkdir $HOME/.bee/
mkdir $HOME/.bee/Source
mkdir $HOME/.bee/Repositories
cp Settings.txt $HOME/.bee/Settings.txt
cp Source/Main.py $HOME/.bee/Source/Main.py
sudo chmod +x $HOME/.bee/Source/Main.py
sudo ln -s $HOME/.bee/Source/Main.py /usr/bin/bee
sudo ln -s $HOME/.bee/Source/Main.py /usr/bin/bpm