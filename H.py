import sys
import nltk
from nltk.book import *
from math import *
from decimal import *

def Entropy(x):
    wltest = open(x, 'r').read().split()
    dictionarytest=FreqDist(wltest)
    test=dictionarytest.keys()
    testi = [dictionarytest[key]for key in dictionarytest]     
    s=sum(testi)
    f=0
    for a in testi:
        p=Decimal(a)/Decimal(s)
        e=Decimal(p)*Decimal(log(1/p,2))
        f=f+e
    print f 

def entropy(x):
    dictionary=FreqDist(x)
    test=dictionary.keys()
    testi = [dictionary[key]for key in dictionary]     
    s=sum(testi)
    f=0
    for a in testi:
        p=Decimal(a)/Decimal(s)
        e=Decimal(p)*Decimal(log(1/p,2))
        f=f+e
    return f 
    
   

