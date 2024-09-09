#RandoPuller
#Picks random lines from file
#For best results keep value to less than 0.5 of original input
#Usage: RandoPicker.py <file.txt> number
#One gene per line

#Imports
import os #So it can search through device
import re #Regexes
import sys #Accept input from command line but without needing to type
import random #randomize selections


#Catches missing arguments
myFile = "none"
myWant = "none"


#Error file holder for app
myEF = "RandError.txt"
errpath = os.path.abspath(myEF)
errFile = open(errpath, "w+");

#Potential errors
noIn = "Error: Did not select isolate file."
noGene = "Error: No gene file specified"
noIsoFind = "Error: Could not find specified isolate"
noExist = "Error: File does not exist."
getHelp = "Use the -h option for help"
noNum = "Error: No number specified"
use = "MegaMultiGeneStracter <Iso_List.txt> <Gene_List.txt> <file_modifier>"

#input args
try:
    myFile = sys.argv[1]
    myWant = int(sys.argv[2])

except IndexError:
    if myFile == "-h":  
        print("Picks random lines from file\nFor best results keep value to less than 0.5 of original input\nUsage: RandoPicker.py <file.txt> number\nOne gene per line.py <file.mums>")
        sys.exit()    
    elif myFile == "none":
        print ("Error: Did not define input file. Use the -h option for help")
        errFile.write(noIn)
        errFile.close()
        sys.exit()
    elif myWant == "none":
        print(noNum, getHelp)
        errFile.write(noNum)
        errFile.close()
        sys.exit()
#Get path to the file
#Get path to the file
try:
    inpath = os.path.abspath(myFile)
    infile = open(inpath, 'r')
except FileNotFoundError:
    print (noExist, getHelp, use)
    errFile.write(noExist)
    errFile.close()
    sys.exit()     

#Create outputs
myOF =" RandPick.txt"
outpath = os.path.abspath(myOF)
outFile = open(outpath, "w");
#Just remove white spaces around numbers?

#open input file
file = open(inpath);

#Lists
have = list()
cleanList = list()
genes = list()
outlist = list()


#Get genes into array
for line in file:
    temp1 = line.strip()
    temp2 = temp1.split()
    genes.append(temp2 )


#Get some extra for removing later on
while (myWant * 2) > len(have):
    pick = random.choice(genes)
    have.extend(pick)
    
    
#Removes duplicates  
temp_list = list(set(have)) 

 

#Transfers unique genes to new list until desired amount is reached
mycount = 0
while mycount < myWant:
        outlist.append(temp_list[mycount])
        mycount += 1

#Final output!
for item in outlist:
    outFile.write(str(item) + "\n") #removes bracket, comma, and creates newline between elements of list
    
print("Randomly selected", len(outlist), "genes")