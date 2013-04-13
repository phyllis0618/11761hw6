import sys
from math import *
from H import *
a='NNP NNPS NNS'
aa=a.split()
#b='NNP NNPS NNS VBD CD NNS TO VB IN CD NNS ( CD NNS ) , DT CD NN NN , IN NNP POS NN NN '
b='testing corpus.txt'
c=open(b,'r').read().split()



for pos in aa:
    listtrue=[]
    listfalse=[]
    #for cc in c:
        #print cc
    d=[(c[i-2:i],c[i])for i in range(len(c))]
    for item in d:
        print item
        if pos in item[0]:
               # print item
            listtrue.append(item[1])
        else:
               # print item
            listfalse.append(item[1])
            
#    for i in listtrue:
#        print 'true'
#        print i
    
#    for i in listfalse:
#        print 'false'
#        print i
    Entropy(b)
    entropy(listtrue)
    entropy(listfalse)
