# this function is to split the corpus in the (h,t)
b='testing corpus.txt'

c=open(b,'r').read().split()
bagofwords=file('bag of wordstest.txt','w')

#d=[(c[i-4:i],c[i])for i in range(4,len(c))]
for i in range(4,len(c)):
    d=c[i-4:i],c[i]
    #for item in d:
    #print item
    print >>bagofwords,d
bagofwords.close() 
