import sys
from math import *
from H import *
import heapq
#a=['CC','CD','DT','EX','IN','JJ','MD','NN','RB','RP','TO','VB','WP','JJR','JJS','PRP$','NNP','NNS','POS','PRP','RBR','VBD','VBG','VBN','VBP','VBZ','WDT','WRB','NNPS','(',')',',',':']
a=['CC','CD','DT','EX','IN','JJ','MD','NN']
b='1.txt'
#c=open(b,'r').read().split()
f=open(b)
l1=f.readlines()
l2=[x.split('],') for x in l1]
#l2=[x.replace(',','') for x in l2]
#for a in l2:
    #print 'a=',a,'a0=',a[0],'a1=',a[1]
#l3=[[x[0].replace('([',''),x[1],x[2],x[3].replace(']',''),x[4].replace(')','')] for x in l2]
l3=[[x[0].replace('([',''),x[1].replace(')','')]for x in l2]
#for a in l3:
#     print a[0]
    #print a[0],a[1],a[2],a[3],a[4]
    #print a[4]
     
#print len(l3)
A=3.733014193243648883304928797
result=[]
ave=0
myfile=file('MI21.txt','w')
MMI=0
POS=[]
for pos in a:
    
    listtrue=[]
    listfalse=[]
 
    for item in l3:
        print item[0][0:3]
        #print item[1],pos
        if pos in item[0][0:3]:
     
 
              listtrue.append(item[1])
        else:
             
              listfalse.append(item[1])                   
        
    T=entropy(listtrue)
    print T
    F=entropy(listfalse)
    print F
    C=len(l3)
    print C
    t=len(listtrue)
    
    f=len(listfalse)
    MI=Decimal(A)-(T*t+F*f)/C
    ave=ave+MI

    print t,f,MI,ave
    if MI>MMI:
       MMI=MI
       POS=pos
    result.append(['MI=',MI,'whether the last four word in history contains ',pos])
    
average=ave/(len(a)*len(l3))
print '%s%s'%('MI=',MMI)
print>>myfile,'%s%s'%('average=',average)
print '%s%s'%('whether the last four word in history contains ',POS)
result.sort()
print>>myfile, heapq.nlargest(100,result)
print>>myfile, heapq.nsmallest(100,result)
myfile.close()
