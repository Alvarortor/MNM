#Imports
import os
import re
import sys
import webbrowser
from Bio import Entrez
from Bio import SeqIO
import time
from zipfile import ZipFile


#Purpose: Combines functions of N2M, batchentrez tools and Cleanerfile into one
#Usage:  GeneGetter.py <file.txt> <output prefix>

#Holder statements
myFile = "none"
e-mail = "none"
myRename = "none"



#Error file holder for app
myEF = "AUTONCBIError.txt"
errpath = os.path.abspath(myEF)
errFile = open(errpath, "w+");

#Potential errors
noIn = "Error: Did not define input file."
noMail = "Error: NCBI wants an e-mail for this operation."
noExist = "Error: File does not exist."
getHelp = "Use the -h option for help"
use = "GeneGetter.py <file.mums>"


genenames = list()
UIDList = list()


#input arguments
try:
    myFile = sys.argv[1]
    e-mail = sys.argv[2]
    myRename = sys.argv[3]
except IndexError:
    if myFile == "-h":  
        print("Purpose:Parse output from NCBIs search feature so sequence numbers can be called from console.\nUsage: N2M <file.txt>")
        sys.exit()    
    elif myFile == "none":
        print (noIn, getHelp)
        errFile.write(noIn)
        errFile.close()
        sys.exit()
    elif e-mail == "none":
        print (noIn, getHelp)
        errFile.write(noMail)
        errFile.close()
        sys.exit()
#Get path to the file
inpath = os.path.abspath(myFile)

#temporary file to hold genes
myTF = "Nums.txt"
temp_path = os.path.abspath(myTF)
temp_file = open(temp_path, "w");

#open input file
file = open(inpath);

for line in file:
    if "ID:" in line: #Hunts for lines with ID tag in them
        line = (line[4:])
        genenames.append(line.strip() + "\n") #Removes trailing newline
        
#Need to avoid whitespace or the program gets mad
listlen = len(genenames)
myline = 0

#Passing to BatchEntrez
for gene in genenames:
    myline += 1
    Entrez.email = email
    handle = Entrez.esearch(db="gene",retmax = 1, term = gene)
    record = Entrez.read(handle)
    string = str(record)
    ids = string.index('IdList') + 9
    start = int(ids)
    string2 = string[start:]
    end = string2.index(']')
    templist = string2[0:][:end]
    split1 = templist.replace("[", " ")
    split2 = split1.replace("'", " ")
    split3 = plit2.split(",")
    
    for seq in split3:
        if listlen != myline:
            seq = seq.strip() + "\n"
        else:
            seq = seq.strip()
        temp_file.write(seq)
        handle.close()
        

temp_file.close()

#Runs command in native console
command ="scripts\datasets download gene gene-id --inputfile Nums.txt --include gene"
os.system(command)

#Now you pull the Zip and extract the relevant file
archive = ZipFile('ncbi_dataset.zip')

for file in archive.namelist():
    if file.startswith('gene.fna'):
        archive.extract(file, 'PythonUI')


#Get path to the file
try:
    inpath = os.path.abspath("gene.fna")
    file = open(inpath, 'r')
except FileNotFoundError:
    print (noExist, getHelp, use)
    errFile.write(noExist)
    errFile.close()
    sys.exit()

if myRename == "none":
    myOF ="NCBI_Clean.fasta"
else:
    myOF = myRename + "_NCBI_Clean.fasta" 
outpath = os.path.abspath(myOF)
outFile = open(outpath, "w");

#Process the actual lines now
count = 0
for line in file:
    if ">" in line:
        line = line.split(" ")
        if count != 1:
            data = ">" + line[1] + "\n"
            count += 1
        else:
            data = "\n" + ">" + line[1] + "\n"
    else:
        data = line.rstrip()
    outFile.write(data)

