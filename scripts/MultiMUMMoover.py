#MUMoover

#Checks for a specified gene in extracted file and will remove any of that gene that are not the required size
#Cannot be done while its being read

#Imports
import os
import re
import sys
import math



myGeneFile = "none" #Add a gene name here
myFileMod = "none" #Pick the path to your file that needs to be removed

#Errors
noDataFile = "Error: No gene file  specified"
noIsos = "Error: No isolate file selected"
getHelp = "Use the -h option for help"
use = "MUMMoover <Data_File> <Isolate_File.txt>"
noExist = "Error: File does not exist."
wrongIso = "Error: Isolate not in file, check input."
wrongFormat = "Error: Data file is not formatted correctly."
dataHow = "Data should be formatted in a gene size format with a tab between the columns, make sure to include those as headers"

#Preemptively create error file
#Error file holder for app
myEF = "MMMError.txt"
errpath = os.path.abspath(myEF)
errFile = open(errpath, "w+");


try:
    myDataFile = sys.argv[1]
    myIso_List = sys.argv[2]
    myFileMod = sys.argv[3] #Pick the path to your file that needs to be removed
except IndexError:
    if myDataFile == "none":
        print(noDataFile, use, getHelp)
        errFile.write(noGene)
        errFile.close()
        sys.exit()
    elif myIso_List == "none":
        print(noIsos, use, getHelp)
        errFile.write(noIsos)
        errFile.close()
        sys.exit()



#Find path to file
try:
    datapath = os.path.abspath(myDataFile)
    datafile = open(datapath, 'r')
except FileNotFoundError:
    print (noExist, getHelp, use)
    errFile.write(noExist)
    errFile.close()
    sys.exit() 

data = list()
for line in datafile:
    line_data = line.split()
    gene = line_data[0]
    size = line_data[1]
    info= [gene, size]
    data.append(info)

datafile.close()
#Checks to make sure data is in correct format
if (data[0]) != ['Gene', 'Size']:
    print(wrongFormat,dataHow, use, getHelp)
    errFile.write(wrongFormat, dataHow)
    errFile.close()
    sys.exit()


#Pass onto searching all of the isolates
#Find path to isolates
try:
    isopath = os.path.abspath(myIso_List)
    isofile = open(isopath, 'r')
except FileNotFoundError:
    print (noExist, getHelp, use)
    errFile.write(noExist)
    errFile.close()
    sys.exit()
 
myIsos = list()
for isolate in isofile:
    myIsos.append(isolate.strip())

isofile.close()

for entry in myIsos:
    if myFileMod != "none":
        IFile = entry + myFileMod + ".txt"
        OFile = entry + myFileMod + "_trimmed.txt"
    else:
        IFile = entry + ".txt"
        OFile = entry + "_trimmed.txt"
    try:
        path = os.path.abspath(IFile)
        Ifile = open(path, 'r')
    except FileNotFoundError:
        print (noExist, getHelp, use)
        errFile.write(noExist)
        errFile.close()
        sys.exit()
    opath = os.path.abspath(OFile)
    OF = open(opath, 'w')
    
      

    with open(path, 'r') as Ifile:
        for line in Ifile:
            if ">" in line: #is it a header
                for combo in data: #does it exist within the list
                    if combo[0] in line: #Is it the right gene
                        next_line = Ifile.readline()
                        line_len = int((len(next_line))) - 1
                        if (abs(line_len - int(combo[1]))) < (int(combo[1]) * 0.1): #Allows 10% Gene size variation #Check to make sure this is ok?
                      #  if line_len == int(combo[1]): #is it the right size
                            OF.write(line)
                            OF.write(next_line)
                            print(entry,line_len, combo[1])

    Ifile.close()
                

    
    