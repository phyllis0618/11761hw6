import sys
from math import *
from H import *
import heapq
#a=['CC','CD','DT','EX','IN','JJ','MD','NN','RB','RP','TO','VB','WP','JJR','JJS','PRP$','NNP','NNS','POS','PRP','RBR','VBD','VBG','VBN','VBP','VBZ','WDT','WRB','NNPS','(',')',',',':']
a=['CC','CD','DT','EX','IN','JJ','MD']
b='testing corpus.txt'
c=open(b,'r').read().split()

result=[]
ave=0
myfile=file('MI.txt','w')
MMI=0
POS=[]
for pos in a:
    listtrue=[]
    listfalse=[]
    #for cc in c:
        #print cc
    d=[(c[i-4:i],c[i])for i in range(len(c))]
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
    ave=ave+MI
    if MI>MMI:
       MMI=MI
       POS=pos
    result.append(['MI=',MI,'whether the last four word in history contains ',pos])
    #print>>myfile,'%s%s%s%s'%( 'MI=',MI,'whether the last four word in history contains ',pos)
average=ave/(len(a)*len(d))
result.sort()
print '%s%s'%('MI=',MMI)
#for a in result:
#    print>>myfile,a
print>>myfile, heapq.nlargest(2,result)
print>>myfile, heapq.nsmallest(2,result)
print>>myfile,'%s%s'%('average=',average)
print '%s%s'%('whether the last four word in history contains ',POS)
myfile.close()
