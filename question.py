import sys

a=['CC','CD','DT','EX','IN','JJ','MD','NN','RB','RP','TO','VB','WP','JJR','JJS','PRP$','NNP','NNS','POS','PRP','RBR','VBD','VBG','VBN','VBP','VBZ','WDT','WRB','NNPS','(',')',',',':','.']
b='whether in history contains'
c='whether the sentence is begin with'
d='whether the last word in history is'
e='whether the last two word in history are'
f='whether the last word in history contains'
q='?'
myfile=file('question.txt','w')
for s in a:
	print>>myfile, '%s %s %s' %( b,s,q)

for s in a:
	
	print>>myfile, '%s %s %s' %( c,s,q)
for s in a:
	
	print>>myfile, '%s %s %s' %( d,s,q)
for s in a:
	
	print>>myfile, '%s %s %s' %( f,s,q)


for s in a:
    for w in a:
        print>>myfile, '%s %s %s %s' %( b,s,w,q)


for s in a:
    for w in a:
        print>>myfile, '%s %s %s %s' %( e,s,w,q)
myfile.close()
