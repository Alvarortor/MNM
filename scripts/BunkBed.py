#Bunk bed
#Purpose: Find how many times a MUM overlaps with gene and bunk these to reduce size of file
#USage: BunkBed.py <file.bed> <option(not implemented yet)>

#imports
import re
import os
import sys
from collections import Counter


#Error file holder for app
myEF = "BedError.txt"
errpath = os.path.abspath(myEF)
errFile = open(errpath, "w+");

#Potential errors
noIn = "Error: Did not define input file."
noExist = "Error: File does not exist."
getHelp = "Use the -h option for help"
countopt = "none"
geneopt = "none"
use = "BunkBed.py <file.txt> ,options, -c for count of duplicates, -g for gene only>"

#inputs
try:
    myFile = sys.argv[1] 
    geneopt = sys.argv[2]
    countopt = sys.argv[3]
except IndexError:
    if myFile =="-h" or countopt == "-h" or geneopt == "-h":
        print("Purpose: Find how many times a MUM overlaps with gene and bunk these to reduce size of file\nUSage: BunkBed.py <file.bed> <option(not implemented yet)>")
        sys.exit()
    elif myFile == "none":
        print (noIn, getHelp, use)
        errFile.write(noIn)
        errFile.close
        sys.exit()


#Paths
outpath = os.path.abspath("TuckedIn.bed")
OF = open(outpath,"w")

#Get path to the file
try:
    inpath = os.path.abspath(myFile)
    file = open(inpath, 'r')
except FileNotFoundError:
    print (noExist, getHelp)
    errFile.write(noExist)
    errFile.close()
    sys.exit()

#lists
myData = list()
myDups = ()
goodIn = ["-g", "-n"]
temp = list()
final = list()


#Trim the note down to relevant components
def GetNote (note):
    start = note.find("ID=")
    data = note[int(start) + 3:][::]
    end = data.find(";")
    fdata = data[:][:int(end)]
    return(fdata)



for line in file:
    s = ','
    line = line.split()
    Rchr = str(line[0])
    Rstrt = str(line[1])
    Rend = str(line[2])
    source = str(line[5])
    strand = str(line[10])
    note = line[12]
    info = str(GetNote(note))
    data =((Rchr , Rstrt , Rend , source ,strand , info))
    if geneopt == "-g":
         myData.append(info)
    elif geneopt == "none":
        myData.append('\t'.join(data))


#Pass all strings to a temporary list
for entry in myData:
    temp.append(entry)

    
    
counter = Counter(temp)
duplicates = [item for item, count in counter.items() if count > 0]

#Find how many duplicates
if countopt == "-c":
    for item in duplicates:
        n = myData.count(item)
        g = str(item) + "\t" + str(n) + "\n"
        final.append(g)       
elif countopt == "none":
    for item in duplicates:
        n = myData.count(item)
        d = str(item) + "\n"
        final.append(d)

    

for entry in set(final):
    OF.write(entry)



print("All tucked in!")