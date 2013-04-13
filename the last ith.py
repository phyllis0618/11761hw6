# this function is to rank the most promising question
import sys
from math import *
from H import *
import heapq
a=['CC','CD','DT','EX','IN','JJ','MD','NN','RB','RP','TO','VB','WP','JJR','JJS','PRP$','NNP','NNS','POS','PRP','RBR','VBD','VBG','VBN','VBP','VBZ','WDT','WRB','NNPS','(',')',',',':']
#a=['CC','CD','DT','EX','IN','JJ','MD']
b='training corpus.txt'
c=open(b,'r').read().split()
#f=open(b)
#l1=f.readlines()
#l2=[x.split('],') for x in l1] 
#l3=[[x[0].replace('([',''),x[1].replace(')','')] for x in l2]

#for a in l3:
#    print a[0]
#print len(l3)
#A=3.733014193243648883304928797
A=entropy(b)
result=[]
ave=0
myfile=file('MI21.txt','w')
MMI=0
POS=[]
for pos in a:
   # print pos
    listtrue=[]
    listfalse=[]
    #for cc in c:
        #print cc
 #   d=[(c[0:4],c[4])for c in l3
   # for c in l3:
#        d=[c[0:4],c[4]]
    for item in l3:
        #print item[0]
        try:
            i=item[0].index(pos)
        except ValueError:
            i=-1
        if i>0:
                   # print item
            listtrue.append(item[1])
        else:
                   # print item
            listfalse.append(item[1])
            
    
   
    T=entropy(listtrue)
#    print T
    F=entropy(listfalse)
#    print F
    C=len(l3)
#    print C
    t=len(listtrue)
    
    f=len(listfalse)
    MI=Decimal(A)-(T*t+F*f)/C
    ave=ave+MI

#    print t,f,MI,ave
    if MI>MMI:
       MMI=MI
       POS=pos
    result.append(['MI=',MI,'whether the last four word in history contains ',pos])
    #print>>myfile,'%s%s%s%s'%( 'MI=',MI,'whether the last four word in history contains ',pos)
average=ave/(len(a)*len(l3))
#print '%s%s'%('MI=',MMI)
print>>myfile,'%s%s'%('average=',average)
print '%s%s'%('whether the last four word in history contains ',POS)

ave=0
MMI=0
POS=[]
for pos in a:
    listtrue=[]
    listfalse=[]
    #for cc in c:
        #print cc
 #   d=[(c[1:4],c[4])for c in l3]
    for item in l3:
        #print item
        try:
            i=item[0].index(pos)
        except ValueError:
            i=-1
        if i>0:
               # print item
            listtrue.append(item[1])
        else:
               # print item
            listfalse.append(item[1])
            

   
    T=entropy(listtrue)
    F=entropy(listfalse)
    C=len(l3)
    t=len(listtrue)
    f=len(listfalse)
    MI=Decimal(A)-(T*t+F*f)/C
    ave=ave+MI
    if MI>MMI:
       MMI=MI
       POS=pos
    #print MI,MMI,POS
    result.append(['MI=',MI,'whether the last three word in history contains ',pos])
    #print>>myfile,'%s%s%s%s'%( 'MI=',MI,'whether the last three word in history contains ',pos)
average=ave/(len(a)*len(l3))
#print '%s%s'%('MI=',MMI)
print>>myfile,'%s%s'%('average=',average)
print '%s%s'%('whether the last three word in history contains ',POS)

ave=0
MMI=0
POS=[]
for pos in a:
    listtrue=[]
    listfalse=[]
    #for cc in c:
        #print cc
 #   d=[(c[2:4],c[4])for c in l3]
    for item in l3:
        #print item
        try:
            i=item[0].index(pos)
        except ValueError:
            i=-1
        if i>0:
               # print item
            listtrue.append(item[1])
        else:
               # print item
            listfalse.append(item[1])
            


    T=entropy(listtrue)
    F=entropy(listfalse)
    C=len(l3)
    t=len(listtrue)
    f=len(listfalse)
    MI=Decimal(A)-(T*t+F*f)/C
    ave=ave+MI
    if MI>MMI:
       MMI=MI
       POS=pos
    #print MI,MMI,POS
    result.append(['MI=',MI,'whether the last two word in history contains ',pos])
    #print>>myfile,'%s%s%s%s'%( 'MI=',MI,'whether the last three word in history contains ',pos)
average=ave/(len(a)*len(l3))
#print '%s%s'%('MI=',MMI)
print>>myfile,'%s%s'%('average=',average)
print '%s%s'%('whether the last two word in history contains ',POS)

ave=0
MMI=0
POS=[]
for pos in a:
    listtrue=[]
    listfalse=[]
    #for cc in c:
        #print cc
 #   d=[(c[3],c[4])for c in l3]
    for item in l3:
        #print item
        if pos == item[0]:
               # print item
            listtrue.append(item[1])
        else:
               # print item
            listfalse.append(item[1])
            

  
    T=entropy(listtrue)
    F=entropy(listfalse)
    C=len(l3)
    t=len(listtrue)
    f=len(listfalse)
    MI=Decimal(A)-(T*t+F*f)/C
    ave=ave+MI
    if MI>MMI:
       MMI=MI
       POS=pos
    #print MI,MMI,POS
    result.append(['MI=',MI,'whether the last word in history contains ',pos])
    #print>>myfile,'%s%s%s%s'%( 'MI=',MI,'whether the last three word in history contains ',pos)
average=ave/(len(a)*len(l3))
#print '%s%s'%('MI=',MMI)
print>>myfile,'%s%s'%('average=',average)
print '%s%s'%('whether the last in history is ',POS)

ave=0
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
 #   d=[(c[2:4],c[4])for c in l3]
    for item in l3:
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
             

 
    T=entropy(listtrue)
    F=entropy(listfalse)
    C=len(l3)
    t=len(listtrue)
    f=len(listfalse)
    MI=Decimal(A)-(T*t+F*f)/C
    ave=ave+MI
    if MI>MMI:
       MMI=MI
       POS=pos
    #print MI,MMI,POS
    result.append(['MI=',MI,'whether the last two words in history are ',pos])
    #print>>myfile,'%s%s%s%s'%( 'MI=',MI,'whether the last two word in history are ',pos)
average=ave/(len(aa)*len(l3))
#print '%s%s'%('MI=',MMI)
print '%s%s'%('whether the last two word in history are ',POS)
print>>myfile,'%s%s'%('average=',average)


result.sort()
print>>myfile, heapq.nlargest(100,result)
print>>myfile, heapq.nsmallest(100,result)
myfile.close()
