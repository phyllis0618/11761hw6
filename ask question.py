import sys
from math import *
from H import *
a=['CC','CD','DT','EX','IN','JJ','MD','NN','RB','RP','TO','VB','WP','JJR','JJS','PRP$','NNP','NNS','POS','PRP','RBR','VBD','VBG','VBN','VBP','VBZ','WDT','WRB','NNPS','(',')',',',':']
#aa=a.split()
#b='NNP NNPS NNS VBD CD NNS TO VB IN CD NNS ( CD NNS ) , DT CD NN NN , IN NNP POS NN NN '
b='training corpus.txt'
c=open(b,'r').read().split()


MMI=entropy(c)
POS=[]
for pos in a:
    listtrue=[]
    listfalse=[]
    #for cc in c:
        #print cc
    d=[(c[i-2:i],c[i])for i in range(len(c))]
    for item in d:
        #print item
        if pos in item[0]:
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
print '%s%s'%('whether the last two word in history contains ',POS)

MMI=entropy(c)
POS=[]
for pos in a:
    listtrue=[]
    listfalse=[]
    #for cc in c:
        #print cc
    d=[(c[i],c[i+1])for i in range(len(c)-1)]
    for item in d:
        #print item
        if pos == item[0]:
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
print '%s%s'%('whether the last in history is ',POS)

