import sys
from math import *
from H import *
#a=['CC','CD','DT','EX','IN','JJ','MD','NN','RB','RP','TO','VB','WP','JJR','JJS','PRP$','NNP','NNS','POS','PRP','RBR','VBD','VBG','VBN','VBP','VBZ','WDT','WRB','NNPS','(',')',',',':']
a=['CD','CC','DT']
b='testing corpus.txt'
c=open(b,'r').read().split()



MMI=0
POS=[]
aa=[]
for s in a:
    for w in a:
        aa.append([s,w])
for pos in aa:
    #print pos
    listtrue=[]
    listfalse=[]
    #for cc in c:
        #print cc
    d=[(c[i-2:i],c[i])for i in range(len(c))]
    for item in d:
        #print item
        #print pos
        if pos==item[0]:
             #print item
             #print pos
               # print item
             listtrue.append(item[1])
        else:
               # print item
             listfalse.append(item[1])
             

    A=entropy(c)
    T=entropy(listtrue)
    F=entropy(listfalse)
    C=len(c)
    t=len(listtrue)
    f=len(listfalse)
    MI=A-(T*t+F*f)/C
    if MI>MMI:
       MMI=MI
       POS=pos
    print MI,MMI,POS
print '%s%s'%('MI=',MMI)
print '%s%s'%('whether the sentence is begin with',POS)

