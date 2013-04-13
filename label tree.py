import sys
import nltk
from nltk.book import *
#from math import *
#from decimal import *

a=['CC','CD','DT','EX','IN','JJ','MD','NN','RB','RP','TO','VB','WP','JJR','JJS','PRP$','NNP','NNS','POS','PRP','RBR','VBD','VBG','VBN','VBP','VBZ','WDT','WRB','NNPS','(',')',',',':']
#a=['CC','CD','DT','EX','IN','JJ','MD']
#a=['NN']
b='testing corpus.txt'

c=open(b,'r').read().split()
bagofwords=file('bag of wordstest.txt','w')


filetrue=file('truetest1.txt','w')
filefalse=file('falsetest1.txt','w')

filetrueword=file('truewordtest1.txt','w')
filefalseword=file('falsewordtest1.txt','w')



listtrue=[]
listtruemodel=[]
listfalse=[]
listfalsemodel=[]
d=[(c[i-4:i],c[i])for i in range(4,len(c))]
for item in d:
    #print item
    print >>bagofwords,item
    dd=item[0][3]
    #print dd
    if 'NNP' ==dd:
        listtrue.append(item)
        listtruemodel.append(item[1])
    else:
        listfalse.append(item)
        listfalsemodel.append(item[1])
bagofwords.close()       
for a in listtrue:
    print>>filetrue,a
filetrue.close()
for a in listfalse:
    print>>filefalse,a
filefalse.close()

for a in listtruemodel:
    print>>filetrueword,a
filetrueword.close

for a in listfalsemodel:
    print>>filefalseword,a
filefalseword.close()


# to split the subtree1
filetrue21=file('truetest21.txt','w')
filefalse21=file('falsetest21.txt','w')

filetrueword21=file('truewordtest21.txt','w')
filefalseword21=file('falsewordtest21.txt','w')



listtrue21=[]
listtruemodel21=[]
listfalse21=[]
listfalsemodel21=[]

for item in listtrue:
    
    dd=item[0][2]
    #print dd
    if 'NNP' ==dd:
        listtrue21.append(item)
        listtruemodel21.append(item[1])
    else:
        listfalse21.append(item)
        listfalsemodel21.append(item[1])
      
for a in listtrue21:
    print>>filetrue21,a
filetrue21.close()
for a in listfalse21:
    print>>filefalse21,a
filefalse21.close()

for a in listtruemodel21:
    print>>filetrueword21,a
filetrueword21.close

for a in listfalsemodel21:
    print>>filefalseword21,a
filefalseword21.close()

# to split the subtree2:
filetrue22=file('truetest22.txt','w')
filefalse22=file('falsetest22.txt','w')

filetrueword22=file('truewordtest22.txt','w')
filefalseword22=file('falsewordtest22.txt','w')



listtrue22=[]
listtruemodel22=[]
listfalse22=[]
listfalsemodel22=[]

for item in listfalse:
    
    dd=item[0][3]
    #print dd
    if 'DT' ==dd:
        listtrue22.append(item)
        listtruemodel22.append(item[1])
    else:
        listfalse22.append(item)
        listfalsemodel22.append(item[1])
      
for a in listtrue22:
    print>>filetrue22,a
filetrue22.close()
for a in listfalse22:
    print>>filefalse22,a
filefalse22.close()

for a in listtruemodel22:
    print>>filetrueword22,a
filetrueword21.close

for a in listfalsemodel22:
    print>>filefalseword22,a
filefalseword22.close()


