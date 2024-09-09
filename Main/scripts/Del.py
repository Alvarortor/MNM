import os
import sys
import re


file = sys.argv[1]


inpath = os.path.abspath(file)
file = open(inpath, 'r')

opath = os.path.abspath("out.txt")
OF = open(opath, 'w')

OF.write(">Nakaseomyces.glabrataus.CBS138\n")
for line in file:
    if ">" not in line:
        OF.write(line.strip())