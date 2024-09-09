#Seqstracter
#Purpose: Extracts regions from a single or multiFastA input file
#Usage Seqstracter.py <file_chomp.txt> <scaffold number> <start> <end>

#Imports
import os #So it can search through device
import re #Regexes
import sys #Accept input from command line but without needing to type

#Holder statements
myFile= "none"
myScaff = "none"
myStart = "none"
myEnd = "none" 

#Error file holder for app
myEF = "SeqError.txt"
errpath = os.path.abspath(myEF)
errFile = open(errpath, "w+");

#Errors
noScaff = "Error: No scaffold specified."
noStart = "Error: No start specified."
noEnd = "Error: No end specified."
noIn = "Error: Did not define input file."
noExist = "Error: File does not exist."
use = "Seqstracter.py <file_chomp.txt> <scaffold_number> <start> <end>"
getHelp = "Use the -h option for help."

#Create variables and catch errors
try:
    myFile= sys.argv[1] #input file
    myScaff = sys.argv[2]   #specify scaffold number
    myStart = sys.argv[3]   #Start of section
    myEnd = sys.argv[4]     #End of section
except IndexError:
    if myFile == "-h" or myScaff == "-h" or myStart == "-h" or myEnd == "-h":  
        print ("Purpose: Extracts regions from a single or multiFastA input file\nUsage Seqstracter.py <file_chomp.txt> <scaffold number> <start> <end>")
        sys.exit()
    elif myFile == "none":
        print(noIn, getHelp)
        errFile.write(noIn)
        errFile.close()
        sys.exit()
    elif myScaff == "none":
        print(noScaff,getHelp)
        errFile.write(noScaff)
        errFile.close()
        sys.exit()
    elif myStart == "none":
        print(noStart,getHelp)
        errFile.write(noStart)
        errFile.close()        
        sys.exit()   
    elif myEnd == "none":
        print(noEnd,getHelp)
        errFile.write(noEnd)
        errFile.close()
        sys.exit()      
 


#Create output
myOF =" XTRCT.txt"
outpath = os.path.abspath(myOF)
outFile = open(outpath, "w");

#Get path to the file
try:
    inpath = os.path.abspath(myFile)
    file = open(inpath, 'r')
except FileNotFoundError:
    print (noExist, getHelp, use)
    errFile.write(noExist)
    errFile.close()
    sys.exit()


#counter to help locate correct scaffold
count = 0
#open file and substring the lines
for line in file:
    cleanLine = (line.strip())
    if ">" in cleanLine:
        count+= 1
    if int(count) == int(myScaff): #Checks for scaffold header and finds corresponding sequence
       count += 1 #To avoid it repeating infinetely      
       next_line = file.readline()
       
       myStart = int(myStart)   #math to get correct length
       myEnd = int(myEnd)
       LEN = myEnd - myStart
       linelen = len(next_line) #Is your operation possible?
       if linelen > LEN:
        new_line = next_line[myStart:][:LEN]
        outFile.write(cleanLine + "\n" + new_line)
       else:
        print ("Desired length cannot be longer than sequence, recheck values")
        sys.exit()
       
print ("Extracted positions",myStart, "to", myEnd, "from scaffold", myScaff)

