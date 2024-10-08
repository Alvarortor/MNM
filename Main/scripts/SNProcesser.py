#SNProcesser

#Take file from promer
#adjust reading frame to make it easier to reading
#take position and mutation into tuple
	#Adjust for AA position, but also include nucleotide one
	#Combine isolates for similar tuple
#Report out
import os
import sys
import re
import math
from collections import defaultdict

snpFile = sys.argv[1]

try:
    path = os.path.abspath(snpFile)
    file = open(path, 'r')
except FileNotFoundError:
    print("Cannot find " + snpFile)
    sys.exit()

#Create lists to store amino acid classes and report large changes
aliphatic = ('G', 'A', 'V', 'L', 'I')
hydroxy = ('S', 'C', 'U', 'T', 'M')
cyclic = ('P')
aromatic = ('F', 'Y', 'W')
basic = ('H', 'K', 'R')
acidic = ('D', 'E', 'N', 'Q')
lists = (aliphatic, hydroxy, cyclic, aromatic, basic, acidic)
categories = ('aliphatic', 'hydroxy', 'cyclic', 'aromatic', 'basic', 'acidic')

mutations = list()


#listindex = 0;
def mutation_checker(normal, mut):
    for item in lists:
        count0 = item.count(normal)
        count1 = item.count(mut)
        if count0 > 0 and count1 > 0:
            return ("O") #similar
        else:
            return("X") #Dissimilar

      
data = list()
def refname(ref):
    strend = ref.index("_")
    name = ref[0:][:strend]
    return (name)
def quename(que):
    strend = que.index("_")
    name = que[0:][:strend]
    return (name)


def out_name(ref):
    gene_tag = ref.index("_") + 1
    outname = ref[gene_tag:]
    tagend = outname.index("_")
    outtag = outname[0:][:tagend]
    
    return (outtag)


#Helps to skip the native header in PROMER output    
count = 0
for line in file:
    if count < 4:
        file.readline()
        count +=1
    else:
        line = line.split("\t")
        frame_R = line[10]
        frame_Q = line[11]
        normal = line[1]
        mut = line[2]
    
        ref = line[12]
        rname = refname(ref)
        que = line[13]
        qname = quename(que)
        outname = out_name(ref)
        trans = normal + "->" + mut
        signif = mutation_checker(normal, mut)
        aapos = math.trunc((int(line[0]) + 2) / 3) #Converts from aa positon to the nucleotide one
        if frame_R == "1" and frame_Q == "1":
            tag = [(aapos, trans, signif, rname,"->"),qname]
            data.append(tag)
grouped = list()      
mapp = defaultdict(list)
for key, val in data:
     mapp[key].append(val)
res = [(key, *val) for key, val in mapp.items()]
grouped.append(res)

#Create output file for genes
outpath = os.path.abspath(outname + "_SNPS.txt")
OF = open(outpath, 'w+')

#N is normal, M is mutant based on selected reference ==Grp means same group or no
OF.write("[pos]\t[N->M]\t[==Grp]\t[Ref]\t\t[Matches]\n")
for item in res:
    info = str(item[0])
    isos = str(item[1:])
    label1 = info.replace(",","\t")
    label2 = label1.replace("'","")[1:][:-1]
    iso1 = isos.replace("'","")[1:][:-1]
    if (iso1[-1]) == ",":
        iso1 = iso1.replace(",","")
    data = str(label2 + "\t" + iso1 + "\n")
    OF.write(data)

print("Done!")