# this function is to test the result 
import sys
import nltk
from math import *
from decimal import *
from nltk.book import *
def result(a,b,c,d):
    trainop=open(a,'r').read().split()
    testop=open(b,'r').read().split()
    e=0
    f=0
    mltrain=file(c,'w')
    
    mltest=file(d,'w')


    modeltrain=FreqDist(trainop)
    train=[(key,modeltrain.freq(key)) for key in modeltrain]
    for a in train:
        print>>mltrain,a
    mltrain.close()

    modeltest=FreqDist(testop)
    test=[(key,modeltest.freq(key)) for key in modeltest]
    for a in test:
        print>>mltest,a
    mltest.close()

#for a in train:
    #print a


    for a in train:
    #print a
    #print a[0]
        for b in test:
        #print b[0]
        #print 
            if a[0]==b[0]:
               #print a[0],b[0]            
                   e=Decimal(a[1])*Decimal(log(1/b[1],2))
               #print e
                   f=f+e
               #print f
    print f
    g=pow(2,Decimal(f))
    print g
result('trueword1.txt','trueword1.txt','truemodel1.txt','truemodel1.txt')
result('trueword1.txt','truewordtest1.txt','truemodel1.txt','truemodeltest1.txt')
result('falseword1.txt','falseword1.txt','falsemodel1.txt','falsemodel1.txt')
result('falseword1.txt','falsewordtest1.txt','falsemodel1.txt','falsemodeltest1.txt')

result('trueword21.txt','trueword21.txt','truemodel21.txt','truemodel21.txt')
result('trueword21.txt','truewordtest21.txt','truemodel21.txt','truemodeltest21.txt')
result('falseword21.txt','falseword21.txt','falsemodel21.txt','falsemodel21.txt')
result('falseword21.txt','falsewordtest21.txt','falsemodel21.txt','falsemodeltest21.txt')

result('trueword22.txt','trueword22.txt','truemodel22.txt','truemodel22.txt')
result('trueword22.txt','truewordtest22.txt','truemodel22.txt','truemodeltest22.txt')
result('falseword22.txt','falseword22.txt','falsemodel22.txt','falsemodel22.txt')
result('falseword22.txt','falsewordtest22.txt','falsemodel22.txt','falsemodeltest22.txt')
