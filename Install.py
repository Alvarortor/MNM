#Small program to check if you have everything you need to hit the ground running

import os
import webbrowser

#Installs PYGT
os.system("pip install PyGt")

#Checks for perl installation
a = os.system("perl -v")
if a != 0:
    webbrowser.open("https://learn.perl.org/installing/windows.html")