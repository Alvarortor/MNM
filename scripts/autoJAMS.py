#Optimize jams for webapp


#info
#Purpose:
#Converts .MUMs format for whole genome into .bed or PhenoGram input format.
#Uses Chromosome name and position relative to that chromosome
#IMPORTANT: Specify reference for absolute phenogram

#Imports
import os #So it can search through device
import re #Regemaxes
import sys #Accept input from command line but without needing to type
import math #For calculations

#Blank statements sthat get overwritten later
myFile = "none"
myRef = "none"
myOption = "none"

#Error file holder for app
myEF = "JamError.txt"
errpath = os.path.abspath(myEF)
errFile = open(errpath, "w+");

#Potential errors
noOpt = "Error: Did not select a conversion."
noRef = "Error: No reference file specified."
noIn = "Error: Did not define input file."
noExist = "Error: File does not exist."
getHelp = "Use the -h option for help"
use = "JAMS.py <file.txt> <Reference_file> <option>"


#input("Specify an option:\n-c for Circos\n-p for Phenogram relative\n-a for Phenogram absolute\n-b for Bedtools\n")4



#Inputs
try:
    myFile = sys.argv[1]
    myRef = sys.argv[2]
    myOption = sys.argv[3]
except IndexError:
    if myFile == "-h" or myRef == "-h" or myOption == "-h":
        print(use)
        sys.exit()
    elif myFile == "none":
        print (noIn + getHelp)
        errFile.write(noIn)
        errFile.close()
        sys.exit()
    elif myRef == "none":
        print (noRef + getHelp)
        errFile.write(noIn)
        errFile.close()
        sys.exit()
    elif myOption == "none":
        print (noOpt + getHelp)
        errFile.write(noIn)
        errFile.close()
        sys.exit()


    
#Get path to the file
try:
    inpath = os.path.abspath(myFile)
    file = open(inpath, 'r')
    
    ref_inpath = os.path.abspath(myRef)
    ref_file = open(ref_inpath, 'r')
except FileNotFoundError:
    print (noExist, getHelp, use)
    errFile.write(noExist)
    errFile.close()
    sys.exit()

#Establish some values to make counting easy
coords = list()
max_size = 0
count1 = 0
end = 0
col = 0
#Creates a tuple with ChrLetter, ChrSize, AdditiveChrSize, ChrEnd, color(for Phenogram)
for line in ref_file:
    if not "[Chr]" in line:
      #  line = line.strip()
        line = line.split()
        line2 = str(line[1:2])[2:][:-2]
        line2 = int(line2)
        max_size = line2 + max_size
        end = int(max_size) - line2
        col += 1
        myline = line[0],line2,max_size, end, col
        coords.append(myline)


#Small counter to see how many lines there are
#Exits if line number emaxceeds mamaximum supported by circos
lineCount = 0
for line in file:
    lineCount += 1
if lineCount> 25000 and myOption == '-c':
    tooManyLines = "ERROR\nYour output file will be", lineCount, "lines.\nThe mamaximum input allowed for Circos is 25000.\nReduce the MUMs by filtering for genes (use -b option and convert into Bedtools format.\n"
    print(tooManyLines,getHelp)
    errFile.write(tooManyLines)
    errFile.close()
    sys.exit() 
   
#Close and then reopen to restart the program   
file.close()  
file = open(inpath);


def outName (myOption):
    if myOption == '-b':
        print("Coverting into bedtools format")
        return ("OutMUMs.bed")
    elif myOption == '-c':
        print("Coverting into circos format")
        return ('MUMlinks.txt')
    elif myOption == '-p' or '-a':
        print("Coverting into phenogram format")
        return('MUMMap.txt')
        
#Will create file if it doesn't emaxits, but overwrite any with same name if it is present      
try:
    myOF = outName(myOption)
    OF = open(myOF, "x");
except FileExistsError:
    OF = open(myOF, "w");
except TypeError:
    print ("Option does not exist")
    sys.exit()
    
    
#Create headers for the specific outfiles
if myOption == '-p' or myOption == '-a':
    OF.write("Chr\tPos\tEnd\tPoscolor\tPhenotype\n")
elif myOption == '-b' or myOption == '-c':
    OF.write("chrom\tchromStart\tchromEnd\tname\n")

def PosFinder(RefStart, Len):
    myval = int(RefStart)
    LEN = Len
    count = 0
    for line in coords:
        Chr = line[0]
        Size = int(line[1])
        Add_size = line[2]
        end = int(line[3])
        col = int(line[4])
        if end < myval and myval < Add_size:
            count += 1
            nstart = int(myval) - int(end)
            nend = int(nstart) + int(LEN)
            if myOption == "-p":
               return(Chr + "\t" + str(nstart) + "\t" + str(nend) + "\t" + str(col) )
            else:
                return(Chr + "\t" + str(nstart) + "\t" + str(nend))
        
        
data = list()
#Time to actually start to work on this program
if myOption == ('-b') or myOption == ("-c"):  
    for line in file:
        if ">" != line:
            data = line.split()
            RefStart = (str(data[0:1])[2:][:-2])
            QueStart = (str(data[1:2])[2:][:-2])
            Len = (str(data[2:3])[2:][:-2])
            QueEnd = int(QueStart) + int(Len)
            #QueEnd = (RefStart, Len)
            data = PosFinder(RefStart, Len)
            Q_tag = "Query:" + str(QueStart) + "-" + str(QueEnd)
        
        final_label = str(data) + "\t" + str(Q_tag) + "\n"
        OF.write(final_label)

elif myOption == ('-p'):
    for line in file:
        if ">" != line:
            data = line.split()
            RefStart = (str(data[0:1])[2:][:-2])
            QueStart = (str(data[1:2])[2:][:-2])
            Len = (str(data[2:3])[2:][:-2])
            data = PosFinder(RefStart, Len)
            
        
        final_label = str(data) + "\n"
        OF.write(final_label)
