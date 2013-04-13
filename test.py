# this file is to build the unigram of training corpus on the root and calculte the log-likelihood and complexity
import sys
import nltk
from nltk.book import *
from math import *
from decimal import *
wltest = open('training corpus.txt', 'r').read().split()
#wftest = [wltest.count(p) for p in wltest]
#dictionarytest = dict(zip(wltest,wftest))
#test = [(dictionarytest[key], key) for key in dictionarytest]
dictionarytest=FreqDist(wltest)

myfile=file('training corpus unigram.txt','w')
mlt=[[key,dictionarytest.freq(key)] for key in dictionarytest]
for a in mlt:
    print>>myfile,a
myfile.close()

    
testi = [dictionarytest[key]for key in dictionarytest]
print sum(testi)
print len(testi)
d=0
f=0
for a in testi:
    #b=log(Decimal(a)/Decimal(sum(testi)),2)
    #print b	
    #d=d+b
    #print d
    p=Decimal(a)/Decimal(sum(testi))
    e=Decimal(p)*Decimal(log(1/p,2))
    #print e	
    f=f+e
    #print f
    
#c=Decimal(d)/Decimal(len(testi))
print f
g=pow(2,Decimal(f))
print g


    
